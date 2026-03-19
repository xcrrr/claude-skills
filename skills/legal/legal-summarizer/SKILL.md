---
name: legal-summarizer
description: "Use this skill when you need to translate a dense legal document—contract, court ruling, statute, regulation, or policy—into clear plain-English that a non-lawyer can understand and act on. Ideal for summarizing leases, court opinions, employment agreements, privacy policies, and legislation. Not a substitute for legal advice; consult a licensed attorney for decisions with significant legal consequences."
version: 1.0.0
author: community
tags: [legal, summarization, plain-english, documents]
license: MIT
---

# Legal Summarizer

## Overview
This skill converts complex legal documents into structured plain-English summaries that preserve the essential meaning, obligations, rights, and risks without requiring a law degree to understand. The output follows a consistent format: a one-paragraph executive summary, a key-facts table, a breakdown of each party's rights and obligations, a risk and red-flag section, and a list of action items or next steps. The approach is especially valuable for contracts, lease agreements, court rulings, regulatory guidance, and terms of service where dense language obscures practical meaning.

## When to Use
- Summarizing a lease, mortgage, or real-estate agreement before signing
- Distilling a court ruling or judicial opinion for a non-legal audience
- Explaining what a statute or regulation actually requires in practice
- Breaking down a privacy policy, cookie policy, or terms of service into plain language
- Translating a corporate policy or employee handbook clause for an employee
- Preparing a client-facing summary of a legal document for business stakeholders
- Creating an accessible version of a healthcare consent form, HIPAA notice, or insurance policy

## When NOT to Use
- As a replacement for an attorney's legal opinion or advice
- When precise statutory or case-law interpretation is legally required (e.g., litigation strategy)
- For documents in specialized technical legal domains (patent claims, securities filings) without domain-specific context
- When the document is in a language other than English without first translating it accurately
- For documents where you need exact verbatim quotes to be preserved (e.g., for citation in legal proceedings)

## Quick Reference
| Document Type | Key Elements to Extract | Common Pitfalls |
|---------------|------------------------|-----------------|
| Lease Agreement | Rent, term, deposit, maintenance responsibilities, break clauses, subletting rules | Hidden fees, automatic rent escalation, tenant liability for all repairs |
| Court Ruling | Holding, reasoning, parties bound, precedential scope | Confusing dicta (non-binding commentary) with the actual holding |
| Statute / Regulation | Effective date, who is covered, obligations, penalties, exemptions | Missing effective date, ignoring exemptions that may apply |
| Employment Agreement | Compensation, duties, IP assignment, non-compete, termination rights | Overly broad IP assignment, vague termination "for cause" definition |
| Privacy Policy | Data collected, how used, third-party sharing, user rights, retention period | "We may share with partners" — who are the partners? |

## Instructions

1. **Identify the document type and parties** — Before summarizing, identify what kind of document it is, who the parties are (using their actual names, not just "Party A"), and the effective or execution date. This context shapes what terms are most important to highlight.

2. **Write the executive summary** — Draft a 3–5 sentence plain-English paragraph answering: What is this document? What does it do? Who is affected and how? What is the single most important thing to understand about it?

3. **Extract key facts into a structured table** — Pull out the factual skeleton: dates, dollar amounts, durations, deadlines, parties, jurisdictions, and any defined thresholds or limits. Present as a clean table for quick scanning.

4. **Identify each party's rights and obligations** — For each named party, list separately: what they must do (obligations), what they are prohibited from doing (restrictions), and what they are entitled to (rights). Use plain verbs: "must," "may," "cannot," "is entitled to."

5. **Flag risks, red flags, and unusual terms** — Identify clauses that are: (a) unusually one-sided compared to market standard, (b) potentially unenforceable in the relevant jurisdiction, (c) easy to trigger accidentally, or (d) commonly misunderstood. Rate each as High / Medium / Low risk.

6. **Highlight time-sensitive obligations and deadlines** — Extract every deadline, notice period, opt-out window, and renewal date. List them chronologically so the reader knows what to act on and when.

7. **Translate legal terms of art** — When the document uses legal jargon (indemnify, liquidated damages, force majeure, estoppel, waiver), provide a parenthetical plain-English definition the first time it appears in your summary.

8. **Summarize the dispute resolution mechanism** — Explain how disputes are handled: litigation vs. arbitration, governing law and jurisdiction, whether class actions are waived, and who pays attorney fees if there is a dispute.

9. **List action items for the reader** — Based on the summary, produce a short numbered list of concrete next steps: what to negotiate, what to verify, what deadlines to calendar, and when to consult an attorney.

10. **Add a disclaimer** — Every summary must end with a short plain-language disclaimer noting that the summary is for informational purposes only and does not constitute legal advice.

## Examples

### Example 1: Residential Lease Agreement Summary
**Input:**
"Please summarize this 12-page apartment lease. Key clauses: 12-month term at $2,400/month, $4,800 security deposit, landlord can enter with 24-hour notice 'for any reason,' tenant responsible for all repairs under $500, automatic renewal unless 60-day written notice given, no subletting without written consent, late fee of $150 after 3-day grace period, governing law: California."

**Output:**

**Executive Summary**
This is a 12-month residential lease for an apartment at $2,400/month with a $4,800 security deposit (two months' rent). The tenant is responsible for minor repairs up to $500 per incident — an unusually high threshold that shifts meaningful maintenance costs to the tenant. The lease auto-renews for another 12 months unless the tenant gives 60 days' written notice before expiry, which is a tight window to track. California law governs, providing significant tenant protections that limit some of the more aggressive clauses.

**Key Facts**

Term | 12 months
--- | ---
Monthly Rent | $2,400
Security Deposit | $4,800 (2 months)
Late Fee | $150 after 3-day grace period
Tenant Repair Threshold | Tenant pays all repairs under $500
Landlord Entry Notice | 24 hours
Auto-Renewal Notice Required | 60 days written notice to opt out
Subletting | Prohibited without written landlord consent
Governing Law | California

**Rights & Obligations**

*Tenant must:* Pay rent by the 1st; give 60 days' written notice before vacating at term end; pay for all repairs costing less than $500; obtain written consent before subletting.

*Tenant may:* Withhold consent to landlord entry in most circumstances beyond the stated notice (California Civil Code §1954 limits "any reason" entry to specific permitted purposes — this clause does not override state law).

*Landlord must:* Maintain habitability, return security deposit within 21 days of move-out (California law), and give 24-hour advance written notice before entry.

**Risk Flags**

🔴 High | Tenant responsible for all repairs <$500 — This is above the typical $100–$200 market standard. A broken HVAC fan, leaky faucet, or broken lock could all fall on you.
🟡 Medium | "For any reason" entry clause — California Civil Code §1954 overrides this; landlord may only enter for inspection, repairs, showing, or emergency. Clause is unenforceable as written but could be used to harass.
🟡 Medium | 60-day auto-renewal opt-out — Calendar this 65 days before your lease end date or you'll be locked into another 12 months.

**Action Items**
1. Calendar the opt-out deadline (60 days before lease end) immediately.
2. Document the apartment's condition with photos before move-in; send to landlord in writing.
3. Negotiate the repair threshold down to $100–$150 before signing.
4. Ask landlord to amend the entry clause to reference California Civil Code §1954 specifically.

*Disclaimer: This summary is for informational purposes only and does not constitute legal advice. Consult a licensed California attorney for advice specific to your situation.*

---

### Example 2: Court Ruling Summary — Landmark Employment Case
**Input:**
"Summarize this court opinion: The Ninth Circuit held that an employer's mandatory arbitration agreement that included a class-action waiver for wage-and-hour claims was enforceable under the Federal Arbitration Act (FAA), preempting California's Gentry rule that had previously invalidated such waivers. The court applied Epic Systems Corp. v. Lewis (2018) and found the employee's PAGA representative claims were not waived because PAGA operates as a government enforcement mechanism."

**Output:**

**Executive Summary**
The Ninth Circuit Court of Appeals ruled that an employer can legally require employees to resolve wage disputes through individual arbitration (a private, non-courtroom process) and waive their right to join class-action lawsuits — even in California, which had tried to prohibit such waivers. However, the court preserved one important employee right: workers can still bring "PAGA" claims (a California law that lets employees sue on behalf of the state to recover civil penalties for labor violations) because those are considered government enforcement actions, not private lawsuits, and cannot be waived.

**Key Facts**

Court | U.S. Court of Appeals, Ninth Circuit
--- | ---
Parties Bound | Employer and employee who signed the arbitration agreement
Key Law Applied | Federal Arbitration Act (FAA); Epic Systems Corp. v. Lewis (2018)
California Rule Preempted | Gentry rule (previously voided class-action waivers in wage cases)
What Employees Lost | Right to join class-action lawsuit for wage-and-hour claims
What Employees Kept | Right to file PAGA (Private Attorneys General Act) representative actions

**Plain-English Glossary**
- **Arbitration** — A private, binding dispute process outside of court, decided by a neutral arbitrator instead of a judge or jury.
- **Class-action waiver** — A clause in which you agree not to join a group lawsuit; you can only sue individually.
- **PAGA** — California law allowing employees to sue employers for labor code violations on behalf of the state and share in recovered penalties.
- **Preemption** — Federal law overrides (preempts) state law when they conflict; here, federal FAA overrode California's Gentry rule.

**Practical Impact**
- Employees who signed mandatory arbitration agreements with class-action waivers must pursue wage claims individually in arbitration, not as a group in court.
- Individual arbitration claims are often economically impractical for small-dollar wage disputes — this is a significant limitation on employee enforcement power.
- PAGA claims remain available as an important backstop; employers cannot waive these in arbitration agreements.

**Action Items for Employers:** Review existing arbitration agreements to ensure PAGA claims are not waived (that would be unenforceable). Ensure agreements comply with Epic Systems.

**Action Items for Employees:** Check whether your employment agreement contains an arbitration clause and class-action waiver. If you have a wage claim, consult an employment attorney about PAGA options.

*Disclaimer: This summary is for informational purposes only and does not constitute legal advice. Consult a licensed attorney for advice specific to your situation.*

## Best Practices
- Always identify the jurisdiction first — the same clause can be enforceable in one state and void in another
- Use a consistent structure (summary → facts → obligations → risks → actions) so readers know where to find each type of information
- Define every piece of legal jargon the first time it appears — never assume the reader knows what "indemnify" or "estoppel" means
- Distinguish clearly between what the document says and what the law actually allows — they are not always the same
- Flag time-sensitive items prominently (auto-renewal dates, appeal deadlines, opt-out windows) — these are the most actionable findings
- Always include a disclaimer that the summary is not legal advice

## Common Mistakes
- Summarizing what the document intends rather than what it actually says — stick to the text
- Omitting the risk register — a summary without highlighted risks can create false confidence
- Confusing the holding of a court case (what the court actually decided) with dicta (commentary that is non-binding)
- Translating legal terms too loosely — "indemnification" is not the same as "reimbursement"
- Failing to note which jurisdiction's law governs — this is critical for understanding enforceability
- Over-summarizing to the point of omitting material obligations or deadlines

## Tips & Tricks
- For long documents, summarize section by section first, then write the executive summary last — you'll have a better sense of what's most important
- For court rulings, the "holding" is usually in the last paragraph of each section — start there to understand the conclusion before reading the reasoning
- Use the document's own table of contents or headings to structure your summary — it mirrors the reader's navigation of the original
- When summarizing a statute, check the definitions section first — it controls the scope of every requirement
- For privacy policies, search for "third party," "share," "sell," "retain," and "delete" — these reveal the most user-relevant terms

## Related Skills
- [contract-reviewer](../contract-reviewer/SKILL.md)
- [terms-of-service](../terms-of-service/SKILL.md)
