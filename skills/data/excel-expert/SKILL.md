---
name: excel-expert
description: "Use this skill when working with Excel or Google Sheets formulas, pivot tables, data validation, conditional formatting, or building spreadsheet-based tools. Trigger phrases: 'Excel formula for', 'how do I VLOOKUP', 'build a pivot table', 'conditional formatting rule', 'create a dashboard in Excel'. Not for writing VBA macros, building Python/SQL alternatives to Excel, or migrating data out of spreadsheets."
version: 1.0.0
author: community
tags: [data, excel, spreadsheet, formulas]
license: MIT
---

# Excel Expert

## Overview
This skill covers the full spectrum of professional Excel use—from essential lookup and aggregation formulas through pivot tables, data validation, and conditional formatting to dynamic dashboard construction. It provides ready-to-use formula patterns, step-by-step instructions for advanced features, and a comprehensive quick-reference formula library so you can solve real business spreadsheet problems fast.

## When to Use
- You need a specific Excel formula and aren't sure of the syntax
- A VLOOKUP or INDEX/MATCH is returning an error
- You want to build a pivot table or dynamic summary
- You need to apply conditional formatting rules across a dataset
- You're building a dashboard, budget model, or tracking sheet in Excel
- You want to validate data entry (dropdowns, date ranges, numeric constraints)

## When NOT to Use
- Writing Excel VBA/macro code (use a VBA skill)
- Migrating an Excel model to Python, SQL, or another tool
- Designing a production database (Excel is not a database)
- Analyzing datasets with more than ~500,000 rows (use pandas or SQL)

## Quick Reference
| Formula | Syntax | Use Case |
|---------|--------|----------|
| VLOOKUP | `=VLOOKUP(lookup, table, col_index, 0)` | Look up a value in a table (left-to-right only) |
| XLOOKUP | `=XLOOKUP(lookup, lookup_range, return_range, "Not found")` | Modern replacement for VLOOKUP; any direction |
| INDEX/MATCH | `=INDEX(return_col, MATCH(lookup, lookup_col, 0))` | Flexible lookup; left-to-right or right-to-left |
| SUMIF | `=SUMIF(range, criteria, sum_range)` | Sum values meeting one condition |
| SUMIFS | `=SUMIFS(sum_range, range1, crit1, range2, crit2)` | Sum values meeting multiple conditions |
| COUNTIF | `=COUNTIF(range, criteria)` | Count cells meeting one condition |
| COUNTIFS | `=COUNTIFS(range1, crit1, range2, crit2)` | Count cells meeting multiple conditions |
| IF | `=IF(condition, value_if_true, value_if_false)` | Conditional logic |
| IFS | `=IFS(cond1, val1, cond2, val2, TRUE, default)` | Multiple conditions (Excel 2019+) |
| IFERROR | `=IFERROR(formula, "Error text")` | Catch and handle formula errors |
| AVERAGEIF | `=AVERAGEIF(range, criteria, avg_range)` | Average values meeting a condition |
| MAXIFS | `=MAXIFS(max_range, criteria_range, criteria)` | Max value meeting a condition (Excel 2019+) |
| TEXT | `=TEXT(value, "format_code")` | Format a number/date as a string |
| LEFT/MID/RIGHT | `=LEFT(text, n)` | Extract characters from a string |
| CONCATENATE / & | `=A1&" "&B1` | Join text values |
| LEN | `=LEN(text)` | Count characters in a string |
| TRIM | `=TRIM(text)` | Remove leading/trailing/extra spaces |
| UNIQUE | `=UNIQUE(range)` | Distinct values (Excel 365/2021) |
| FILTER | `=FILTER(array, condition, "No results")` | Filter a range dynamically (Excel 365) |
| SORT | `=SORT(range, sort_index, -1)` | Sort a range dynamically (Excel 365) |

## Instructions

### Step 1: Lookup Formulas — VLOOKUP vs XLOOKUP vs INDEX/MATCH

**VLOOKUP** — simple but limited (lookup column must be leftmost):
```
=VLOOKUP(E2, $A$2:$C$100, 3, 0)
```
- `E2` = what to look up
- `$A$2:$C$100` = table range (lock with $ for copying)
- `3` = return the 3rd column of the table
- `0` = exact match (always use 0 for exact match)

**XLOOKUP** — modern, flexible (Excel 365/2021):
```
=XLOOKUP(E2, A:A, C:C, "Not found", 0)
```
- Can look left or right
- Built-in "not found" default value
- No column index needed

**INDEX/MATCH** — most flexible, works in all Excel versions:
```
=INDEX(C:C, MATCH(E2, A:A, 0))
```
- `INDEX(C:C, ...)` = return from column C
- `MATCH(E2, A:A, 0)` = find the row position of E2 in column A
- Wrap with IFERROR: `=IFERROR(INDEX(C:C, MATCH(E2, A:A, 0)), "Not found")`

**Two-way lookup** (row and column):
```
=INDEX($B$2:$F$10, MATCH($A14, $A$2:$A$10, 0), MATCH(B$13, $B$1:$F$1, 0))
```

### Step 2: Conditional Aggregation (SUMIFS, COUNTIFS, AVERAGEIF)

**SUMIFS** — total sales for "West" region in "Q3":
```
=SUMIFS(D:D, B:B, "West", C:C, "Q3")
```

**SUMIFS with date range** — sales in January 2024:
```
=SUMIFS(D:D, A:A, ">="&DATE(2024,1,1), A:A, "<="&DATE(2024,1,31))
```

**COUNTIFS** — count orders over $1,000 from new customers:
```
=COUNTIFS(E:E, "New", D:D, ">1000")
```

**Running total** (cumulative sum):
```
=SUM($D$2:D2)
```
(The first `$D$2` is anchored; copy down the column to get a running total.)

### Step 3: Nested IF and IFS

**Nested IF** — grade banding:
```
=IF(B2>=90,"A", IF(B2>=80,"B", IF(B2>=70,"C", IF(B2>=60,"D","F"))))
```

**IFS** (cleaner, Excel 2019+):
```
=IFS(B2>=90,"A", B2>=80,"B", B2>=70,"C", B2>=60,"D", TRUE,"F")
```

**Combining with IFERROR**:
```
=IFERROR(VLOOKUP(A2, Products!$A:$C, 3, 0), "Product not found")
```

### Step 4: Pivot Tables (Step-by-Step)
1. Click anywhere in your data range
2. **Insert → PivotTable** → choose "New Worksheet"
3. Drag fields:
   - **Rows**: dimension to group by (e.g., Region, Product)
   - **Columns**: secondary dimension (e.g., Quarter)
   - **Values**: metric to aggregate (e.g., Revenue → Sum)
   - **Filters**: optional slicer (e.g., Year)
4. Right-click a value field → **Value Field Settings** → choose Sum/Count/Average/Max
5. Right-click a date field → **Group** → select Month/Quarter/Year
6. Add a Slicer: **PivotTable Analyze → Insert Slicer** for interactive filtering

**Refresh data**: Right-click pivot → Refresh (or Ctrl+Alt+F5 for all pivots)

**GETPIVOTDATA formula** to pull a specific cell:
```
=GETPIVOTDATA("Revenue", $A$3, "Region", "West", "Quarter", "Q3")
```

### Step 5: Conditional Formatting
1. Select the data range (e.g., D2:D100)
2. **Home → Conditional Formatting**

**Heat map (color scale):**
- Conditional Formatting → Color Scales → choose 3-color scale
- Min = red, Mid = yellow, Max = green

**Highlight above-average values:**
- Conditional Formatting → Top/Bottom Rules → Above Average

**Custom formula rule** (highlight entire row if status = "Late"):
- Conditional Formatting → New Rule → "Use a formula"
- Formula: `=$E2="Late"` ($ locks the column, not the row)
- Apply to: `$A$2:$F$100`

**Data bars** (mini bar chart inside cells):
- Conditional Formatting → Data Bars → choose a style

### Step 6: Data Validation
1. Select the target cell(s)
2. **Data → Data Validation**

**Dropdown list:**
- Allow: List
- Source: `West,East,North,South` (comma-separated) or a named range `=RegionList`

**Date range:**
- Allow: Date
- Data: between
- Start: `=TODAY()-365`, End: `=TODAY()`

**Whole number with error message:**
- Allow: Whole number, Between 1 and 100
- Error Alert tab → set Title and Message

**Custom formula validation** (email format check):
- Allow: Custom
- Formula: `=ISNUMBER(FIND("@",A2))`

### Step 7: Build a Dynamic Dashboard
1. Create a **Data** sheet with raw data
2. Create a **Summary** sheet with SUMIFS/COUNTIFS formulas referencing Data
3. Use **Form Controls** (Developer → Insert → Combo Box) linked to a cell for filter selection
4. Reference the linked cell in formulas: `=SUMIFS(Data!D:D, Data!B:B, $G$1)` where G1 = selected region
5. Build charts from Summary data; they update automatically as G1 changes
6. Add **slicers** connected to pivot tables for click-to-filter interactivity

## Examples

### Example 1: Build a Dynamic Sales Dashboard
**Input:** Raw sales data sheet with columns: `Date | Region | Product | Revenue | Units`

**Dashboard formulas in Summary sheet:**
```
# G1 = selected region (from dropdown)

Total Revenue (selected region):
=SUMIF(Data!B:B, G1, Data!D:D)

Total Revenue (all regions):
=SUM(Data!D:D)

Region Share %:
=SUMIF(Data!B:B, G1, Data!D:D) / SUM(Data!D:D)

Month-over-Month revenue (current month):
=SUMIFS(Data!D:D, Data!B:B, G1, Data!A:A, ">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))

Top Product in Region:
=INDEX(Data!C:C, MATCH(MAXIFS(Data!D:D, Data!B:B, G1), Data!D:D, 0))
```

**Steps:**
1. Insert Combo Box (Developer → Insert → Combo Box), link to cell G1
2. Fill source range with region list
3. Wire formulas above to G1
4. Insert line chart and bar chart referencing summary rows
5. Format numbers: select cells → Ctrl+1 → Number → Currency

**Output:** Dashboard that updates all metrics and charts when user selects a region from the dropdown.

---

### Example 2: Fix a Broken VLOOKUP
**Input:** `=VLOOKUP(A2, B:D, 2, 0)` returning `#N/A` for values that exist in the table.

**Diagnosis checklist:**
1. **Trailing spaces**: `=VLOOKUP(TRIM(A2), B:D, 2, 0)` — fixes hidden whitespace
2. **Number vs text mismatch**: A2 is text "1234" but column B has number 1234
   - Fix: `=VLOOKUP(VALUE(A2), B:D, 2, 0)` or `=VLOOKUP(TEXT(A2,"0"), B:D, 2, 0)`
3. **Wrong match type**: last argument is `1` (approximate match) instead of `0`
   - Fix: always use `0` for exact match
4. **Table range not including the lookup column**: VLOOKUP needs lookup column as the LEFTMOST column
   - Fix: reorder table or switch to XLOOKUP/INDEX-MATCH
5. **After fixing**: wrap with IFERROR to handle remaining misses gracefully:
   ```
   =IFERROR(VLOOKUP(TRIM(A2), $B$1:$D$500, 2, 0), "Not found")
   ```

**Output:** Working lookup with a user-friendly "Not found" instead of #N/A.

## Best Practices
- Always lock table references with $ in lookups: `$A$2:$C$100` (breaks on copy otherwise)
- Use named ranges (Formulas → Name Manager) for tables referenced in many formulas
- Prefer XLOOKUP over VLOOKUP if your Excel version supports it (2021/365)
- Use IFERROR around every lookup formula to handle mismatches gracefully
- Keep raw data on a separate "Data" sheet; never mix calculations into raw data rows
- Format numbers as Currency/Percentage in cells, not in the formula text
- Freeze panes (View → Freeze Panes) on dashboards to keep headers visible

## Common Mistakes
- Using `1` (approximate match) instead of `0` (exact match) in VLOOKUP
- Forgetting to anchor the table range with $ when copying formulas down
- Circular references: a cell that refers to itself (check Formulas → Error Checking)
- Mixing text and numbers in the same column (causes SUMIF/VLOOKUP to miss rows)
- Deleting rows in source data without updating named ranges
- Using whole-column references (A:A) in very large files—can slow calculation
- Hard-coding dates instead of using `=TODAY()` or `=DATE(2024,1,1)` for flexibility

## Tips & Tricks
- `Ctrl+Shift+Enter` for array formulas (older Excel); Excel 365 handles arrays natively
- `Ctrl+T` converts a range to a Table—formulas auto-expand as you add rows
- Name your pivot table slicers to connect them to multiple pivots (right-click slicer → Report Connections)
- `=UNIQUE(A:A)` + `=SORT()` + `=FILTER()` are Excel 365's "spill" functions—they expand automatically
- Press `F4` to toggle absolute/relative references while editing a formula
- `Ctrl+`` ` (backtick) toggles between showing formulas and values in all cells
- Use `=INDIRECT("Sheet2!A"&ROW())` to dynamically reference cells across sheets

## Related Skills
- [data-analyst](../../data/data-analyst/SKILL.md)
- [data-cleaner](../../data/data-cleaner/SKILL.md)
- [dashboard-designer](../../data/dashboard-designer/SKILL.md)
