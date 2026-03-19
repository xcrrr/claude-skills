---
name: docx
description: "Use this skill when generating, planning, or describing structured Word-compatible documents from outlines, raw content, or templates including heading hierarchy, table structures, and formatting conventions. Not for editing existing DOCX files programmatically. Not for PDF layout or presentation slide design."
version: 1.0.0
author: community
tags: [files, documents, word, docx, formatting]
license: MIT
---

# DOCX

## Overview
This skill covers the design and generation of structured Microsoft Word-compatible documents (.docx format). It helps users translate raw content, outlines, or requirements into well-organized professional documents with consistent heading hierarchy, table structures, numbered sections, formatting conventions, headers/footers, styles, and page layout. This skill applies whether the output is a narrative document written in prose form (for human formatting in Word) or a structured description intended for programmatic generation using libraries like `python-docx`.

## When to Use
- Generating a complete DOCX document from an outline or brief
- Planning the structure and section hierarchy for a business report or proposal
- Describing table layouts, heading structures, and content for Word documents
- Converting raw meeting notes, bullet points, or data into a polished document
- Creating templates for recurring document types (reports, proposals, contracts)
- Planning multi-section documents with front matter, body, and appendices
- Describing DOCX structure for programmatic generation via `python-docx` or `docxtpl`

## When NOT to Use
- Editing an existing DOCX file's binary content (use Word application or python-docx directly)
- Designing a PDF layout with precise page positioning (use pdf skill)
- Creating presentation slides (use pptx skill)
- Generating spreadsheet workbooks (use xlsx skill)
- Writing long-form articles or blog posts without specific document structure requirements

## Quick Reference
| Task | Approach |
|------|----------|
| Define document structure | Use heading levels H1 (title), H2 (sections), H3 (subsections) |
| Format tables | Specify column headers, data rows, alignment, and whether header row is bold/shaded |
| Add front matter | Cover page, table of contents, executive summary before body sections |
| Number sections | Use "1. Introduction", "1.1 Background", "1.1.1 Context" hierarchy |
| Style body text | Specify font (Calibri 11pt default), line spacing (1.15 or 1.5), paragraph spacing |
| Insert figures/charts | Describe position (inline vs float), caption text, and reference in body |
| Page layout | Specify margins (Normal: 1in all sides), orientation (portrait/landscape), page size |

## Instructions

1. **Define the document purpose and audience** — Before writing, clarify: Who will read this document? What decisions should it support? What is the expected length? This determines the appropriate formality, section depth, and level of detail required.

2. **Plan the document hierarchy** — Outline the heading structure first:
   - **H1 (Title/Document Title)**: One per document, on the cover page
   - **H2 (Main Sections)**: Major divisions (e.g., Executive Summary, Background, Methodology)
   - **H3 (Subsections)**: Supporting content within each H2 section
   - **H4 (Sub-subsections)**: Only if necessary; avoid going deeper than H4

3. **Structure the front matter** — Professional documents typically include: cover page (title, author, date, version), table of contents (auto-generated in Word from heading styles), and an executive summary (1–2 pages for decision-makers who won't read the full document).

4. **Write section content** — For each section, plan: opening paragraph (what this section covers), body content (details, analysis, data), and closing statement or transition. Use numbered paragraphs for regulatory or legal documents; use flowing prose for reports and proposals.

5. **Design tables** — For each table: provide a title/caption, define column headers and their alignment (left, center, right), specify data types per column, and indicate if the header row should have background shading. Mark any cells that should be merged.

6. **Plan visual elements** — For figures, charts, or images: write the caption text, specify where in the text the figure is referenced, and describe the content. In a description for programmatic generation, also specify the image file path or chart data source.

7. **Add lists and callouts** — Bullet lists for unordered items (features, considerations), numbered lists for ordered items (steps, rankings), and callout boxes or shaded text boxes for important notes, warnings, or key findings.

8. **Define headers and footers** — Specify: left/center/right content in the header (company logo, document title, section name), left/center/right content in the footer (confidentiality notice, page number, date), and whether the first page has a different header/footer.

9. **Specify styles and formatting** — Define the style guide: body font (Calibri 11pt or Times New Roman 12pt), heading fonts and sizes, line spacing, paragraph spacing before/after, color scheme for headings. Consistent styles make the document look professional and are critical if others will extend the template.

10. **Add back matter** — Include as needed: appendices (labeled A, B, C), references/bibliography, glossary of terms, and revision history table.

## Examples

### Example 1: Project Proposal Document
**Input:** A consulting firm needs a project proposal for a client presenting a 6-month data platform modernization engagement.

**Output:**

**Document structure:**
```
Cover Page
  Title: "Data Platform Modernization: Project Proposal"
  Client: Acme Corp
  Prepared by: TechConsult LLC
  Date: [Month Year]
  Version: 1.0 | Confidential

Table of Contents (auto-generated)

1. Executive Summary (H2)
   One-page summary of the problem, proposed solution, timeline, and investment.

2. Background and Context (H2)
   2.1 Current State Assessment (H3)
       Description of existing data infrastructure, pain points.
   2.2 Business Drivers (H3)
       Why this project is necessary; business KPIs affected.

3. Proposed Solution (H2)
   3.1 Solution Architecture (H3)
       High-level architecture diagram (Figure 1). Description of components.
   3.2 Technology Stack (H3)
       Table: Component | Selected Technology | Rationale
   3.3 Data Migration Approach (H3)

4. Project Plan (H2)
   4.1 Phases and Milestones (H3)
       Table: Phase | Duration | Deliverables | Key Milestones
   4.2 Assumptions and Dependencies (H3)
   4.3 Risk Register (H3)
       Table: Risk | Likelihood | Impact | Mitigation

5. Team and Governance (H2)
   Table: Role | Name | Responsibility | Allocation (%)

6. Investment (H2)
   6.1 Fee Summary (H3)
       Table: Phase | Professional Fees | Expenses | Total
   6.2 Payment Terms (H3)

7. Terms and Conditions (H2)

Appendix A: Team Biographies
Appendix B: Client References
Appendix C: Revision History
  Table: Version | Date | Author | Changes
```

**Formatting conventions:**
```
Body text: Calibri 11pt, 1.15 line spacing, 6pt spacing after paragraph
H2 headings: Calibri 16pt Bold, Dark Blue (#1F3864), 12pt space before
H3 headings: Calibri 13pt Bold, Medium Blue (#2E75B6), 6pt space before
Table header rows: Bold, light blue background (#D6E4F0), centered
Page margins: 1 inch all sides
Header: Left = company logo | Right = "Confidential"
Footer: Left = document title | Center = page number | Right = date
```

### Example 2: Business Report with Executive Summary — python-docx Generation
**Input:** Generate a monthly operations report programmatically using python-docx.

**Output:**

**python-docx implementation:**
```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import datetime

def create_operations_report(month: str, data: dict) -> Document:
    doc = Document()

    # Set page margins
    section = doc.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.25)

    # Title
    title = doc.add_heading(f'Operations Report — {month}', level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Metadata
    doc.add_paragraph(f'Prepared: {datetime.date.today().strftime("%B %d, %Y")}')
    doc.add_paragraph(f'Department: Operations | Status: FINAL')
    doc.add_page_break()

    # Executive Summary
    doc.add_heading('Executive Summary', level=1)
    doc.add_paragraph(data['executive_summary'])

    # KPI Summary Table
    doc.add_heading('Key Performance Indicators', level=2)
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    headers = ['Metric', 'Target', 'Actual', 'Status']
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        hdr_cells[i].text = header
        hdr_cells[i].paragraphs[0].runs[0].bold = True

    for kpi in data['kpis']:
        row_cells = table.add_row().cells
        row_cells[0].text = kpi['metric']
        row_cells[1].text = str(kpi['target'])
        row_cells[2].text = str(kpi['actual'])
        row_cells[3].text = '✓' if kpi['met'] else '✗'

    # Operational Highlights
    doc.add_heading('Operational Highlights', level=1)
    for highlight in data['highlights']:
        doc.add_paragraph(highlight, style='List Bullet')

    # Issues and Risks
    doc.add_heading('Issues and Risks', level=1)
    for issue in data['issues']:
        p = doc.add_paragraph(style='List Number')
        p.add_run(issue['title']).bold = True
        p.add_run(f' — {issue["description"]}')

    return doc

# Usage
report = create_operations_report('January 2025', report_data)
report.save('operations_report_jan2025.docx')
```

## Best Practices
- Always define heading styles before writing content — consistent styles enable auto-TOC and navigation
- Use built-in Word/python-docx styles rather than manual formatting — they are portable and maintainable
- Keep tables simple — avoid merged cells when possible; they are hard to read and maintain
- Place the executive summary at the front — decision-makers often read only this section
- Use numbered sections for formal documents (government, legal, technical specs); prose headings for business reports
- Include a revision history table in all documents that will go through multiple review cycles
- Set `Track Changes` expectation up front if the document will be edited collaboratively

## Common Mistakes
- Inconsistent heading levels — skipping from H2 to H4 breaks table of contents and navigation
- Using manual bold/font changes instead of styles — breaks when the template is updated
- Overly wide tables that don't fit the page margins — always verify column widths sum to page width minus margins
- Forgetting page breaks between major sections — makes the document look unprofessional
- Using spaces for indentation instead of paragraph indent settings — breaks on different printers and screen sizes
- Creating a table of contents manually instead of using Word's auto-generate feature

## Tips & Tricks
- Use `docxtpl` for template-based generation — fill a Word template with Jinja2 syntax, much easier than building from scratch
- For complex tables, design in Excel first, then describe the structure for DOCX
- The `python-mammoth` library converts DOCX to clean HTML for web publishing
- Word's "Navigation Pane" is the best test: if headings show correctly there, the structure is right
- Use `styles.xml` in the DOCX to define a corporate style guide once and reuse across documents
- For very long documents, split into multiple DOCX files and use Word's Master Document feature
- PDF export from Word preserves all styles and is the safest format for sharing with external parties

## Related Skills
- [pdf](../pdf/SKILL.md)
- [pptx](../pptx/SKILL.md)
- [xlsx](../xlsx/SKILL.md)
