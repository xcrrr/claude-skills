---
name: sql-expert
description: "Use this skill when writing, optimizing, or reviewing SQL queries, designing database schemas, or diagnosing slow query performance. Trigger phrases: 'write a SQL query', 'optimize this query', 'why is this slow', 'how do I join these tables'. Not for NoSQL databases or ORM-specific code generation."
version: 1.0.0
author: community
tags: [coding, sql, database, query-optimization]
license: MIT
---

# SQL Expert

## Overview
The SQL Expert skill covers writing efficient, correct SQL queries — from basic CRUD to advanced analytics using window functions, CTEs, and complex joins. It includes a systematic query optimization process (analyze → explain → index → rewrite), common anti-patterns to avoid, and guidance on aggregations, subqueries, and report-style queries. The examples use standard ANSI SQL with notes for PostgreSQL, MySQL, and SQLite dialect differences where relevant.

## When to Use
- Writing SQL queries for data retrieval, aggregation, or reporting
- Optimizing a slow or resource-intensive query
- Designing a normalized database schema
- Understanding and using window functions or CTEs
- Identifying and fixing N+1 query patterns in application code

## When NOT to Use
- MongoDB, DynamoDB, or other NoSQL query languages (different paradigm)
- ORM-specific query builders like SQLAlchemy DSL or ActiveRecord (use framework docs)
- Database administration tasks (backups, replication, user management)
- Full-text search configuration (Elasticsearch, pgvector, etc.)

## Quick Reference
| Technique | When to Use |
|-----------|-------------|
| `EXPLAIN ANALYZE` | Diagnose slow query; understand index usage |
| Index on filter column | `WHERE col = ?`, `ORDER BY col`, `JOIN ON col` |
| Composite index | Multiple columns in WHERE/ORDER BY together |
| CTE (`WITH`) | Break complex queries into readable steps |
| Window function | Ranking, running totals, moving averages |
| `LATERAL JOIN` | Correlated subquery per row (PostgreSQL) |
| `COALESCE(a, b)` | Return first non-null value |
| `FILTER (WHERE ...)` | Conditional aggregation without CASE |
| `DISTINCT ON` | First row per group (PostgreSQL) |
| Partial index | Index only rows matching a WHERE condition |

## Instructions

1. **Understand the data model**
   - Identify the relevant tables, their primary keys, and foreign key relationships.
   - Know the cardinality: one-to-many, many-to-many (junction table needed).
   - Check column data types — comparing varchar to int causes implicit casts that break index usage.

2. **Write a correct query first**
   - Start with the simplest correct query. Get the right answer before optimizing.
   - Use CTEs (`WITH` clauses) to break complex queries into named, readable steps.
   - Verify the result against a small known dataset before running on production.

3. **Analyze slow queries with EXPLAIN**
   ```sql
   EXPLAIN ANALYZE
   SELECT ...;
   ```
   - Look for `Seq Scan` on large tables — almost always means a missing index.
   - Look for `Hash Join` vs `Nested Loop` — hash joins are better for large datasets.
   - Check `rows=` estimates vs actual rows — large differences mean stale statistics (`ANALYZE table_name`).
   - High `cost=` numbers are relative — focus on the most expensive nodes.

4. **Add indexes strategically**
   - Add an index on every foreign key and every column used in `WHERE`, `JOIN ON`, or `ORDER BY`.
   - Use composite indexes for queries that filter on multiple columns together: `(status, created_at)`.
   - Partial indexes for sparse conditions: `CREATE INDEX ON orders (user_id) WHERE status = 'pending'`.
   - Too many indexes slow down writes — audit with `pg_stat_user_indexes` for unused indexes.

5. **Avoid common anti-patterns**
   - **N+1 queries**: fetching child records in a loop. Solve with a JOIN or a single `IN (...)` query.
   - **SELECT \***: fetches unused columns; prevents index-only scans.
   - **Functions on indexed columns in WHERE**: `WHERE YEAR(created_at) = 2024` breaks index use. Use range: `WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'`.
   - **OR across columns**: use `UNION ALL` instead for index friendliness.
   - **Implicit type coercion**: `WHERE user_id = '42'` when `user_id` is integer.

6. **Use window functions for analytics**
   - `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()` for ranking within groups.
   - `SUM() OVER (PARTITION BY ... ORDER BY ...)` for running totals.
   - `LAG()` / `LEAD()` for comparing a row to the previous/next row.
   - `NTILE(n)` for percentile buckets.

7. **Normalize schema to at least 3NF**
   - Each table represents one entity.
   - No repeating groups or arrays in columns.
   - Every non-key column depends on the whole primary key (no partial dependency).
   - Consider denormalization only for read-heavy, performance-critical paths.

## Examples

### Example 1: Optimize a slow query

**Input:**
```sql
-- This query takes 8 seconds on a table with 5 million rows
SELECT *
FROM orders
WHERE YEAR(created_at) = 2024
  AND status = 'completed'
ORDER BY created_at DESC;
```

**EXPLAIN output shows:** Full table scan (`Seq Scan`), no indexes used.

**Output (optimized):**

**Problem 1:** `YEAR(created_at)` applies a function to the column, preventing index usage.
**Fix:** Use a range comparison:
```sql
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01'
```

**Problem 2:** `SELECT *` fetches all columns. Use only needed columns.

**Problem 3:** No index on `(status, created_at)`.

**Optimized query:**
```sql
SELECT
  id,
  user_id,
  total_amount,
  status,
  created_at
FROM orders
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01'
  AND status = 'completed'
ORDER BY created_at DESC;
```

**Required index:**
```sql
-- Composite index: status first (equality), then created_at (range + sort)
CREATE INDEX idx_orders_status_created
  ON orders (status, created_at DESC);
```

**Result:** Query time drops from 8s to ~15ms.

---

### Example 2: Write a complex report query with CTEs and window functions

**Input:** "Show me the top 3 products by revenue for each category, with their rank and percent of category revenue."

**Schema:**
```sql
products (id, name, category_id)
categories (id, name)
order_items (id, order_id, product_id, quantity, unit_price)
```

**Output:**
```sql
WITH product_revenue AS (
  -- Step 1: Calculate total revenue per product
  SELECT
    p.id         AS product_id,
    p.name       AS product_name,
    c.id         AS category_id,
    c.name       AS category_name,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM order_items oi
  JOIN products p ON p.id = oi.product_id
  JOIN categories c ON c.id = p.category_id
  GROUP BY p.id, p.name, c.id, c.name
),
ranked AS (
  -- Step 2: Rank products within each category and compute category share
  SELECT
    product_id,
    product_name,
    category_id,
    category_name,
    revenue,
    RANK() OVER (
      PARTITION BY category_id
      ORDER BY revenue DESC
    ) AS rank_in_category,
    ROUND(
      100.0 * revenue / SUM(revenue) OVER (PARTITION BY category_id),
      2
    ) AS pct_of_category
  FROM product_revenue
)
-- Step 3: Filter to top 3 per category
SELECT
  category_name,
  rank_in_category,
  product_name,
  revenue,
  pct_of_category
FROM ranked
WHERE rank_in_category <= 3
ORDER BY category_name, rank_in_category;
```

**Sample output:**
```
category_name | rank | product_name      | revenue  | pct_of_category
--------------+------+-------------------+----------+----------------
Electronics   |    1 | Wireless Headset  | 125400.00|   34.21
Electronics   |    2 | Laptop Stand      |  98200.00|   26.80
Electronics   |    3 | USB-C Hub         |  76100.00|   20.77
Clothing      |    1 | Winter Jacket     |  89300.00|   41.12
...
```

---

### Example 3: Fix an N+1 query

**Input (Python with ORM, causing N+1):**
```python
orders = Order.query.filter_by(status='completed').all()
for order in orders:
    # This fires a separate query for EACH order — N+1!
    user = User.query.get(order.user_id)
    print(f"{user.email}: {order.total}")
```

**Output (single query with JOIN):**
```sql
SELECT
  o.id,
  o.total,
  o.created_at,
  u.email,
  u.name
FROM orders o
JOIN users u ON u.id = o.user_id
WHERE o.status = 'completed'
ORDER BY o.created_at DESC;
```

Or using SQLAlchemy eager loading:
```python
orders = (
    Order.query
    .options(joinedload(Order.user))
    .filter_by(status='completed')
    .all()
)
for order in orders:
    print(f"{order.user.email}: {order.total}")  # No extra queries
```

## Best Practices
- Always use parameterized queries — never concatenate user input into SQL strings (SQL injection)
- Alias table names in multi-table queries: `orders o`, `users u` for readability
- Format SQL with consistent capitalization: keywords UPPER, identifiers lower
- Test queries on a subset of data before running on full production tables
- Use transactions for multi-statement writes to ensure atomicity
- Document complex queries with inline comments explaining the intent of each step

## Common Mistakes
- Forgetting `GROUP BY` when using aggregate functions (returns wrong results or error)
- Using `HAVING` when `WHERE` is correct (`WHERE` filters before aggregation; `HAVING` after)
- Joining on non-indexed columns, causing full table scans on both tables
- Using `NOT IN` with a subquery that can return NULL (always returns zero rows — use `NOT EXISTS`)
- Assuming `ORDER BY` without `LIMIT` returns results in a consistent order (it doesn't)
- Running `UPDATE` or `DELETE` without a `WHERE` clause in production

## Tips & Tricks
- `EXPLAIN (ANALYZE, BUFFERS)` in PostgreSQL shows cache hit vs disk read — crucial for identifying I/O bottlenecks
- `pg_stat_statements` extension tracks the slowest queries in production automatically
- Use `RETURNING id` in `INSERT`/`UPDATE` to get the affected row's data without a second query
- `COPY` command is orders of magnitude faster than `INSERT` for bulk data loads
- `GENERATE_SERIES()` in PostgreSQL is excellent for filling date gaps in reports

## Related Skills
- [code-reviewer](../code-reviewer/SKILL.md)
- [api-designer](../api-designer/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
- [architecture-designer](../architecture-designer/SKILL.md)
