---
name: budget-planner
description: "Use this skill when you need to build, review, or refine personal or business budgets — triggered by phrases like 'help me budget', 'create a spending plan', 'where is my money going', or 'plan my finances'. Not for tax filing, investment portfolio management, or legal financial advice."
version: 1.0.0
author: community
tags: [finance, budgeting, personal-finance, planning]
license: MIT
---

# Budget Planner

## Overview
The Budget Planner skill helps individuals and businesses design structured, actionable budgets that align spending with priorities. It covers income tracking, expense categorization, variance analysis between projected and actual figures, and short- to medium-term forecasting. Whether you are a salaried employee trying to save for a house, a freelancer managing irregular income, or a small business owner planning a quarterly operating budget, this skill guides you through every step — from listing income sources to identifying savings opportunities and stress-testing spending scenarios.

## When to Use
- A user wants to create a monthly household or personal spending plan
- A user needs to track income from multiple sources (salary, freelance, rental, dividends)
- A small business owner needs to plan a quarterly or annual operating budget
- A user wants to analyze where overspending occurred and how to correct it
- A user asks for help allocating a fixed income across categories (rent, food, savings, entertainment)
- A user needs to build a zero-based budget or 50/30/20 budget structure
- A user wants a variance report comparing budgeted vs. actual spending

## When NOT to Use
- The user needs formal tax preparation or filing assistance
- The user is asking for regulated investment or portfolio management advice
- The task is purely accounting reconciliation requiring access to live bank feeds
- The user needs legal or compliance guidance on financial reporting standards (GAAP/IFRS)
- The user requires actuarial calculations or pension fund modeling

## Quick Reference
| Task | Approach |
|------|----------|
| Personal monthly budget | Collect net income, list fixed/variable expenses, apply 50/30/20 or zero-based method |
| Business quarterly budget | Break down revenue streams, COGS, OpEx, and compute gross/net margins |
| Variance analysis | Compare actual vs. budgeted line items; flag items >10% off target |
| Irregular income budgeting | Use lowest-month baseline income; treat surplus as savings buffer |
| Savings goal planning | Back-calculate required monthly savings from target amount and timeline |
| Category rebalancing | Identify over-budget categories and propose offsets in discretionary spend |

## Instructions

1. **Gather income information** — Ask the user for all income sources: gross salary, net take-home pay, freelance or side income, rental income, dividends, and any irregular bonuses. Clarify whether figures are monthly, bi-weekly, or annual and normalize everything to the same period.

2. **List all fixed expenses** — Capture non-negotiable, recurring costs: rent/mortgage, insurance premiums, loan repayments, subscriptions, and utilities with stable rates. Record amounts and due dates.

3. **List all variable expenses** — Identify spending categories that fluctuate: groceries, dining, transportation (fuel/transit), entertainment, clothing, healthcare copays, and personal care. Use recent bank statements to estimate averages where possible.

4. **Choose a budgeting framework** — Select the appropriate method based on user goals:
   - **50/30/20**: 50% needs, 30% wants, 20% savings/debt repayment
   - **Zero-based**: Every dollar is assigned a purpose; income minus expenses equals zero
   - **Envelope method**: Allocate cash caps per category
   - **Pay yourself first**: Savings are deducted before any discretionary spending

5. **Allocate funds across categories** — Distribute net income into the chosen categories. Ensure total allocated spending does not exceed net income. Flag any deficit immediately.

6. **Build the budget table** — Present results in a clear table with columns: Category, Monthly Budget, Actual (if known), Variance, and Notes. Group by fixed, variable, savings, and debt.

7. **Run variance analysis** — If the user provides actuals, compute the difference (Budgeted − Actual) and percentage deviation. Flag variances greater than 10% as needing attention. Identify root causes where possible.

8. **Forecast and stress-test** — Project the budget forward 3–12 months. Test scenarios such as income reduction of 20%, unexpected medical expense, or a major one-time purchase. Show how the budget absorbs or fails under each scenario.

9. **Identify savings opportunities** — Highlight discretionary line items that are high relative to income. Suggest specific, realistic reductions and quantify the annual impact of each change.

10. **Summarize and recommend next steps** — Provide a one-paragraph executive summary of financial position, key risk areas, and top 3 prioritized action items.

## Examples

### Example 1: Monthly Personal Budget (Salaried Employee)
**Input:**
"I take home $4,200/month after tax. My rent is $1,350, car payment $280, car insurance $110, phone $65, streaming services $45. I spend roughly $500 on groceries, $300 on dining out, $200 on gas, $150 on clothing, $100 on gym and personal care. I want to save for a $10,000 emergency fund in 12 months and also pay off a $3,000 credit card balance in 6 months."

**Output:**
```
MONTHLY BUDGET — Net Income: $4,200

FIXED EXPENSES
─────────────────────────────────────────
Rent/Mortgage         $1,350   (32.1%)
Car Payment             $280    (6.7%)
Car Insurance           $110    (2.6%)
Phone                    $65    (1.5%)
Streaming                $45    (1.1%)
Fixed Subtotal        $1,850   (44.0%)

VARIABLE EXPENSES
─────────────────────────────────────────
Groceries               $500   (11.9%)
Dining Out              $300    (7.1%)
Gas/Transportation      $200    (4.8%)
Clothing                $150    (3.6%)
Gym & Personal Care     $100    (2.4%)
Variable Subtotal     $1,250   (29.8%)

SAVINGS & DEBT
─────────────────────────────────────────
Emergency Fund          $833   (target: $10,000 ÷ 12)
Credit Card Payoff      $500   (target: $3,000 ÷ 6)
Savings Subtotal      $1,333   (31.7%)

REMAINING BUFFER       -$233   ⚠ DEFICIT

ANALYSIS:
Your goals exceed current cash flow by $233/month. Recommended adjustments:
• Reduce dining out from $300 → $150 (-$150)
• Reduce clothing from $150 → $70 (-$80)
• Pause one streaming service (-$15)
Adjusted Buffer: +$12/month ✓

GOAL TIMELINE:
• Emergency Fund: $833/mo → $10,000 by month 12 ✓
• Credit Card: $500/mo → $3,000 paid off by month 6 ✓

STRESS TEST — Income drops 15% ($630):
Immediate cuts needed: suspend emergency fund savings temporarily,
apply full surplus to credit card (priority), resume emergency fund
after month 6 payoff.
```

### Example 2: Small Business Quarterly Budget (Freelance Design Studio)
**Input:**
"I run a small design studio with 2 contractors. Q1 projected revenue: $85,000 from 3 retainer clients ($20k, $25k, $30k) plus ~$10k in one-off projects. Costs: contractor payments ~$28,000, software/tools $1,200, co-working space $900, marketing $2,000, professional services (accountant, lawyer) $3,500, travel/client entertainment $1,800, miscellaneous $600. I want to set aside 25% of profit for taxes and invest 10% back into the business."

**Output:**
```
Q1 BUDGET — Freelance Design Studio

REVENUE
─────────────────────────────────────────
Retainer Client A        $20,000
Retainer Client B        $25,000
Retainer Client C        $30,000
One-off Projects         $10,000
Total Revenue            $85,000

COST OF GOODS SOLD (COGS)
─────────────────────────────────────────
Contractor Payments      $28,000
COGS Total               $28,000
Gross Profit             $57,000  (Gross Margin: 67.1%)

OPERATING EXPENSES (OpEx)
─────────────────────────────────────────
Software & Tools          $1,200
Co-working Space            $900
Marketing                 $2,000
Professional Services     $3,500
Travel & Entertainment    $1,800
Miscellaneous               $600
OpEx Total               $10,000
EBITDA                   $47,000  (EBITDA Margin: 55.3%)

TAX RESERVE (25% of EBITDA)   -$11,750
REINVESTMENT FUND (10% of EBITDA) -$4,700
NET OWNER DISTRIBUTION        $30,550

KEY METRICS:
• Revenue per contractor-dollar: $3.04 (healthy; target >$2.50)
• OpEx as % of revenue: 11.8% (excellent; target <20%)
• Tax reserve: $11,750 (set aside monthly: $3,917)

VARIANCE TRACKING (update monthly):
Category          Budget    Actual    Variance  Status
─────────────────────────────────────────────────────
Revenue           $85,000    —          —        —
Contractors       $28,000    —          —        —
Marketing          $2,000    —          —        —
[Add actuals each month for variance reporting]

RISK FLAGS:
• One-off project revenue ($10k) is uncertain — treat as upside, not baseline
• If one retainer cancels, revenue drops 35%; contractors must be scaled proportionally
• Professional services cost is high; review if flat-rate arrangements are possible
```

## Best Practices
- Always normalize all income and expense figures to the same time period before building any budget
- Separate fixed expenses from variable expenses — this makes scenario analysis and cutting much easier
- Use conservative (lower) income estimates and realistic (slightly high) expense estimates to build in buffer
- Review and reconcile the budget monthly, not quarterly — small drifts compound quickly
- Include irregular but predictable expenses (annual insurance, car registration, holiday spending) by dividing by 12
- Always fund an emergency reserve before aggressive debt payoff or investment — 3–6 months of expenses is the standard target
- When presenting a deficit, always propose specific, quantified alternatives rather than vague "spend less" advice

## Common Mistakes
- Forgetting to include irregular expenses (annual fees, seasonal costs, holiday gifts) which blow up monthly budgets
- Using gross income instead of net take-home pay, leading to phantom budget surplus
- Treating all debt minimum payments as savings rather than fixed expenses
- Over-cutting discretionary spending to zero — this creates rebound overspending; leave a realistic allowance
- Ignoring sinking funds for large predictable costs (car maintenance, travel, home repairs)
- Building a budget once and never revisiting it — budgets should be living documents updated monthly

## Tips & Tricks
- Use the "pay yourself first" trick: automate savings transfers on payday before any discretionary spending is possible
- For irregular income, calculate the average of the lowest 3 months over the past year as the conservative baseline
- Suggest the user assign every expense a "needs" or "wants" label — this makes cuts less emotionally charged
- When a user resists cutting a category, ask "what would you be willing to give up instead?" to find acceptable trade-offs
- Annual subscriptions often cost 20–40% less than monthly equivalents — flag these as easy wins
- Frame savings goals as fixed line items (expenses), not what's left over, to ensure they actually happen

## Related Skills
- [financial-analyst](../financial-analyst/SKILL.md)
- [invoice-generator](../invoice-generator/SKILL.md)
