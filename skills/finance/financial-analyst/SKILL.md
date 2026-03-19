---
name: financial-analyst
description: "Use this skill when you need financial modeling, ratio analysis, or business financial health assessment — triggered by phrases like 'analyze my financials', 'calculate my burn rate', 'model this scenario', or 'is this business profitable'. Not for tax advice, bookkeeping, or regulated investment advisory services."
version: 1.0.0
author: community
tags: [finance, financial-analysis, modeling, ratios]
license: MIT
---

# Financial Analyst

## Overview
The Financial Analyst skill provides rigorous, structured analysis of financial data across income statements, balance sheets, and cash flow statements. It calculates key performance ratios such as ROI, EBITDA margins, burn rate, runway, LTV/CAC ratio, current ratio, and debt-to-equity. The skill models financial scenarios (best/base/worst case), assesses business financial health, and delivers clear narratives with data-driven recommendations. It is designed for founders, operators, investors, and finance teams who need rapid but credible analysis without a dedicated CFO.

## When to Use
- A founder or operator needs a financial health check on their startup or business
- A user wants to calculate and interpret key financial ratios from raw statements
- A user needs to model revenue growth or cost scenarios with projections
- An investor or analyst wants to assess unit economics (LTV, CAC, payback period)
- A user asks for burn rate, runway, or cash flow analysis
- A business owner needs to understand profitability drivers and margin trends
- A user wants a sensitivity analysis or break-even calculation
- A user needs to compare financial performance across periods or against benchmarks

## When NOT to Use
- The user requires regulated investment advice, securities recommendations, or portfolio management
- The task is tax preparation, tax strategy, or compliance filing
- The user needs forensic accounting or fraud investigation
- The analysis requires access to live market data or real-time stock prices
- The user needs an audited financial statement under GAAP/IFRS standards

## Quick Reference
| Task | Approach |
|------|----------|
| Profitability check | Calculate gross margin, EBITDA margin, net margin; compare to industry benchmarks |
| SaaS unit economics | Compute LTV = ARPU × Gross Margin ÷ Churn Rate; CAC = Sales+Marketing Spend ÷ New Customers |
| Burn rate & runway | Monthly Burn = Cash Out − Cash In; Runway = Cash Balance ÷ Net Burn Rate |
| Break-even analysis | Break-even Units = Fixed Costs ÷ (Price − Variable Cost per Unit) |
| ROI calculation | ROI = (Net Benefit ÷ Total Investment) × 100; annualize if needed |
| Liquidity check | Current Ratio = Current Assets ÷ Current Liabilities; Quick Ratio excludes inventory |
| Leverage assessment | Debt-to-Equity = Total Debt ÷ Shareholders' Equity; flag if >2.0 for most industries |

## Instructions

1. **Identify the analysis scope** — Clarify what statements or data the user has available (P&L, balance sheet, cash flow, or raw metrics like revenue and costs). Determine the time period (monthly, quarterly, annual) and whether this is a single-period snapshot or trend analysis across periods.

2. **Collect and normalize data** — Request all relevant figures. Ensure consistency: same currency, same period length, and proper categorization (e.g., COGS vs. OpEx). Flag any inconsistencies or missing line items that would materially affect the analysis.

3. **Build or reconstruct the income statement** — Organize data into: Revenue → Gross Profit (Revenue − COGS) → EBITDA (Gross Profit − OpEx) → EBIT (EBITDA − D&A) → Net Income (EBIT − Interest − Taxes). Calculate margins at each level.

4. **Analyze the balance sheet** — Assess assets (current vs. long-term), liabilities (current vs. long-term), and equity. Compute liquidity ratios (current ratio, quick ratio) and leverage ratios (debt-to-equity, debt-to-assets).

5. **Review cash flow** — Distinguish operating cash flow (the most important indicator of business health), investing cash flow, and financing cash flow. A business can be profitable on paper but cash-flow negative; flag this divergence explicitly.

6. **Calculate key ratios** — Select ratios appropriate to the business type:
   - **All businesses**: Gross Margin, EBITDA Margin, Net Margin, Current Ratio
   - **SaaS/Subscription**: MRR, ARR, Churn Rate, LTV, CAC, LTV:CAC ratio, Payback Period
   - **Startups**: Burn Rate, Runway, Months to Break-even
   - **Capital-intensive**: Asset Turnover, Return on Assets (ROA), Debt Service Coverage

7. **Benchmark against industry standards** — Compare key ratios to typical ranges for the industry. Clearly label whether each metric is healthy, borderline, or concerning.

8. **Build scenarios if requested** — Create best/base/worst case models by varying 2–3 key assumptions (revenue growth rate, churn, gross margin). Show the impact on the bottom line and runway under each scenario.

9. **Identify key risks and drivers** — Pinpoint the 2–3 variables that most influence financial outcomes. Highlight any red flags (negative working capital, declining margins, high CAC relative to LTV, short runway).

10. **Deliver findings and recommendations** — Present a structured summary: Financial Health Score (qualitative: Strong / Adequate / At Risk), key strengths, key risks, and 3–5 prioritized, specific action items with expected financial impact.

## Examples

### Example 1: SaaS Startup Financial Health Check
**Input:**
"We're a B2B SaaS startup. Monthly figures: MRR $42,000, new customers this month: 18, churned customers: 4 (out of 210 total), average contract value $2,400/year. Sales & marketing spend: $28,000/month. Gross margin: 74%. Cash in bank: $380,000. Monthly burn: $95,000 cash out, $42,000 cash in."

**Output:**
```
SAAS FINANCIAL HEALTH CHECK

─── REVENUE METRICS ───────────────────────────────
MRR                         $42,000
ARR (MRR × 12)             $504,000
Customer Count                   210
ARPU (MRR ÷ Customers)         $200/month

─── CHURN & RETENTION ─────────────────────────────
Monthly Churn Rate         4 ÷ 210 = 1.90%
Annual Churn Rate         ~20.6% (1 − (1−0.019)^12)
Assessment: ⚠ HIGH — SaaS benchmark target is <5% annual (0.4%/mo)

─── UNIT ECONOMICS ─────────────────────────────────
LTV = ARPU × Gross Margin ÷ Monthly Churn
    = $200 × 0.74 ÷ 0.019
    = $7,789

CAC = Sales & Marketing Spend ÷ New Customers
    = $28,000 ÷ 18
    = $1,556

LTV:CAC Ratio              $7,789 ÷ $1,556 = 5.0x  ✓ HEALTHY
  (Benchmark: >3x = good, >5x = excellent)

CAC Payback Period         $1,556 ÷ ($200 × 0.74) = 10.5 months
  (Benchmark: <12 months for SMB SaaS ✓)

─── BURN & RUNWAY ──────────────────────────────────
Gross Monthly Burn          $95,000
Monthly Revenue (cash in)   $42,000
Net Burn Rate               $53,000/month
Cash Balance               $380,000
Runway                     $380,000 ÷ $53,000 = 7.2 months  ⛔ CRITICAL

─── PROFITABILITY ───────────────────────────────────
Gross Profit (MRR × 74%)    $31,080
Net Monthly Loss           -$53,000 (assuming no other OpEx beyond S&M and COGS)

─── HEALTH ASSESSMENT ──────────────────────────────
Overall Rating: ⚠ AT RISK

✅ STRENGTHS:
• LTV:CAC of 5.0x is excellent — sales efficiency is strong
• Gross margin of 74% is healthy for SaaS (benchmark: 70–80%)
• CAC payback under 12 months

⛔ RISKS:
• CRITICAL: 7.2 months runway — fundraising or cost cuts needed immediately
• HIGH CHURN: 1.9%/month (20.6% annual) will erode revenue; must diagnose cause
• If churn is not addressed, LTV falls and unit economics deteriorate

─── RECOMMENDATIONS ────────────────────────────────
1. [URGENT] Begin fundraising or bridge financing — 7 months is inside the typical 6–9 month raise timeline
2. [HIGH] Conduct churn exit interviews on the 4 lost customers; identify if product, support, or pricing issue
3. [MEDIUM] Model a 20% S&M spend reduction ($5,600/mo) — extends runway by 1.4 months with modest CAC impact
4. [MEDIUM] Target expansion revenue (upsells) from existing 210 customers to improve net revenue retention
5. [LOW] Negotiate annual prepay discounts to accelerate cash collection and smooth burn
```

### Example 2: Investment ROI Analysis (Equipment Purchase)
**Input:**
"We're considering buying a CNC machine for $180,000. It will let us bring production in-house instead of outsourcing. Current outsourcing cost: $14,500/month. In-house operating cost (labor, materials, maintenance): estimated $6,200/month. Machine has a 10-year useful life with $15,000 salvage value. We use a 12% discount rate. Should we buy it?"

**Output:**
```
INVESTMENT ROI ANALYSIS — CNC Machine Purchase

─── BASIC FINANCIALS ───────────────────────────────
Initial Investment          $180,000
Monthly Cost Savings        $14,500 − $6,200 = $8,300/month
Annual Cost Savings         $8,300 × 12 = $99,600
Useful Life                 10 years
Salvage Value               $15,000
Discount Rate               12% (hurdle rate)

─── SIMPLE PAYBACK PERIOD ──────────────────────────
$180,000 ÷ $99,600 = 1.81 years (≈ 21.7 months)
Assessment: ✅ EXCELLENT — payback under 2 years

─── RETURN ON INVESTMENT (ROI) ─────────────────────
Total Savings (10 yrs)      $99,600 × 10 = $996,000
Total Cost                  $180,000 − $15,000 salvage = $165,000 net
Net Benefit                 $996,000 − $165,000 = $831,000
Simple ROI                  $831,000 ÷ $180,000 × 100 = 461.7%

─── NET PRESENT VALUE (NPV) ────────────────────────
Annual savings discounted at 12% over 10 years:
PV Annuity Factor (12%, 10yr) = 5.6502
PV of Savings = $99,600 × 5.6502 = $562,760
PV of Salvage = $15,000 × (1/1.12^10) = $15,000 × 0.3220 = $4,830
NPV = $562,760 + $4,830 − $180,000 = +$387,590

Assessment: ✅ STRONG POSITIVE NPV — invest

─── INTERNAL RATE OF RETURN (IRR) ──────────────────
IRR ≈ 55% (well above 12% hurdle rate)
Assessment: ✅ EXCEPTIONAL — IRR is 4.6× the required return

─── SENSITIVITY ANALYSIS ───────────────────────────
Scenario              Monthly Savings  NPV        Decision
─────────────────────────────────────────────────────────
Optimistic (+20%)         $9,960      +$500,521     BUY ✅
Base Case                 $8,300      +$387,590     BUY ✅
Pessimistic (−30%)        $5,810      +$181,380     BUY ✅
Break-even savings        ~$2,750/mo  NPV = $0     —

DECISION: Even under a 30% worse-than-expected scenario, the investment
generates strong positive returns. The break-even monthly savings needed
($2,750) is only 33% of projected savings — very large margin of safety.

─── RECOMMENDATION ─────────────────────────────────
STRONG BUY. The CNC machine purchase is financially compelling:
• 21-month simple payback (outstanding for capital equipment)
• NPV of +$387,590 at 12% discount rate
• IRR of ~55%, far exceeding the 12% hurdle
• Robust to significant downside scenarios

Consider: Verify in-house operating cost estimate with a pilot run if
possible. Confirm maintenance contract terms are included in the $6,200/mo
estimate. Explore financing — at 12% hurdle rate, debt <10% APR
improves returns further.
```

## Best Practices
- Always distinguish between cash-basis and accrual-basis figures — mixing them creates misleading analysis
- State all assumptions explicitly: growth rates, margins, discount rates. Readers must be able to challenge the inputs
- Use ranges and scenarios, not single-point estimates — all financial projections carry uncertainty
- Benchmark every ratio against industry context; a 40% gross margin means very different things in SaaS vs. retail
- Prioritize cash flow analysis — profits are an opinion, cash is a fact; many profitable businesses fail due to cash flow
- When presenting risks, quantify them: "churn increase of 1% reduces LTV by $X" is more useful than "churn is a risk"
- Flag data quality issues prominently; garbage in, garbage out — unreliable inputs must be noted

## Common Mistakes
- Confusing gross margin and net margin, leading to misstating profitability
- Using MRR × 12 = ARR without adjusting for churn — overstates forward revenue
- Ignoring working capital changes in cash flow — a growing business can be cash-negative even with profits
- Calculating LTV without including gross margin (using revenue instead of gross profit)
- Treating CAC as only ad spend — sales salaries, commissions, and tooling must be included
- Discounting at the wrong rate — using a risk-free rate for a risky startup overstates NPV dramatically
- Presenting projections without sensitivity analysis, giving false precision to uncertain numbers

## Tips & Tricks
- The "Rule of 40" is a quick SaaS health check: Revenue Growth Rate + Profit Margin should exceed 40%
- For startups, default alive vs. default dead analysis (when do you hit break-even on current trajectory?) is often more actionable than NPV
- A LTV:CAC below 3x is a warning; below 1x the business model is fundamentally broken
- Quick runway extension levers: reduce S&M (least impactful on near-term revenue), defer hiring, negotiate vendor payment terms
- When analyzing an income statement for the first time, look at gross margin trend before anything else — compression there is the most dangerous early signal
- For capital investments, always run break-even sensitivity: "how bad does this have to get for the investment to be wrong?" builds decision confidence

## Related Skills
- [budget-planner](../budget-planner/SKILL.md)
- [invoice-generator](../invoice-generator/SKILL.md)
