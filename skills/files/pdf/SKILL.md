---
name: pdf
description: "Use this skill when describing, summarizing, extracting structured data from, or answering questions about PDF documents, or when planning PDF layout and structure for reports, contracts, and publications. Not for editing binary PDF files directly. Not for converting PDFs to other formats programmatically."
version: 1.0.0
author: community
tags: [files, pdf, documents, extraction, summarization]
license: MIT
---

# PDF

## Overview
This skill covers working with PDF documents in two primary modes: (1) comprehension and extraction — reading, summarizing, and pulling structured data from PDF content; and (2) layout planning — designing the structure, sections, and visual hierarchy of a new PDF document for reports, contracts, research papers, or publications. For comprehension tasks, it applies structured extraction, hierarchical summarization, and question-answering techniques. For layout tasks, it describes the page structure, section organization, typography, and visual design that tools like LaTeX, ReportLab, WeasyPrint, or Adobe InDesign should implement.

## When to Use
- Summarizing a long PDF report into a structured briefing or executive summary
- Extracting tables, financial figures, dates, names, or clauses from a PDF document
- Answering specific questions about the contents of a PDF
- Planning the section layout and page design for a new PDF report or publication
- Describing PDF structure for programmatic generation using ReportLab or WeasyPrint
- Reviewing PDF contracts to identify key clauses, obligations, and risk terms
- Converting PDF content into structured JSON, Markdown, or CSV

## When NOT to Use
- Editing the binary content of an existing PDF (use Adobe Acrobat or pdf manipulation tools)
- Converting PDF files to DOCX or other formats (use conversion tools like `pdf2docx`, LibreOffice)
- Creating presentation slides (use pptx skill)
- Generating DOCX reports (use docx skill)
- OCR of scanned image-only PDFs without text layer (requires specialized OCR tools like Tesseract)

## Quick Reference
| Task | Approach |
|------|----------|
| Summarize a PDF | Hierarchical summary: document summary → section summaries → key findings |
| Extract a table | Identify column headers, data types per column, output as Markdown or JSON |
| Find specific data | Quote the exact text with page reference; flag if not found explicitly |
| Identify key clauses | Scan for section headings; extract clause text, obligation, and party responsible |
| Plan PDF layout | Define: page size, margins, header/footer, section hierarchy, font stack, color palette |
| Generate PDF programmatically | Use ReportLab (Python) for data-driven PDFs; WeasyPrint for HTML-to-PDF |
| Compare two PDFs | Identify additions, deletions, and changed clauses between versions |

## Instructions

1. **Understand the document type** — Identify what kind of PDF you are working with: research paper, financial report, legal contract, government form, technical manual, or marketing brochure. Each type has different structural conventions and extraction priorities.

2. **Navigate the document structure** — Review the table of contents or section headings to build a mental map of the document. For extraction tasks, identify which sections contain the target data before diving in. For long documents (100+ pages), focus on the executive summary, section introductions, and conclusion.

3. **For summarization — apply hierarchical structure** — Create a three-level summary:
   - **Document-level**: 1–3 sentences capturing the core purpose and key conclusions
   - **Section-level**: 2–4 sentences per major section
   - **Key findings**: Bullet list of the most actionable or important points

4. **For data extraction — identify target entities** — Define what you are looking for before reading: specific data types (dates, monetary amounts, percentages, names), specific tables (revenue by quarter, list of parties, schedule of deliverables), or specific clauses (termination, liability, payment terms). Then systematically search and extract.

5. **Present extracted data in structured format** — Always convert extracted data to a clean format:
   - Tables → Markdown table or JSON array
   - Key-value pairs → YAML or JSON object
   - Contract clauses → Section title + quote + interpretation + risk flag
   - Financial figures → Consistent unit format (all in millions, or all in thousands)

6. **Flag ambiguities and gaps** — When data is implied but not explicitly stated, flag it. When a section is unclear or contradictory, note it. When the document appears to be missing pages or the extraction may be incomplete, say so explicitly.

7. **For PDF layout planning — define the grid** — Specify: page size (A4 or Letter), margins (top/bottom/left/right), number of columns (single, two-column academic style, etc.), gutter width between columns, and baseline grid for text alignment.

8. **Define the typography system** — Specify: primary font (serif for formal, sans-serif for modern), heading hierarchy sizes, body text size and line height, caption style, and code/monospace font if needed. Define a limited color palette (typically 2–3 colors: primary, secondary, accent).

9. **Plan the page components** — Describe: running headers (chapter title, document title), page numbers (position and format), footer content (confidentiality, date), and any watermarks or security markings.

10. **For programmatic generation — provide the data schema** — If the PDF is data-driven (a report generated from a database), define the data schema that feeds the template: field names, types, formatting rules, and conditional logic (e.g., show a warning box if value exceeds threshold).

## Examples

### Example 1: Extracting Key Data from a PDF Annual Report
**Input:** A 120-page annual report PDF for a publicly traded company. Extract: revenue, net income, EPS, segment breakdown, and key risk factors.

**Output:**

**Document summary:**
```
Acme Corp 2024 Annual Report (120 pages) covers fiscal year ended December 31, 2024.
The company reported record revenue driven by North America growth, offset by EMEA softness.
Key risks include regulatory changes in the EU and supply chain concentration in Southeast Asia.
```

**Financial highlights (extracted from pages 8–12, Consolidated Statements of Operations):**
```json
{
  "fiscal_year": 2024,
  "currency": "USD millions",
  "revenue": {
    "total": 4823,
    "yoy_change_pct": 12.4
  },
  "gross_profit": {
    "amount": 2156,
    "margin_pct": 44.7
  },
  "operating_income": {
    "amount": 891,
    "margin_pct": 18.5
  },
  "net_income": {
    "amount": 672,
    "margin_pct": 13.9
  },
  "earnings_per_share": {
    "basic": 4.21,
    "diluted": 4.18
  }
}
```

**Segment breakdown (from page 15, Segment Revenue table):**
| Segment | Revenue ($M) | YoY Growth | % of Total |
|---------|-------------|------------|------------|
| North America | 2,841 | +18.2% | 58.9% |
| EMEA | 1,124 | -2.1% | 23.3% |
| Asia Pacific | 858 | +14.7% | 17.8% |

**Key risk factors (from pages 34–41, Risk Factors section):**
```
1. Regulatory Risk (EU AI Act) — New regulations may require product modifications
   by Q3 2025, estimated compliance cost of $40–60M (page 35)
2. Supply Chain Concentration — 73% of component sourcing from two suppliers in
   Vietnam and Thailand; single supplier disruption could reduce production by 30% (page 37)
3. Currency Risk — 41% of revenue denominated in non-USD currencies; 10% USD
   strengthening would reduce reported revenue by ~$198M (page 39)
```

**Extraction confidence notes:**
- Financial figures verified against both the income statement (p. 10) and the MD&A summary (p. 8)
- Segment data extracted from Note 4 (p. 15); prior year comparisons from same note
- Risk factor descriptions are paraphrased; exact quotes available on request

### Example 2: Summarizing and Reviewing a PDF Contract
**Input:** A 45-page SaaS Master Service Agreement (MSA). Identify key obligations, risk clauses, and any non-standard terms.

**Output:**

**Contract overview:**
```
Document: Master Service Agreement
Parties: TechVendor Inc. (Vendor) and ClientCorp Ltd. (Customer)
Effective Date: January 1, 2025
Term: 3 years with automatic renewal
Governing Law: State of Delaware, USA
```

**Key obligations by party:**

| Obligation | Party | Section | Notes |
|------------|-------|---------|-------|
| Maintain 99.9% uptime SLA | Vendor | §5.2 | Credits apply for downtime > 0.1% |
| Pay invoices within 30 days | Customer | §8.1 | 1.5%/month late fee |
| Provide security incident notice within 48 hours | Vendor | §9.3 | Non-standard: industry norm is 72 hours |
| Maintain SOC 2 Type II certification | Vendor | §9.1 | Annual report required |
| Provide 6-month termination notice | Customer | §12.1 | ⚠️ Non-standard: typical is 30–90 days |

**Risk flags — clauses requiring legal review:**
```
⚠️  HIGH: §11.3 — Liability cap set at 3 months of fees. Standard is 12 months.
    Recommendation: Negotiate to minimum 6 months or last 12 months of fees paid.

⚠️  MEDIUM: §7.2 — Vendor retains right to use Customer data for "product improvement."
    Recommendation: Add exclusion for confidential or PII data; require opt-out option.

⚠️  MEDIUM: §12.4 — Auto-renewal with 6-month notice requirement (Customer).
    Standard notice period is 30–90 days. Risk of unintended renewal.

ℹ️  NOTE: §13.1 — Vendor can modify pricing with 60-day notice during term.
    Standard is fixed pricing for the term. Flag for pricing stability discussion.
```

**Missing standard clauses:**
- No data processing addendum (DPA) referenced — required for GDPR compliance
- No escrow provision for source code — risk if Vendor goes out of business
- No audit rights clause — Customer cannot verify Vendor's security or compliance claims

## Best Practices
- Always cite page numbers or section numbers when extracting or quoting from a PDF
- Distinguish between explicit statements and your interpretation — use "the document states..." vs "this implies..."
- For financial extraction, cross-check figures across multiple sections (income statement vs MD&A)
- When planning PDF layout, use a grid system — it creates visual consistency without repeated manual specification
- For contracts, organize extraction by party obligation, not by document order — it's more useful to reviewers
- Flag "non-standard" clauses by comparison to industry norms, not just your preference
- For long documents, create a structured extract/summary before answering specific questions

## Common Mistakes
- Summarizing only the first and last sections — middle sections often contain critical technical or financial detail
- Confusing tables in the PDF with appendices — confirm data provenance before quoting
- Missing footnotes and endnotes — they often contain critical qualifications and exceptions
- Treating scanned PDFs as text PDFs — if there is no text layer, extraction requires OCR first
- Presenting extracted numbers without their units or time periods — creates ambiguity
- Ignoring defined terms in contracts — "Customer" may have a specific definition different from the colloquial use

## Tips & Tricks
- For large PDFs, process section by section rather than the whole document at once
- Look for a "Key Metrics" or "Highlights" box near the front of reports — it's often the most dense summary
- In contracts, the Schedule and Exhibit sections often contain the binding commercial terms — don't skip them
- Use `pdfplumber` (Python) for accurate table extraction from PDFs with complex layouts
- For redline comparison of two contract versions, `diff-pdf` or Word's compare feature works well
- `PyMuPDF (fitz)` is fastest for extracting raw text; `pdfplumber` is best for tables; `camelot` is best for financial tables

## Related Skills
- [docx](../docx/SKILL.md)
- [pptx](../pptx/SKILL.md)
- [xlsx](../xlsx/SKILL.md)
