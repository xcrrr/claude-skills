---
name: invoice-generator
description: "Use this skill when you need to create, format, or review a professional invoice — triggered by phrases like 'generate an invoice', 'bill my client', 'create an invoice for', or 'write up my charges'. Not for tax returns, payroll processing, or accounts-receivable system integrations."
version: 1.0.0
author: community
tags: [finance, invoicing, freelance, billing]
license: MIT
---

# Invoice Generator

## Overview
The Invoice Generator skill produces complete, professional invoices for freelancers, consultants, agencies, and small businesses. It correctly structures line items, quantities, unit rates, subtotals, applicable taxes, discounts, payment terms, and due dates. The skill handles hourly, project-based, retainer, and milestone billing models. Output is formatted for readability and professional presentation — suitable for direct use in email or conversion to PDF. It also catches common invoicing errors such as incorrect tax calculations, missing required fields, and unclear payment terms that delay client payment.

## When to Use
- A freelancer needs to bill a client for completed work (hourly or project-based)
- A consultant needs to invoice for a retainer, milestone, or deliverable
- A small business needs to generate an invoice for products sold or services rendered
- A user needs to add taxes (VAT, GST, sales tax) correctly to a bill
- A user wants to include payment terms, late fee clauses, or bank transfer instructions
- A user needs to re-issue or correct a previous invoice
- A user wants a quick-reference invoice number scheme or tracking approach

## When NOT to Use
- The user needs a full accounting system or automated invoicing software setup
- The task involves payroll processing or employee pay stubs
- The user needs legal contract drafting (scope of work, service agreement)
- The task requires integration with accounting software (QuickBooks, Xero, FreshBooks)
- The user needs tax remittance calculations or VAT return filing

## Quick Reference
| Task | Approach |
|------|----------|
| Hourly billing | Line item: Hours × Hourly Rate; list each engagement type separately if rates differ |
| Fixed-price project | Single line item or milestone-based items; reference deliverable description |
| Retainer invoice | State retainer period, monthly fee, and hours/deliverables included |
| Tax calculation | Apply tax rate to taxable subtotal only; note tax ID/number on invoice |
| Late fee clause | State: "Invoices unpaid after [N] days subject to [X]% monthly fee" |
| Invoice numbering | Use format: INV-[YEAR]-[SEQUENCE], e.g., INV-2025-0042 |
| Payment methods | List accepted methods and include all required details (account, routing, PayPal, etc.) |

## Instructions

1. **Collect sender (your) information** — Gather the invoicing party's full legal name or business name, address, email, phone number, and tax/VAT/GST registration number (if applicable).

2. **Collect client (recipient) information** — Get the client's company name, billing contact name, billing address, and any required purchase order (PO) number or billing reference the client needs on the invoice.

3. **Assign an invoice number and date** — Generate a unique, sequential invoice number (e.g., INV-2025-0042). Record the invoice date (today) and calculate the due date based on the agreed payment terms (Net 15, Net 30, etc.).

4. **List all line items** — For each deliverable or service:
   - Write a clear, specific description (avoid vague terms like "services rendered")
   - Specify quantity (hours, units, days, licenses)
   - Specify unit rate (per hour, per unit, flat fee)
   - Calculate line total (Quantity × Rate)

5. **Apply discounts if applicable** — If a discount was agreed, show it as a separate line item as a negative amount or percentage, keeping the calculation transparent.

6. **Calculate the subtotal** — Sum all line item totals before tax. This is the taxable base (or pre-tax base if some items are tax-exempt).

7. **Apply taxes correctly** — Identify the applicable tax type and rate (Sales Tax, VAT, GST). Apply only to taxable items. Show the tax amount as a separate line. If tax-exempt, state the reason (e.g., "Services exported outside the EU — VAT exempt under Article 44").

8. **Calculate the total amount due** — Subtotal ± Discount + Tax = Total Due. State the currency clearly (USD, EUR, GBP, etc.).

9. **State payment terms and methods** — Include:
   - Payment due date (not just "Net 30" — include the actual calendar date)
   - Accepted payment methods with full details (bank account + routing numbers, PayPal, Stripe link, check payable to)
   - Late payment fee clause if applicable

10. **Add any required notes** — Include project reference numbers, PO numbers, contract clause references, or client-specific billing codes. Add a brief thank-you note for professional courtesy.

## Examples

### Example 1: Freelance Web Developer Invoice
**Input:**
"I'm a freelance developer. I need to invoice Acme Corp for: 22 hours of frontend development at $125/hr, 8 hours of code review at $95/hr, and a fixed-fee deployment setup for $350. My client's PO number is PO-8812. Payment terms are Net 30. I'm in the US and don't charge sales tax. My payment info is Chase bank, routing 021000021, account 4567890123. Invoice should be from Jane Doe Web Development."

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        INVOICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FROM                              TO
Jane Doe Web Development          Acme Corp
jane@janedoeweb.dev               Accounts Payable
(555) 867-5309                    123 Business Ave
Portland, OR 97201                New York, NY 10001

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Invoice #:    INV-2025-0042
Invoice Date: June 18, 2025
Due Date:     July 18, 2025  (Net 30)
PO Number:    PO-8812
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LINE ITEMS
┌────────────────────────────────┬──────┬──────────┬───────────┐
│ Description                    │  Qty │    Rate  │    Total  │
├────────────────────────────────┼──────┼──────────┼───────────┤
│ Frontend Development           │   22 │ $125.00  │ $2,750.00 │
│ (React component build,        │  hrs │    /hr   │           │
│  responsive design, QA fixes)  │      │          │           │
├────────────────────────────────┼──────┼──────────┼───────────┤
│ Code Review & Documentation    │    8 │  $95.00  │   $760.00 │
│ (PR reviews, inline comments,  │  hrs │    /hr   │           │
│  README updates)               │      │          │           │
├────────────────────────────────┼──────┼──────────┼───────────┤
│ Production Deployment Setup    │    1 │ $350.00  │   $350.00 │
│ (CI/CD pipeline, env config,   │ flat │   flat   │           │
│  staging + prod environments)  │      │          │           │
└────────────────────────────────┴──────┴──────────┴───────────┘

                              Subtotal:    $3,860.00
                           Tax (0%):           $0.00
                     ─────────────────────────────
                     TOTAL DUE (USD):    $3,860.00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PAYMENT INSTRUCTIONS
Please remit payment by July 18, 2025.

Bank Transfer (ACH/Wire):
  Bank:          Chase Bank
  Routing #:     021000021
  Account #:     4567890123
  Account Name:  Jane Doe Web Development

Checks payable to: Jane Doe Web Development

Late Payment: Invoices unpaid after 30 days are subject to a
1.5% monthly service charge on the outstanding balance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Thank you for your business! It's a pleasure working with you.
Questions? Contact jane@janedoeweb.dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Example 2: Consulting Services Invoice with VAT
**Input:**
"I run a UK-based strategy consulting firm, Apex Consulting Ltd. VAT registered (GB123456789). Client is TechStart GmbH, based in Germany (B2B). Invoice for: 3 days of strategy workshop facilitation at £1,800/day, a written strategic roadmap deliverable at £2,500 fixed, and £340 in reimbursable travel expenses (London–Frankfurt flights). B2B EU client so zero-rated VAT under reverse charge. Payment terms Net 14. We accept bank transfer only."

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        INVOICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FROM                              TO
Apex Consulting Ltd               TechStart GmbH
14 King Street                    Rosenthaler Str. 40
London, EC2V 8EA                  10178 Berlin, Germany
United Kingdom
VAT No: GB123456789               VAT No: DE987654321

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Invoice #:    INV-2025-0018
Invoice Date: 18 June 2025
Due Date:     2 July 2025  (Net 14)
Project Ref:  Digital Transformation Strategy Q2 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LINE ITEMS
┌────────────────────────────────────┬─────┬──────────┬───────────┐
│ Description                        │ Qty │    Rate  │    Total  │
├────────────────────────────────────┼─────┼──────────┼───────────┤
│ Strategy Workshop Facilitation     │   3 │ £1,800   │  £5,400   │
│ (On-site Berlin, 19–21 May 2025;   │ days│    /day  │           │
│  leadership alignment sessions,    │     │          │           │
│  facilitated working groups)       │     │          │           │
├────────────────────────────────────┼─────┼──────────┼───────────┤
│ Strategic Roadmap — Written        │   1 │ £2,500   │  £2,500   │
│ Deliverable (3-year roadmap,       │ flat│   flat   │           │
│  initiative prioritisation matrix, │     │          │           │
│  executive summary deck)           │     │          │           │
├────────────────────────────────────┼─────┼──────────┼───────────┤
│ Reimbursable Travel Expenses       │   1 │   £340   │    £340   │
│ (London LHR–Frankfurt FRA return;  │     │  actual  │           │
│  receipts attached)                │     │          │           │
└────────────────────────────────────┴─────┴──────────┴───────────┘

                              Subtotal:      £8,240
            VAT (0% — Reverse Charge):         £0
          ───────────────────────────────────────
                     TOTAL DUE (GBP):      £8,240

VAT NOTE: Services supplied to a business customer established
outside the UK (EU). Zero-rated for UK VAT purposes under the
place of supply rules (S.7A VATA 1994). The recipient (TechStart
GmbH) is liable to account for VAT under the EU reverse charge
mechanism in Germany.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PAYMENT INSTRUCTIONS
Payment due by 2 July 2025.

Bank Transfer:
  Bank:          Barclays Bank PLC
  Sort Code:     20-00-00
  Account No:    12345678
  Account Name:  Apex Consulting Ltd
  IBAN:          GB29 BARC 2000 0012 3456 78
  BIC/SWIFT:     BARCGB22

Payment must be made in GBP. Any bank charges are for the
payer's account.

Late Payment: Interest charged at 8% above Bank of England
base rate per annum under the Late Payment of Commercial
Debts (Interest) Act 1998.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Travel expense receipts enclosed. Please contact
billing@apexconsulting.co.uk with any queries.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Best Practices
- Always include both the invoice date AND the actual due date (not just "Net 30") — ambiguity delays payment
- Write line item descriptions specifically enough that any reader understands what was delivered without needing a contract
- Separate reimbursable expenses from service fees as distinct line items for transparency and audit clarity
- Include your tax registration number on every invoice if you are VAT/GST registered — omitting it can be illegal
- Use a consistent, sequential invoice numbering scheme from day one — this aids tracking and looks professional
- Send invoices promptly — the longer you wait after project completion, the longer you wait to be paid
- Keep copies of all invoices and acknowledgment emails; in disputes, documentation is everything

## Common Mistakes
- Listing "services rendered" or "consulting services" without any specifics — clients and their accountants need detail
- Forgetting to include the client's PO or reference number, causing the invoice to be rejected by their AP department
- Calculating tax on the full invoice total including non-taxable reimbursements (travel expenses are often not taxable)
- Using inconsistent payment terms (e.g., saying "Net 30" in email but "due on receipt" on the invoice)
- Not stating the currency, which causes confusion for international clients
- Omitting your bank details or PayPal information, forcing follow-up emails that delay payment
- Re-using invoice numbers or leaving gaps in sequences, which raises red flags for tax authorities

## Tips & Tricks
- Set up a template with your logo, contact details, and bank info pre-filled to reduce preparation time per invoice
- Add a "payment link" note (Stripe, PayPal.me) for clients who prefer card payment — it significantly speeds up collection
- For long-term clients, consider switching to automatic recurring invoices (retainer model) to reduce admin friction
- If a client is consistently late, add a prompt pay discount (e.g., 2% discount if paid within 5 days) — it works better than late fees in most relationships
- For international invoices, include both the exchange rate used and the local currency equivalent as a courtesy
- Number invoices starting at 101 or 1001 rather than 001 — this avoids signaling to clients that they are your first customer

## Related Skills
- [budget-planner](../budget-planner/SKILL.md)
- [financial-analyst](../financial-analyst/SKILL.md)
