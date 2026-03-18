---
name: data-analyst
description: "Use this skill when analyzing datasets, identifying trends, running statistical summaries, or interpreting data to answer business questions. Trigger phrases: 'analyze this data', 'what does this data show', 'find patterns in', 'summarize these results', 'is this statistically significant'. Not for building production data pipelines, creating live dashboards, or writing database schema designs."
version: 1.0.0
author: community
tags: [data, analysis, statistics, insights]
license: MIT
---

# Data Analyst

## Overview
This skill guides structured exploratory data analysis (EDA) and statistical interpretation. It provides a repeatable framework for understanding datasets—from first-look summaries through pattern detection, outlier identification, hypothesis testing, and insight communication—so analysis is rigorous, reproducible, and actionable for stakeholders.

## When to Use
- You have a dataset (CSV, table, JSON) and need to understand what it contains
- A stakeholder asks "what's happening with our X metric?"
- You need to compare two groups or time periods
- You want to identify which variables correlate with an outcome
- You need to validate or challenge a business assumption with data
- You're preparing findings for a report, slide deck, or recommendation

## When NOT to Use
- Building or optimizing ETL pipelines (use a data engineering skill)
- Real-time streaming analytics
- Designing a database schema or data warehouse
- Machine learning model training (use an ML skill)
- Writing complex production SQL stored procedures

## Quick Reference
| Task | Approach |
|------|----------|
| First look at dataset | Shape, dtypes, `.head()`, `.describe()` |
| Check data quality | Null counts, duplicate rows, value ranges |
| Understand distributions | Histogram, box plot, mean/median/std |
| Find relationships | Correlation matrix, scatter plots |
| Compare groups | Group-by aggregations, t-test |
| Spot outliers | IQR method, Z-score, box plots |
| Communicate findings | Headline → context → evidence → action |
| Hypothesis test | Define H0/H1, choose test, check p-value |
| Segment analysis | Group by dimension, compare KPIs |
| Time-series trend | Rolling averages, period-over-period % change |

## Instructions

### Step 1: Understand the Business Question
Before touching data, clarify:
- What decision will this analysis inform?
- Who is the audience (executive, engineer, analyst)?
- What does "success" look like for this analysis?

Example: "We want to know if our new pricing page increased trial sign-ups."

### Step 2: First-Look Exploration (EDA Phase 1)
```python
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# Basic shape and types
print(df.shape)          # (rows, cols)
print(df.dtypes)         # column types
print(df.head(10))       # first rows

# Summary statistics
print(df.describe(include='all'))  # count, mean, std, min, quartiles, max

# Null values
print(df.isnull().sum())           # nulls per column
print(df.isnull().mean() * 100)    # % missing per column

# Duplicates
print(df.duplicated().sum())
```

### Step 3: Univariate Analysis — One Variable at a Time
For **numerical columns**:
- **Mean**: arithmetic average, sensitive to outliers
- **Median**: middle value, robust to outliers
- **Std**: spread of values; 1 std covers ~68% of a normal distribution
- **Skewness**: >1 right-skewed (long tail of high values); <-1 left-skewed

```python
col = df['revenue']
print(f"Mean:   {col.mean():.2f}")
print(f"Median: {col.median():.2f}")
print(f"Std:    {col.std():.2f}")
print(f"Skew:   {col.skew():.2f}")
```

For **categorical columns**:
```python
print(df['region'].value_counts())
print(df['region'].value_counts(normalize=True) * 100)  # percentages
```

### Step 4: Bivariate Analysis — Relationships Between Variables
**Correlation** (numerical vs numerical):
```python
corr_matrix = df[['revenue', 'units_sold', 'discount_pct', 'marketing_spend']].corr()
print(corr_matrix.round(2))
# Interpretation: |r| > 0.7 strong, 0.4–0.7 moderate, < 0.4 weak
```

**Group comparison** (categorical vs numerical):
```python
df.groupby('region')['revenue'].agg(['mean', 'median', 'std', 'count'])
```

**Pivot for cross-tab**:
```python
pd.crosstab(df['product_category'], df['customer_segment'], values=df['revenue'], aggfunc='sum')
```

### Step 5: Outlier Detection
**IQR Method** (robust, non-parametric):
```python
Q1 = df['revenue'].quantile(0.25)
Q3 = df['revenue'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['revenue'] < lower) | (df['revenue'] > upper)]
print(f"Outliers: {len(outliers)} rows ({len(outliers)/len(df)*100:.1f}%)")
```

**Z-Score Method** (assumes normal distribution):
```python
from scipy import stats
z_scores = np.abs(stats.zscore(df['revenue']))
outliers_z = df[z_scores > 3]
```

### Step 6: Hypothesis Testing Basics
When comparing two groups (e.g., control vs treatment):

```python
from scipy import stats

control = df[df['group'] == 'control']['conversion_rate']
treatment = df[df['group'] == 'treatment']['conversion_rate']

# Two-sample t-test
t_stat, p_value = stats.ttest_ind(control, treatment)
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Statistically significant difference (p < 0.05)")
else:
    print("No statistically significant difference")
```

For proportions (e.g., click rates):
```python
from statsmodels.stats.proportion import proportions_ztest
count = np.array([treatment_conversions, control_conversions])
nobs  = np.array([treatment_n, control_n])
stat, pval = proportions_ztest(count, nobs)
```

### Step 7: Communicate Findings
Use the **BLOT structure**: Bottom Line On Top
1. **Headline**: The single most important finding
2. **Context**: Why this matters
3. **Evidence**: Data supporting the claim (keep it to 3 key numbers)
4. **Recommendation**: What should happen next

## Examples

### Example 1: Analyze Sales Data Trends
**Input:** Monthly sales CSV with columns: `date`, `region`, `product`, `revenue`, `units_sold`, `discount_pct`

**Analysis approach:**
```python
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

# Monthly revenue trend
monthly = df.groupby('month')['revenue'].sum().reset_index()
monthly['pct_change'] = monthly['revenue'].pct_change() * 100

# Revenue by region
region_summary = df.groupby('region').agg(
    total_revenue=('revenue', 'sum'),
    avg_order_value=('revenue', 'mean'),
    total_units=('units_sold', 'sum')
).sort_values('total_revenue', ascending=False)

# Discount correlation with revenue
corr = df[['revenue', 'discount_pct']].corr().iloc[0, 1]
print(f"Discount vs Revenue correlation: {corr:.2f}")
```

**Output insight:** "Revenue grew 12% MoM in Q3, driven primarily by the West region (+34%). However, the North region is declining (−8% MoM). Discount rate correlates negatively with revenue per order (r = −0.42), suggesting aggressive discounting is not recovering volume losses."

---

### Example 2: Interpret Survey Results
**Input:** NPS survey data with columns: `respondent_id`, `score` (0–10), `segment`, `comment`

```python
df['nps_category'] = pd.cut(
    df['score'],
    bins=[-1, 6, 8, 10],
    labels=['Detractor', 'Passive', 'Promoter']
)

summary = df['nps_category'].value_counts(normalize=True) * 100
promoters = summary.get('Promoter', 0)
detractors = summary.get('Detractor', 0)
nps_score = promoters - detractors

print(f"NPS Score: {nps_score:.1f}")
print(f"Promoters: {promoters:.1f}%")
print(f"Detractors: {detractors:.1f}%")

# NPS by segment
df.groupby('segment').apply(
    lambda x: (
        (x['nps_category'] == 'Promoter').mean() -
        (x['nps_category'] == 'Detractor').mean()
    ) * 100
).sort_values()
```

**Output insight:** "Overall NPS is +42 (industry average: +31). Enterprise customers score +68, while SMB customers score only +18—suggesting an onboarding gap for smaller accounts. Top detractor theme: 'slow support response times' (mentioned in 38% of Detractor comments)."

## Best Practices
- Always ask the business question before opening the data
- State your assumptions explicitly (e.g., "excluding rows where revenue < 0")
- Round numbers appropriately for your audience (executives: 1 decimal; engineers: 3+ decimals)
- Distinguish correlation from causation in all communications
- Include sample sizes in every comparison (n=30 vs n=30,000 tells a different story)
- Use median over mean for skewed distributions (salaries, order values, response times)
- Validate findings against business intuition; anomalies may be data quality issues

## Common Mistakes
- Reporting averages without standard deviation or distribution context
- Comparing groups with very different sample sizes without noting it
- Treating correlation as causation (e.g., "discount causes lower revenue")
- Ignoring data freshness—always check the date range of your data
- Over-indexing on a single metric; always check at least 2–3 related metrics
- Not filtering out test/internal users from customer-facing metrics
- Forgetting to handle time zones when aggregating date-based data

## Tips & Tricks
- Start every analysis with `df.describe()` and `df.isnull().sum()`—it catches 80% of data issues
- A box plot reveals outliers, IQR, and skewness in one glance—use it before any group comparison
- When a metric looks wrong, add a row count to the aggregation to check for sample size issues
- Use `.value_counts(dropna=False)` to catch NaN values hiding in categorical columns
- Period-over-period % change is almost always more meaningful than raw numbers for trends
- Keep a running "data diary" noting any filters, exclusions, or transformations applied

## Related Skills
- [chart-builder](../../data/chart-builder/SKILL.md)
- [sql-analyst](../../data/sql-analyst/SKILL.md)
- [data-cleaner](../../data/data-cleaner/SKILL.md)
- [dashboard-designer](../../data/dashboard-designer/SKILL.md)
