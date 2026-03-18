---
name: sql-analyst
description: "Use this skill when writing SQL queries for data analysis, reporting, or business metrics. Trigger phrases: 'write a SQL query to', 'how do I calculate in SQL', 'build a report using SQL', 'SQL for monthly active users', 'write a retention query'. Not for database administration, schema design, query optimization for production systems, or NoSQL databases."
version: 1.0.0
author: community
tags: [data, sql, analysis, reporting]
license: MIT
---

# SQL Analyst

## Overview
This skill provides analytical SQL patterns for answering business questions from relational databases. It covers GROUP BY aggregations, window functions, CTEs, subqueries, date functions, and common business metrics queries (revenue, retention, funnel analysis, cohort analysis). The focus is on readable, correct analytical SQL that produces actionable insights—not on DBA-level optimization or schema changes.

## When to Use
- You need to query a database to answer a business question
- Building a report, dashboard data source, or ad-hoc analysis
- Calculating business metrics: revenue, retention, MAU, conversion, cohort analysis
- Translating a business question ("how many users came back in month 2?") into SQL
- Understanding what data exists in a table and what it means

## When NOT to Use
- Designing or altering database schemas (`CREATE TABLE`, `ALTER TABLE`)
- Database administration (indexes, query plan optimization, partitioning)
- Loading/transforming large datasets in production ETL systems
- MongoDB, Cassandra, or other NoSQL databases (different query languages)
- Writing stored procedures or database functions for production systems

## Quick Reference
| Pattern | SQL Construct | Use Case |
|---------|---------------|----------|
| Aggregate by group | `GROUP BY ... HAVING` | Revenue by region, count by category |
| Running total | `SUM() OVER (ORDER BY date)` | Cumulative revenue |
| Rank within group | `RANK() / ROW_NUMBER() OVER (PARTITION BY ...)` | Top N per category |
| Period-over-period | `LAG() OVER (ORDER BY month)` | Month-over-month comparison |
| Deduplication | `ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC)` | Keep most recent record |
| Percentage of total | `SUM(val) / SUM(SUM(val)) OVER ()` | Revenue share by region |
| Multi-step logic | CTE (`WITH ...`) | Break complex queries into steps |
| Conditional count | `COUNT(CASE WHEN cond THEN 1 END)` | Count subset within aggregate |
| Date truncation | `DATE_TRUNC('month', date)` | Aggregate by month/week/quarter |
| Cohort analysis | Self-join or DATEDIFF on first/return events | Retention calculation |

## Instructions

### Step 1: Understand the Business Question
Before writing SQL, translate the question into data terms:
- **What table(s)** hold the relevant data?
- **What is the grain** of each table (one row per what)?
- **What filters** apply (date range, user segment, product)?
- **What is the output shape**? (one number, time series, grouped table)

### Step 2: Basic Aggregation Patterns

**GROUP BY with multiple metrics:**
```sql
SELECT
    region,
    product_category,
    COUNT(DISTINCT order_id)          AS num_orders,
    COUNT(DISTINCT customer_id)       AS num_customers,
    SUM(revenue)                      AS total_revenue,
    AVG(revenue)                      AS avg_order_value,
    SUM(revenue) / COUNT(DISTINCT order_id) AS revenue_per_order
FROM orders
WHERE order_date >= '2024-01-01'
  AND status = 'completed'
GROUP BY region, product_category
ORDER BY total_revenue DESC;
```

**HAVING** — filter aggregated results:
```sql
-- Regions with more than 100 orders and avg order value > $500
SELECT
    region,
    COUNT(*) AS num_orders,
    AVG(revenue) AS avg_order_value
FROM orders
GROUP BY region
HAVING COUNT(*) > 100
   AND AVG(revenue) > 500;
```

### Step 3: Window Functions

**Running total (cumulative revenue):**
```sql
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER (ORDER BY order_date) AS cumulative_revenue
FROM orders
ORDER BY order_date;
```

**Period-over-period with LAG():**
```sql
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(revenue) AS monthly_revenue
    FROM orders
    GROUP BY 1
)
SELECT
    month,
    monthly_revenue,
    LAG(monthly_revenue) OVER (ORDER BY month) AS prev_month_revenue,
    ROUND(
        (monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY month))
        / NULLIF(LAG(monthly_revenue) OVER (ORDER BY month), 0) * 100,
    1) AS pct_change
FROM monthly
ORDER BY month;
```

**Rank within group (top product per region):**
```sql
WITH ranked AS (
    SELECT
        region,
        product,
        SUM(revenue) AS total_revenue,
        RANK() OVER (PARTITION BY region ORDER BY SUM(revenue) DESC) AS rnk
    FROM orders
    GROUP BY region, product
)
SELECT region, product, total_revenue
FROM ranked
WHERE rnk = 1;
```

**Percentage of total per group:**
```sql
SELECT
    region,
    SUM(revenue) AS region_revenue,
    ROUND(
        SUM(revenue) * 100.0 / SUM(SUM(revenue)) OVER (),
    1) AS pct_of_total
FROM orders
GROUP BY region
ORDER BY region_revenue DESC;
```

**Deduplication — keep most recent record per customer:**
```sql
WITH deduped AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC) AS rn
    FROM customers
)
SELECT * FROM deduped WHERE rn = 1;
```

### Step 4: CTEs (Common Table Expressions)
Use CTEs to break complex queries into readable, testable steps.

```sql
-- Monthly revenue + rolling 3-month average + growth flag
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(revenue)                    AS revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY 1
),
rolling_avg AS (
    SELECT
        month,
        revenue,
        AVG(revenue) OVER (
            ORDER BY month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS rolling_3m_avg
    FROM monthly_revenue
)
SELECT
    month,
    revenue,
    ROUND(rolling_3m_avg, 0) AS rolling_3m_avg,
    CASE WHEN revenue > rolling_3m_avg THEN 'Above trend' ELSE 'Below trend' END AS trend_status
FROM rolling_avg
ORDER BY month;
```

### Step 5: Business Metrics Queries

**Monthly Active Users (MAU):**
```sql
SELECT
    DATE_TRUNC('month', event_date) AS month,
    COUNT(DISTINCT user_id)          AS mau
FROM user_events
WHERE event_type = 'session_start'
GROUP BY 1
ORDER BY 1;
```

**Revenue by cohort (signup month):**
```sql
WITH user_cohorts AS (
    SELECT
        user_id,
        DATE_TRUNC('month', created_at) AS cohort_month
    FROM users
),
monthly_revenue AS (
    SELECT
        o.customer_id,
        DATE_TRUNC('month', o.order_date) AS order_month,
        SUM(o.revenue) AS revenue
    FROM orders o
    GROUP BY 1, 2
)
SELECT
    c.cohort_month,
    r.order_month,
    DATEDIFF('month', c.cohort_month, r.order_month) AS months_since_signup,
    COUNT(DISTINCT r.customer_id) AS paying_users,
    SUM(r.revenue) AS cohort_revenue
FROM user_cohorts c
JOIN monthly_revenue r ON c.user_id = r.customer_id
GROUP BY 1, 2, 3
ORDER BY 1, 3;
```

**Conversion funnel:**
```sql
SELECT
    COUNT(DISTINCT CASE WHEN step = 'view_product'   THEN user_id END) AS step1_view,
    COUNT(DISTINCT CASE WHEN step = 'add_to_cart'    THEN user_id END) AS step2_cart,
    COUNT(DISTINCT CASE WHEN step = 'begin_checkout' THEN user_id END) AS step3_checkout,
    COUNT(DISTINCT CASE WHEN step = 'purchase'       THEN user_id END) AS step4_purchase,
    ROUND(
        COUNT(DISTINCT CASE WHEN step = 'purchase' THEN user_id END) * 100.0
        / NULLIF(COUNT(DISTINCT CASE WHEN step = 'view_product' THEN user_id END), 0),
    1) AS overall_conversion_pct
FROM funnel_events
WHERE event_date >= '2024-01-01';
```

**Day-1 / Day-7 / Day-30 retention:**
```sql
WITH first_seen AS (
    SELECT user_id, MIN(DATE(event_date)) AS first_day
    FROM events
    GROUP BY user_id
),
activity AS (
    SELECT DISTINCT user_id, DATE(event_date) AS active_day
    FROM events
)
SELECT
    f.first_day                        AS cohort_date,
    COUNT(DISTINCT f.user_id)          AS cohort_size,
    COUNT(DISTINCT CASE WHEN a.active_day = f.first_day + INTERVAL '1 day'  THEN f.user_id END) AS d1_retained,
    COUNT(DISTINCT CASE WHEN a.active_day = f.first_day + INTERVAL '7 days' THEN f.user_id END) AS d7_retained,
    COUNT(DISTINCT CASE WHEN a.active_day = f.first_day + INTERVAL '30 days' THEN f.user_id END) AS d30_retained,
    ROUND(COUNT(DISTINCT CASE WHEN a.active_day = f.first_day + INTERVAL '1 day' THEN f.user_id END) * 100.0
          / NULLIF(COUNT(DISTINCT f.user_id), 0), 1) AS d1_rate,
    ROUND(COUNT(DISTINCT CASE WHEN a.active_day = f.first_day + INTERVAL '7 days' THEN f.user_id END) * 100.0
          / NULLIF(COUNT(DISTINCT f.user_id), 0), 1) AS d7_rate,
    ROUND(COUNT(DISTINCT CASE WHEN a.active_day = f.first_day + INTERVAL '30 days' THEN f.user_id END) * 100.0
          / NULLIF(COUNT(DISTINCT f.user_id), 0), 1) AS d30_rate
FROM first_seen f
LEFT JOIN activity a ON f.user_id = a.user_id
GROUP BY 1
ORDER BY 1;
```

### Step 6: Date Functions Reference
| Function | PostgreSQL | BigQuery | Snowflake | MySQL |
|----------|------------|---------|-----------|-------|
| Truncate to month | `DATE_TRUNC('month', d)` | `DATE_TRUNC(d, MONTH)` | `DATE_TRUNC('month', d)` | `DATE_FORMAT(d, '%Y-%m-01')` |
| Difference in days | `d2 - d1` | `DATE_DIFF(d2, d1, DAY)` | `DATEDIFF(day, d1, d2)` | `DATEDIFF(d2, d1)` |
| Add interval | `d + INTERVAL '7 days'` | `DATE_ADD(d, INTERVAL 7 DAY)` | `DATEADD(day, 7, d)` | `DATE_ADD(d, INTERVAL 7 DAY)` |
| Today | `CURRENT_DATE` | `CURRENT_DATE()` | `CURRENT_DATE()` | `CURDATE()` |
| Extract year | `EXTRACT(YEAR FROM d)` | `EXTRACT(YEAR FROM d)` | `YEAR(d)` | `YEAR(d)` |

## Examples

### Example 1: Calculate Monthly Active Users (MAU) with MoM Growth
**Input:** Table `user_events(user_id, event_type, event_date)` in PostgreSQL.

```sql
WITH mau AS (
    SELECT
        DATE_TRUNC('month', event_date) AS month,
        COUNT(DISTINCT user_id)          AS mau
    FROM user_events
    WHERE event_date >= '2023-01-01'
    GROUP BY 1
)
SELECT
    month,
    mau,
    LAG(mau) OVER (ORDER BY month)                           AS prev_mau,
    mau - LAG(mau) OVER (ORDER BY month)                    AS mau_change,
    ROUND(
        (mau - LAG(mau) OVER (ORDER BY month)) * 100.0
        / NULLIF(LAG(mau) OVER (ORDER BY month), 0),
    1)                                                        AS mau_growth_pct
FROM mau
ORDER BY month;
```

**Output:**
```
month       | mau   | prev_mau | mau_change | mau_growth_pct
------------|-------|----------|------------|---------------
2023-01-01  | 8420  | null     | null       | null
2023-02-01  | 9130  | 8420     | 710        | 8.4
2023-03-01  | 10240 | 9130     | 1110       | 12.2
```

---

### Example 2: Build a Cohort Retention Query
**Input:** Tables `users(user_id, created_at)` and `orders(order_id, customer_id, order_date)` in Snowflake.

```sql
WITH cohorts AS (
    SELECT
        user_id,
        DATE_TRUNC('month', created_at) AS cohort_month
    FROM users
    WHERE created_at >= '2023-01-01'
),
order_activity AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', order_date) AS order_month
    FROM orders
),
cohort_data AS (
    SELECT
        c.cohort_month,
        DATEDIFF('month', c.cohort_month, oa.order_month) AS month_number,
        COUNT(DISTINCT c.user_id) AS retained_users
    FROM cohorts c
    LEFT JOIN order_activity oa ON c.user_id = oa.customer_id
    GROUP BY 1, 2
),
cohort_sizes AS (
    SELECT cohort_month, COUNT(*) AS cohort_size
    FROM cohorts
    GROUP BY 1
)
SELECT
    cd.cohort_month,
    cs.cohort_size,
    cd.month_number,
    cd.retained_users,
    ROUND(cd.retained_users * 100.0 / cs.cohort_size, 1) AS retention_rate
FROM cohort_data cd
JOIN cohort_sizes cs ON cd.cohort_month = cs.cohort_month
WHERE cd.month_number BETWEEN 0 AND 6
ORDER BY cd.cohort_month, cd.month_number;
```

**Output:** A retention table showing what % of each monthly signup cohort placed an order in each subsequent month — the foundation of a retention heatmap.

## Best Practices
- Always alias aggregated columns (`SUM(revenue) AS total_revenue`) for readability
- Use CTEs instead of nested subqueries when logic has more than 2 steps
- Use `COUNT(DISTINCT user_id)` not `COUNT(user_id)` when counting unique entities
- Use `NULLIF(denominator, 0)` in division to avoid divide-by-zero errors
- Filter early (in WHERE, not HAVING) to reduce rows before aggregation
- Use `DATE_TRUNC()` for time grouping—it handles month-end dates correctly
- Always include a date filter in analytical queries; querying all-time data is rarely needed and always slow

## Common Mistakes
- `COUNT(*)` when you mean `COUNT(DISTINCT user_id)`—counts duplicate rows
- Division without `NULLIF`: `revenue / sessions` crashes when sessions = 0
- Using HAVING instead of WHERE to filter raw rows (HAVING runs after GROUP BY)
- Forgetting `LEFT JOIN` vs `INNER JOIN`: inner join silently drops users with no activity
- Comparing dates with string literals that aren't in ISO format: `WHERE date > '01/01/2024'` fails in most databases
- Not testing CTEs step-by-step before assembling the full query
- Window functions in WHERE clause (not allowed; use a subquery or CTE)

## Tips & Tricks
- Build and test CTEs one at a time: write just the first CTE, run it, verify the output, then add the next
- `EXPLAIN ANALYZE` (PostgreSQL) or `QUERY PROFILE` (Snowflake) to understand slow queries
- Use `LIMIT 100` during development; remove for final runs
- `QUALIFY ROW_NUMBER() OVER (...) = 1` in Snowflake/BigQuery deduplicates without a wrapping CTE
- `SELECT * EXCEPT (col1, col2)` in BigQuery to exclude specific columns without listing all the rest
- Store complex metric definitions as views so they can be reused across reports

## Related Skills
- [data-analyst](../../data/data-analyst/SKILL.md)
- [data-cleaner](../../data/data-cleaner/SKILL.md)
- [dashboard-designer](../../data/dashboard-designer/SKILL.md)
