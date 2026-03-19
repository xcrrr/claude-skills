---
name: contract-reviewer
description: "Use this skill when you need to review a contract for risky clauses, missing protections, one-sided provisions, or negotiation leverage before signing. Suitable for employment agreements, SaaS subscriptions, vendor contracts, NDAs, and freelance agreements. Not a substitute for a licensed attorney — always seek qualified legal counsel for high-value or complex contracts."
version: 1.0.0
author: community
tags: [legal, contracts, risk, negotiation]
license: MIT
---

# Contract Reviewer

## Overview
This skill provides a structured approach to reading and critiquing contracts, surfacing clauses that expose you to undue risk, identifying terms that are missing or one-sided, and preparing you for negotiation. It covers common contract types including employment agreements, SaaS/vendor subscriptions, NDAs, independent contractor agreements, and partnership or licensing deals. The output is a prioritized risk register and a set of redlines or negotiation talking points — not a legal opinion. Always have a qualified attorney review contracts with significant financial or legal consequences.

## When to Use
- Reviewing an employment offer letter or employment agreement before signing
- Evaluating a SaaS vendor or software license agreement
- Examining an NDA presented by a potential partner or employer
- Reviewing an independent contractor or freelance services agreement
- Assessing a partnership, joint-venture, or revenue-sharing agreement
- Preparing a list of redlines or negotiation talking points for contract discussions
- Conducting a quick "sanity check" on a short agreement before engaging an attorney

## When NOT to Use
- As a replacement for a licensed attorney in high-value or high-risk transactions (M&A, real estate, litigation settlements)
- When the contract is in a jurisdiction with highly specialized requirements you are unfamiliar with
- For regulated industries (financial services, healthcare, government) where compliance implications are complex
- When the counterparty is already in breach and you need legal recourse strategy
- For court filings, legal briefs, or formal legal opinions

## Quick Reference
| Clause Type | Red Flag Signal | Suggested Fix |
|-------------|-----------------|---------------|
| Liability cap | "Unlimited liability" or no cap | Add mutual liability cap = 12 months of fees |
| IP assignment | "All work product … including pre-existing IP" | Carve out pre-existing IP explicitly |
| Non-compete | Broad geography, long duration (>1 year), vague scope | Narrow to specific role, geography, 6–12 months |
| Termination | "Terminate for convenience" with no notice | Add 30-day notice and payment for work done |
| Auto-renewal | Evergreen clause with short opt-out window | Negotiate 60-day opt-out window and price lock |
| Indemnification | Unilateral — only one party indemnifies | Make indemnification mutual or cap exposure |
| Governing law | Unfavorable jurisdiction | Negotiate to your home state/country |

## Instructions

1. **Identify the contract type** — Determine what kind of agreement you are reviewing (employment, NDA, SaaS subscription, services, licensing, partnership). The risk profile and standard market terms differ significantly by type.

2. **Locate and read the definitions section first** — Defined terms control the entire agreement. Pay close attention to how "Services," "Confidential Information," "Intellectual Property," "Term," and "Cause" are defined — overly broad definitions expand obligations dramatically.

3. **Map the key commercial terms** — Extract and tabulate: parties, effective date, term/duration, payment terms, deliverables or services, auto-renewal provisions, and termination rights. These form the factual skeleton of your review.

4. **Audit liability and indemnification** — Identify whether liability is capped, mutual, or unlimited. Flag any clause where one party indemnifies the other for broad categories (e.g., "any third-party claims"). Check whether indemnification is triggered by negligence alone or requires breach.

5. **Review intellectual property clauses** — Determine who owns: (a) work product created under the agreement, (b) pre-existing IP each party brings in, (c) improvements or derivatives. Flag any "work-for-hire" or broad assignment clauses that sweep in pre-existing IP.

6. **Examine non-compete, non-solicitation, and confidentiality clauses** — Note scope (role, geography, industry), duration, and enforceability. In many jurisdictions overly broad non-competes are unenforceable, but they still create chilling effects and litigation risk.

7. **Check termination and exit provisions** — Identify termination triggers (for cause vs. for convenience), notice periods, consequences upon termination (e.g., payment obligations, IP reversion, data return), and survival clauses listing terms that outlast termination.

8. **Review dispute resolution** — Note whether disputes go to arbitration (binding, private, limits class actions) or litigation; the governing law and jurisdiction; and whether the prevailing party recovers attorney fees.

9. **Identify missing standard protections** — For each contract type, note what is absent: e.g., no SLA in a SaaS agreement, no data breach notification requirement, no severance in an employment agreement, no payment schedule in a services contract.

10. **Produce a prioritized risk register** — Classify each finding as Critical (must fix before signing), Important (negotiate if possible), and Minor (acceptable as-is or low risk). Provide a specific redline suggestion or negotiation talking point for each Critical and Important item.

## Examples

### Example 1: Employment Contract Review
**Input:**
"Here is my offer letter from a startup. Key clauses: (1) 'Employee assigns to Company all inventions, whether or not related to Company's business, conceived during employment.' (2) 'Employee agrees not to work for any competitor in the US for 2 years post-employment.' (3) 'Company may terminate Employee at will with no notice.' (4) Salary $120k, no mention of equity vesting schedule despite 0.2% equity grant."

**Output:**

**Risk Register**

Priority | Clause | Issue | Recommended Redline
--- | --- | --- | ---
🔴 Critical | IP Assignment | Assigns ALL inventions including personal side projects unrelated to company business | Add: "Excluding inventions that (i) do not use Company resources, (ii) are developed entirely outside working hours, and (iii) do not relate to Company's current or reasonably anticipated business."
🔴 Critical | Non-Compete | 2-year US-wide non-compete is likely overbroad and potentially unenforceable (especially in CA, ND, OK, MN) but creates litigation risk | Negotiate to: 12 months, limited to direct competitors in your product category, within your specific geographic sales territory
🔴 Critical | Equity Vesting | No vesting schedule documented for 0.2% equity | Request attached Stock Option Agreement or Grant Notice specifying: standard 4-year vest / 1-year cliff, acceleration on change of control
🟡 Important | Termination | At-will with no notice leaves you with zero transition income | Request: 2-week notice period or 2-week severance in lieu of notice for involuntary termination without cause
🟢 Minor | No mention of expense reimbursement policy | Could create disputes over travel/equipment costs | Ask for reference to employee handbook or add standard expense reimbursement clause

**Negotiation Talking Points:**
- "The IP assignment clause is broader than industry standard — I'm happy to assign IP related to [Company]'s business but need a carve-out for personal projects I've been building independently."
- "A 2-year national non-compete is unusual for a role of this scope and jurisdiction. Would you consider 12 months limited to [specific product category]?"

---

### Example 2: SaaS Subscription Agreement Review
**Input:**
"We're signing a 2-year SaaS contract for a CRM platform at $48k/year. Notable clauses: (1) Auto-renews unless cancelled 90 days before term end. (2) Vendor can modify pricing with 30 days notice. (3) No SLA or uptime guarantee mentioned. (4) 'Customer grants Vendor a perpetual, irrevocable license to use Customer Data to improve Vendor's products.' (5) Liability cap = $500 (one month's fees)."

**Output:**

**Risk Register**

Priority | Clause | Issue | Recommended Redline
--- | --- | --- | ---
🔴 Critical | Customer Data License | Perpetual, irrevocable right to use your CRM data (customer records, deals, contacts) to train Vendor's products — a serious privacy and competitive risk | Replace with: "Vendor may use aggregated, anonymized usage data solely for product improvement. Vendor may not use Customer Data to train AI models or for any purpose other than providing the Services."
🔴 Critical | Liability Cap | $500 cap (1 month fee) on a $96k contract exposes you to full loss with no recourse | Negotiate cap to equal 12 months of fees paid ($48,000), with carve-outs for IP infringement and data breach
🔴 Critical | Auto-Renewal | 90-day cancellation window is unusually long — easy to miss | Negotiate to 30-day cancellation window; add price lock clause preventing increases at renewal without 90-day advance notice
🟡 Important | No SLA | No uptime commitment on business-critical CRM | Request 99.9% uptime SLA with service credits (e.g., 10% monthly fee credit per hour of excess downtime)
🟡 Important | Unilateral price change | 30-day notice is too short for budget planning | Negotiate: no price increases during initial term; 90-day notice + cap increases at CPI or 5% annually at renewal

**Bottom Line:** Do not sign as-is. The data license clause and $500 liability cap are dealbreakers for a $96k commitment. These are negotiable — enterprise SaaS vendors routinely accept DPA amendments and higher liability caps.

## Best Practices
- Always read the definitions section before any other clause — it controls everything
- Create a risk register rather than a running list of comments; priorities help focus negotiation energy
- Research market-standard terms for the specific contract type before negotiating — you need a baseline
- Request a redlined Word document rather than negotiating verbally — written changes create a record
- Never sign under artificial time pressure ("offer expires tomorrow") — legitimate counterparties allow reasonable review time
- Check the governing law clause early — it determines which jurisdiction's rules apply to your non-compete, IP, and dispute resolution

## Common Mistakes
- Focusing only on payment terms and ignoring IP, liability, and data clauses — the financial terms are often the least risky part
- Assuming standard templates are "non-negotiable" — most commercial terms are negotiable, especially for contracts over $10k
- Missing auto-renewal clauses buried in definitions or general terms sections
- Overlooking survival clauses that extend obligations (e.g., confidentiality, non-compete) years after termination
- Conflating "limitation of liability" with "indemnification" — they interact but are distinct protections
- Signing an NDA before reviewing what "Confidential Information" is defined to include

## Tips & Tricks
- Use Ctrl+F to search for: "unlimited," "perpetual," "irrevocable," "sole discretion," "at any time," "waive" — these words signal one-sided provisions
- Compare the indemnification clause structure: if it's indented and asymmetric (one party indemnifies, not both), that's a red flag
- For employment contracts in the US, check your state's specific non-compete laws before deciding whether to fight the clause
- Ask for a "mutual" version of any one-sided clause (NDA, indemnification, IP) as a first negotiation move — it's a reasonable ask
- The "entire agreement" clause means prior verbal promises don't count — get all commitments in the written contract

## Related Skills
- [legal-summarizer](../legal-summarizer/SKILL.md)
- [terms-of-service](../terms-of-service/SKILL.md)
