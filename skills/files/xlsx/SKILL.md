---
name: xlsx
description: "Use this skill when designing Excel or Google Sheets workbooks with formulas, named ranges, pivot tables, charts, and data validation, or when creating financial models, trackers, and dashboards in spreadsheet format. Not for database design or SQL queries. Not for generating CSV files without workbook structure."
version: 1.0.0
author: community
tags: [files, excel, spreadsheet, xlsx, formulas]
license: MIT
---

# XLSX

## Overview
This skill covers the design and implementation of Excel-compatible workbooks (.xlsx) and Google Sheets for professional use. It addresses workbook architecture (sheet organization, tab naming, data vs. calculation vs. presentation layers), formula design (lookup formulas, array formulas, dynamic arrays), named ranges for readable and maintainable formulas, pivot tables for summarization, charts for visualization, data validation for input integrity, and conditional formatting for visual cues. Outputs are either complete spreadsheet designs with formula specifications or Python code using `openpyxl` or `xlsxwriter` for programmatic workbook generation.

## When to Use
- Designing a financial model (budget, forecast, P&L, cash flow) in spreadsheet format
- Building a data tracker with validation, dropdowns, and summary dashboards
- Creating a reporting workbook that automatically calculates KPIs from raw data input
- Designing a pivot table structure for multi-dimensional data summarization
- Specifying formulas and structure for a workbook someone else will build in Excel
- Generating Excel workbooks programmatically from application data using Python
- Auditing or improving an existing spreadsheet's formula logic and structure

## When NOT to Use
- Replacing a proper relational database for data with more than ~100,000 rows
- Building real-time dashboards that require live database connectivity (use BI tools like Tableau or Power BI)
- Designing data pipelines or ETL processes (use data engineering tools)
- Creating presentations (use pptx skill)
- Generating PDF reports (use pdf or docx skills)

## Quick Reference
| Task | Approach |
|------|----------|
| Look up a value from a table | `XLOOKUP(lookup_value, lookup_range, return_range)` or `INDEX/MATCH` |
| Sum with conditions | `SUMIFS(sum_range, criteria_range1, criteria1, ...)` |
| Count with conditions | `COUNTIFS(range1, criteria1, range2, criteria2, ...)` |
| Dynamic subtotals | `SUBTOTAL(9, range)` — respects filters; `9` = SUM |
| Protect formula cells | Lock formula cells; protect sheet; leave input cells unlocked |
| Create a dropdown list | Data Validation → List → specify source range or comma-separated values |
| Name a range | Formulas → Name Manager → New; use in formulas as `=SUM(Revenue)` |
| Pivot table refresh | Right-click pivot → Refresh; or VBA `ThisWorkbook.RefreshAll` |

## Instructions

1. **Design the workbook architecture** — Separate concerns across sheets:
   - **`README` / `Instructions` sheet**: Document the workbook purpose, how to use it, input cells, and assumptions.
   - **`Inputs` / `Assumptions` sheet**: All user-modifiable inputs in one place. Color-code input cells (e.g., blue font or yellow fill).
   - **`Data` / `Raw Data` sheet(s)**: Source data that feeds calculations. Formatted as structured Tables (Ctrl+T).
   - **`Calculations` / `Model` sheet(s)**: Formulas and intermediate calculations. No hard-coded values — all reference the Inputs sheet.
   - **`Dashboard` / `Summary` sheet**: Charts, KPIs, and formatted output for stakeholders. No formulas — only links to calculation sheets.

2. **Define named ranges** — Name every important range or cell: input assumptions (e.g., `Discount_Rate`, `Headcount_2025`), summary outputs, and frequently-referenced lookup tables. Named ranges make formulas readable: `=Revenue * Gross_Margin_Rate` is clearer than `=B12 * Assumptions!C5`.

3. **Build lookup structures** — Use structured Tables (`Ctrl+T`) for all data ranges. Table references (`Table1[Column]`) update automatically when rows are added, unlike fixed ranges. For lookups, prefer `XLOOKUP` over `VLOOKUP` — it supports left-lookups, exact/approximate match, and a default-if-not-found value.

4. **Design the formula layer** — Write formulas that are: (a) readable — use named ranges and intermediate cells rather than nesting 5 functions deep; (b) auditable — one calculation step per cell; (c) consistent — the same formula across a row or column, not one-off adjustments; (d) error-handled — wrap in `IFERROR` or `IFNA` where appropriate.

5. **Add data validation** — Apply data validation to all input cells to prevent invalid entries:
   - Numeric inputs: whole number or decimal with min/max bounds
   - Category inputs: dropdown list from a named range or fixed list
   - Date inputs: date validation with reasonable min/max
   - Text inputs: text length validation where appropriate
   Add an input message (tooltip) and an error alert message for each validation.

6. **Build pivot tables for summarization** — Place the source data in a structured Table. Insert pivot tables on a separate sheet. Design the pivot layout: rows (grouping dimensions), columns (time or category), values (sum/count/average), and filters (slicers for interactive filtering). Add a slicer for the most important filter dimension.

7. **Design charts** — For each chart: specify the chart type and why (column for comparison, line for trends, combo for dual-axis), identify the data series, write the chart title as an insight statement (not a description), add data labels on the key series, remove chart junk (gridlines unless needed, legend if only one series, border). Keep the color palette consistent with the workbook theme.

8. **Apply conditional formatting** — Use sparingly for maximum impact: traffic light colors (red/yellow/green) for KPI status, data bars for magnitude visualization in tables, color scales for heatmaps, and icon sets for directional indicators. Always define the rules explicitly so they are reproducible.

9. **Protect the workbook** — Lock all formula cells (Format Cells → Protection → Locked). Leave input cells unlocked. Protect the sheet (Review → Protect Sheet) with a password if needed. Consider also hiding rows/columns used for intermediate calculations that users shouldn't modify.

10. **Document assumptions and version** — Add a `README` sheet with: workbook purpose, owner, last updated date, version number, list of input cells and their descriptions, list of outputs and how to interpret them, and known limitations. Add a version history table at the bottom of the README.

## Examples

### Example 1: Monthly Expense Tracker Workbook
**Input:** A small team needs a personal/team monthly expense tracker with categories, budget vs. actual comparison, and a summary dashboard.

**Output:**

**Workbook structure:**
```
Sheet 1: README
  - Purpose, how to use, input cells highlighted
  - Version: 1.0 | Owner: Finance Team | Updated: 2025-01

Sheet 2: Budgets (Inputs)
  Named ranges: Budget_Jan, Budget_Feb, ... Budget_Dec (or annual budget split by month)
  Table structure:
    | Category | Annual Budget | Jan Budget | Feb Budget | ... | Dec Budget |
    | Salaries | $120,000      | $10,000    | $10,000    | ... | $10,000    |
    | Software  | $24,000      | $2,000     | $2,000     | ... | $2,000     |
    | Travel    | $12,000      | $0         | $500       | ... | $2,000     |
  Input validation: Numeric, min $0
  Note: Only the Budgets sheet should be editable by most users

Sheet 3: Transactions (Data)
  Formatted as Excel Table "Transactions"
  Columns: Date | Description | Category | Amount | Approved By | Notes
  Category column: Dropdown validation from Budget category list
  Amount: Positive number validation; no negatives (use separate refund row)

Sheet 4: Monthly Summary (Calculations)
  SUMIFS formula for actuals by category by month:
    =SUMIFS(Transactions[Amount], Transactions[Category], [@Category],
            Transactions[Date], ">="&DATE(Year, Month, 1),
            Transactions[Date], "<"&DATE(Year, Month+1, 1))
  
  Variance formula: =Budget_Amount - Actual_Amount
  Variance %: =IF(Budget_Amount=0, "N/A", Variance/Budget_Amount)
  Status: =IF(Variance_Pct < -0.1, "Over Budget", IF(Variance_Pct < 0, "Watch", "On Track"))
  Conditional formatting: Status cell — red/yellow/green based on text value

Sheet 5: Dashboard
  KPI Cards (top row):
    Total Budget YTD | Actual Spend YTD | Remaining Budget | % Budget Used
  
  Chart 1: Stacked bar chart — Budget vs Actual by Category (current month)
  Chart 2: Line chart — Cumulative spend vs cumulative budget over the year
  Chart 3: Donut chart — Spend by category as % of total
  Slicer: Month selector (updates all charts)
```

**Key formulas:**
```excel
-- Actual spend for a category in a specific month --
=SUMIFS(
    Transactions[Amount],
    Transactions[Category], B5,
    Transactions[Date], ">="&DATE($B$2, $C$2, 1),
    Transactions[Date], "<"&EOMONTH(DATE($B$2, $C$2, 1), 0)+1
)

-- Budget utilization status (with color via conditional formatting) --
=IF(D5/C5 > 1, "OVER", IF(D5/C5 > 0.9, "WATCH", "OK"))

-- Year-to-date actual spend (all months through current) --
=SUMIFS(
    Transactions[Amount],
    Transactions[Date], ">="&DATE(YEAR(TODAY()), 1, 1),
    Transactions[Date], "<="&TODAY()
)
```

### Example 2: Sales Pipeline Spreadsheet with Dashboard
**Input:** A sales team needs a pipeline tracker that shows deals by stage, weighted pipeline value, forecast by month, and rep performance.

**Output:**

**Workbook structure and formulas:**
```
Sheet 1: Deals (Data — Excel Table "Pipeline")
  Columns and validation:
    Deal ID        | Auto-increment (=MAX(Pipeline[Deal_ID])+1 for new row)
    Company        | Text, required
    Deal Owner     | Dropdown: named range "SalesReps" from Config sheet
    Stage          | Dropdown: Prospect / Qualified / Proposal / Negotiation / Closed Won / Closed Lost
    Deal Value ($) | Number, min $0
    Close Date     | Date, must be >= TODAY()
    Probability (%)| Auto-fill from Stage using XLOOKUP:
                     =XLOOKUP([@Stage], Config!A:A, Config!B:B, "")
    Weighted Value  | =[@[Deal Value]]*[@[Probability]]
    Days in Stage   | =TODAY()-[@[Stage Entry Date]]
    Notes          | Text

Sheet 2: Config (Inputs — locked except admin)
  Stage Probabilities:
    | Stage        | Probability | Target Days in Stage |
    | Prospect     | 10%         | 14                   |
    | Qualified    | 25%         | 21                   |
    | Proposal     | 50%         | 14                   |
    | Negotiation  | 75%         | 10                   |
    | Closed Won   | 100%        | —                    |
    | Closed Lost  | 0%          | —                    |
  Named range: SalesReps (list of rep names)
  Named range: Stages (list of stage names for validation)

Sheet 3: Forecast (Calculations)
  Monthly forecast by rep:
    =SUMPRODUCT(
        (Pipeline[Deal_Owner]=A3) *
        (MONTH(Pipeline[Close_Date])=B2) *
        (YEAR(Pipeline[Close_Date])=YEAR(TODAY())) *
        Pipeline[Weighted_Value]
    )
  
  Stage funnel (count by stage):
    =COUNTIFS(Pipeline[Stage], "Qualified", Pipeline[Deal_Owner], $A3)

Sheet 4: Rep Scorecards (Calculations)
  Per-rep metrics:
    | Rep Name | Open Pipeline | Wtd Pipeline | Deals Won MTD | Win Rate | Avg Deal Size |
  
  Win Rate: =COUNTIFS(Pipeline[Deal_Owner], A3, Pipeline[Stage], "Closed Won") /
              MAX(1, COUNTIFS(Pipeline[Deal_Owner], A3, Pipeline[Stage], "Closed Won") +
                     COUNTIFS(Pipeline[Deal_Owner], A3, Pipeline[Stage], "Closed Lost"))

Sheet 5: Dashboard
  Slicers: Month, Deal Owner, Stage
  
  Chart 1: Funnel chart — deals count and value by stage
  Chart 2: Bar chart — weighted pipeline by rep (sorted descending)
  Chart 3: Line chart — monthly forecast vs. monthly quota
  Chart 4: Horizontal bar — days in stage by deal (aging heatmap — highlight if > target)
  
  KPI Cards:
    Total Open Pipeline: =SUMIFS(Pipeline[Deal Value], Pipeline[Stage], "<>Closed Won", Pipeline[Stage], "<>Closed Lost")
    Weighted Pipeline: =SUMIFS(Pipeline[Weighted Value], ...)
    Deals Closing This Month: =COUNTIFS(...)
    Forecast vs. Quota: =[Forecast MTD] / [Quota MTD]
```

**Conditional formatting rules:**
```
Days in Stage column:
  Green: <= target days for stage
  Yellow: target days < days <= 2× target
  Red: > 2× target days (deal is stalled)

Win Rate cell:
  Green: >= 30%
  Yellow: 20–30%
  Red: < 20%
```

## Best Practices
- Never hard-code values in formula cells — all constants belong in named cells on the Inputs sheet
- Use Excel Tables (Ctrl+T) for all data ranges — they auto-expand and work with structured references
- Color-code consistently: blue/yellow = user input, white = calculated, gray = locked/reference
- Keep one concept per column — never store two data points in one cell (e.g., "100 units - estimate")
- Test formulas at boundary conditions: empty cells, zero values, negative values, future dates
- Document complex formulas with a comment in the adjacent cell explaining what it calculates
- Use `IFERROR` to handle divide-by-zero and missing lookups gracefully rather than showing `#N/A`

## Common Mistakes
- Using `VLOOKUP` with a fixed column index — it breaks if columns are inserted; use `XLOOKUP` or `INDEX/MATCH`
- Circular references — often caused by accidentally referencing a cell in its own formula; use iterative calc only when intentional
- Mixing data and formatting in the same cells (e.g., writing "$1,200 est." — store 1200 and format the cell)
- Not protecting formula cells — users accidentally overwrite calculated cells with typed values
- Using merged cells in data tables — they break sorting, filtering, and SUMIFS functions
- Forgetting to refresh pivot tables after updating source data — add a refresh button with a simple macro
- Building massive all-in-one sheets instead of separating inputs, calculations, and outputs into layers

## Tips & Tricks
- Press `Ctrl+~` to toggle between formula view and value view — great for auditing
- Use `Ctrl+[` to jump to a formula's precedent cells — follow the formula chain
- `LAMBDA` function lets you define reusable custom functions in Excel without VBA
- `LET` function stores intermediate calculations in named variables within a single formula
- For programmatic generation, `openpyxl` handles formulas and styles; `xlsxwriter` is faster for large datasets
- Use `Power Query` (Get & Transform) to pull and transform data from external sources without VBA
- Name your Excel Tables descriptively (`Pipeline`, `Budgets`, not `Table1`, `Table2`) — structured references become self-documenting

## Related Skills
- [docx](../docx/SKILL.md)
- [pdf](../pdf/SKILL.md)
