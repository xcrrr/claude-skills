---
name: data-cleaner
description: "Use this skill when preparing raw data for analysis—handling missing values, removing duplicates, fixing data types, resolving inconsistent formats, or filtering outliers. Trigger phrases: 'clean this data', 'fix the missing values', 'standardize these dates', 'deduplicate this dataset', 'the data has formatting issues'. Not for designing database schemas, building ETL pipelines for production systems, or statistical modeling."
version: 1.0.0
author: community
tags: [data, cleaning, preprocessing, pandas]
license: MIT
---

# Data Cleaner

## Overview
This skill provides a structured approach to data quality—diagnosing issues in raw datasets and resolving them systematically before analysis or modeling. It covers the six most common data problems (missing values, duplicates, wrong types, outliers, inconsistent formats, and invalid values), with practical pandas code snippets and decision logic for each. Clean data is the foundation of trustworthy analysis.

## When to Use
- You received a raw CSV, Excel file, or database export and need to prepare it for analysis
- A dataset has null values, duplicate rows, or mismatched formats
- Date strings are inconsistent (e.g., "2023-01-15", "Jan 15, 2023", "15/01/23")
- Categorical columns have spelling variations ("USA", "U.S.A.", "United States")
- Numeric columns contain text like "$1,200.00" or "N/A"
- You want a reproducible cleaning pipeline (not one-off manual fixes)

## When NOT to Use
- Designing a data warehouse or ETL orchestration system (use dbt, Airflow)
- Cleaning data in a SQL database directly (use sql-analyst skill)
- Feature engineering for machine learning (use an ML preprocessing skill)
- Processing real-time streaming data

## Quick Reference
| Issue | Detection | Fix Strategy |
|-------|-----------|--------------|
| Missing values | `df.isnull().sum()` | Drop, fill with mean/median/mode, or flag |
| Duplicate rows | `df.duplicated().sum()` | `df.drop_duplicates()` |
| Wrong data types | `df.dtypes` | `df.astype()`, `pd.to_datetime()`, `pd.to_numeric()` |
| Outliers | IQR / Z-score | Cap (winsorize), remove, or flag |
| Inconsistent strings | `df['col'].value_counts()` | `.str.strip().str.lower()`, `.replace()` map |
| Date format mix | `pd.to_datetime(errors='coerce')` | Normalize to ISO 8601 |
| Currency strings | `df['col'].str.replace('[\\$,]','',regex=True)` | Cast to float |
| Invalid values | Range checks, business rules | Replace with NaN, then handle as missing |
| Whitespace | `df.columns.str.strip()` | Strip and rename columns |
| Mixed case categories | `.str.title()` or `.str.upper()` | Standardize to one case |

## Instructions

### Step 1: Audit the Dataset First
Always understand what you have before changing anything.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("raw_data.csv")

# Overview
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# Missing value report
missing = df.isnull().sum()
missing_pct = (df.isnull().mean() * 100).round(1)
missing_report = pd.DataFrame({'count': missing, 'pct': missing_pct})
print("\nMissing values:\n", missing_report[missing_report['count'] > 0])

# Duplicate check
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Unique values in categoricals
for col in df.select_dtypes(include='object').columns:
    n_unique = df[col].nunique()
    print(f"{col}: {n_unique} unique values — {df[col].unique()[:5]}")
```

### Step 2: Handle Missing Values
Choose the right strategy based on missingness type and business context.

```python
# Strategy 1: Drop rows with too many missing values (>50% missing)
threshold = 0.5
df = df.dropna(thresh=int(threshold * len(df.columns)))

# Strategy 2: Drop columns with very high missingness
df = df.drop(columns=df.columns[df.isnull().mean() > 0.8])

# Strategy 3: Fill numerical with median (robust to outliers)
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Strategy 4: Fill categorical with mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Strategy 5: Fill with a sentinel value (flag the missingness)
df['revenue_missing'] = df['revenue'].isnull().astype(int)
df['revenue'] = df['revenue'].fillna(0)

# Strategy 6: Forward-fill for time-series data
df = df.sort_values('date')
df['price'] = df['price'].ffill()
```

**Decision guide:**
- < 5% missing → fill with median/mode or drop rows
- 5–30% missing → fill with median/mode + add a `_missing` flag column
- > 30% missing → consider dropping the column; or use advanced imputation
- Structured missingness (e.g., only weekends) → investigate, then forward-fill

### Step 3: Remove and Handle Duplicates
```python
# Find duplicates
dupes = df[df.duplicated(keep=False)]
print(f"Duplicate rows: {len(dupes)}")
print(dupes.head(10))

# Remove all exact duplicates (keep first occurrence)
df = df.drop_duplicates()

# Deduplicate on key columns only (keep most recent)
df = df.sort_values('updated_at', ascending=False)
df = df.drop_duplicates(subset=['customer_id', 'product_id'], keep='first')

print(f"Rows after dedup: {df.shape[0]}")
```

### Step 4: Fix Data Types
```python
# Convert numeric columns that were read as strings
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['quantity'] = df['quantity'].astype(int)

# Parse dates — handle mixed formats
df['order_date'] = pd.to_datetime(df['order_date'], infer_datetime_format=True, errors='coerce')

# Boolean columns
df['is_active'] = df['is_active'].map({'Yes': True, 'No': False, '1': True, '0': False})

# Categorical (saves memory for low-cardinality string columns)
df['region'] = df['region'].astype('category')

# Check how many dates failed to parse
print("Unparseable dates:", df['order_date'].isnull().sum())
```

### Step 5: Standardize String/Format Inconsistencies
```python
# Basic normalization: strip whitespace, lowercase
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.lower()

# Fix specific column
df['country'] = df['country'].str.strip()

# Standardize country variations
country_map = {
    'usa': 'United States',
    'u.s.a.': 'United States',
    'united states of america': 'United States',
    'uk': 'United Kingdom',
    'great britain': 'United Kingdom',
}
df['country'] = df['country'].str.lower().map(country_map).fillna(df['country'].str.title())

# Clean currency strings: "$1,200.50" → 1200.50
df['price'] = (df['price']
    .astype(str)
    .str.replace(r'[\$,€£]', '', regex=True)
    .str.strip()
    .pipe(pd.to_numeric, errors='coerce')
)

# Standardize phone numbers
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)  # digits only

# Normalize email
df['email'] = df['email'].str.lower().str.strip()
```

### Step 6: Handle Outliers
```python
# IQR-based capping (winsorization) — preserves row, limits extreme values
def cap_outliers_iqr(series, factor=1.5):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR
    return series.clip(lower=lower, upper=upper)

df['revenue'] = cap_outliers_iqr(df['revenue'])

# Flag outliers without removing them
from scipy import stats
df['revenue_zscore'] = stats.zscore(df['revenue'].fillna(df['revenue'].median()))
df['is_outlier'] = (df['revenue_zscore'].abs() > 3).astype(int)

# Remove outliers (use only when business-justified)
df_clean = df[df['revenue_zscore'].abs() <= 3].copy()
```

### Step 7: Validate the Cleaned Data
```python
def validate_dataset(df):
    issues = []

    # No remaining nulls in required columns
    required = ['customer_id', 'order_date', 'revenue']
    for col in required:
        nulls = df[col].isnull().sum()
        if nulls > 0:
            issues.append(f"FAIL: {col} has {nulls} nulls")

    # Revenue is non-negative
    if (df['revenue'] < 0).any():
        issues.append(f"FAIL: revenue has {(df['revenue']<0).sum()} negative values")

    # Dates are in valid range
    if not df['order_date'].between('2020-01-01', '2025-12-31').all():
        issues.append("FAIL: order_date has values outside expected range")

    # No duplicates on key
    dupes = df.duplicated(subset=['order_id']).sum()
    if dupes > 0:
        issues.append(f"FAIL: {dupes} duplicate order_ids")

    if issues:
        for issue in issues:
            print(issue)
    else:
        print("All validation checks passed ✓")

validate_dataset(df)
```

## Examples

### Example 1: Clean a CSV with Missing Values
**Input:** Sales CSV where `revenue` has 15% nulls, `region` has mixed case ("West", "west", "WEST"), `order_date` has formats like "2023-01-15" and "Jan 15 2023".

```python
import pandas as pd
import numpy as np

df = pd.read_csv("sales_raw.csv")
print(f"Before: {df.shape[0]} rows, {df.isnull().sum().sum()} nulls")

# Fix region inconsistency
df['region'] = df['region'].str.strip().str.title()

# Fix dates
df['order_date'] = pd.to_datetime(df['order_date'], infer_datetime_format=True, errors='coerce')
bad_dates = df['order_date'].isnull().sum()
if bad_dates > 0:
    print(f"Warning: {bad_dates} dates could not be parsed — review these rows")

# Handle missing revenue: flag and fill with median
df['revenue_missing'] = df['revenue'].isnull().astype(int)
df['revenue'] = df['revenue'].fillna(df['revenue'].median())

# Remove full duplicates
df = df.drop_duplicates()

print(f"After: {df.shape[0]} rows, {df.isnull().sum().sum()} nulls")
df.to_csv("sales_clean.csv", index=False)
```

**Output:**
```
Before: 5,240 rows, 786 nulls
Warning: 12 dates could not be parsed — review these rows
After: 5,214 rows, 12 nulls (unparseable dates only)
```
The dataset is now ready for analysis with a `revenue_missing` flag for downstream filtering.

---

### Example 2: Standardize Date Formats
**Input:** Column with 5 different date formats: `"2023-01-15"`, `"Jan 15, 2023"`, `"15/01/2023"`, `"20230115"`, `"01-15-2023"`

```python
raw_dates = pd.Series([
    "2023-01-15",
    "Jan 15, 2023",
    "15/01/2023",
    "20230115",
    "01-15-2023"
])

# pandas infer_datetime_format handles most common formats
parsed = pd.to_datetime(raw_dates, infer_datetime_format=True, errors='coerce')

# For the tricky ones, try dayfirst=True fallback
mask = parsed.isnull()
if mask.any():
    parsed[mask] = pd.to_datetime(raw_dates[mask], dayfirst=True, errors='coerce')

# Standardize to ISO 8601
standardized = parsed.dt.strftime('%Y-%m-%d')
print(standardized)
```

**Output:**
```
0    2023-01-15
1    2023-01-15
2    2023-01-15
3    2023-01-15
4    2023-01-15
dtype: object
```
All five formats normalized to `YYYY-MM-DD`.

## Best Practices
- Always work on a copy: `df_clean = df.copy()` before any mutations
- Document every cleaning decision with a comment explaining the business rationale
- Run a before/after row count and null count to confirm changes had expected effect
- Separate the cleaning script from the analysis script—cleaning is a distinct step
- Use `errors='coerce'` when casting types; it creates NaN instead of crashing
- Keep the original raw file untouched; write cleaned output to a new file
- Add validation assertions at the end of the pipeline to catch regressions

## Common Mistakes
- Dropping rows with missing values without checking if they're systematically biased
- Filling missing numerical values with mean when data is skewed (use median instead)
- Deduplicating without specifying which duplicate to keep (temporal or priority logic)
- Stripping time zones from datetime columns without converting to a consistent zone first
- Normalizing strings to lowercase before mapping to display values (map, then format)
- Using `inplace=True` — it's being deprecated in pandas and can cause hidden bugs
- Not re-checking for new nulls introduced by type conversion failures

## Tips & Tricks
- `df.info()` shows non-null counts and dtypes at a glance—always run it first
- `df.select_dtypes(include='object').apply(pd.Series.nunique)` finds all string columns with their cardinality in one shot
- `pd.to_datetime(col, unit='s')` for Unix timestamp columns
- Use `df.pipe()` to chain cleaning steps into a readable pipeline
- `df['col'].str.contains(r'^\d{4}-\d{2}-\d{2}$')` to find rows matching ISO date format
- `df.memory_usage(deep=True).sum() / 1e6` to check memory before/after optimization

## Related Skills
- [data-analyst](../../data/data-analyst/SKILL.md)
- [sql-analyst](../../data/sql-analyst/SKILL.md)
- [excel-expert](../../data/excel-expert/SKILL.md)
