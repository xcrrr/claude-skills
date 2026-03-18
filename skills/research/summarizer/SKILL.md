---
name: summarizer
description: "Use this skill when condensing long documents, articles, reports, or passages into shorter, accurate summaries. Trigger phrases: 'summarize this', 'give me the key points', 'TL;DR', 'condense this document'. Do NOT use when author voice and style must be preserved for creative works, or as a substitute for full reading of legal contracts, medical documents, or other high-stakes materials."
version: 1.0.0
author: community
tags: [research, summarization, synthesis, reading]
license: MIT
---

# Summarizer

## Overview
This skill produces clear, accurate, and appropriately condensed summaries of documents, articles, reports, research papers, and other long-form content. A great summary is not just shorter—it is a faithful representation of the original's key claims, structure, and conclusions, stripped of repetition, filler, and tangential detail. This skill handles executive summaries, abstract-style synopses, bullet-point briefings, and layered summaries (a brief headline summary plus a more detailed breakdown). The goal is to save time while ensuring that nothing essential is lost.

## When to Use
- Condensing a research paper, report, or article into a brief overview
- Creating an executive summary for a business document or proposal
- Generating a TL;DR for a long online article or thread
- Summarizing meeting notes, transcripts, or recorded discussions
- Producing a structured briefing from a dense technical document
- Summarizing multiple sources into a comparative overview
- Generating chapter-by-chapter summaries of a book or long report

## When NOT to Use
- Creative writing or fiction where the author's voice and style are the point (a summary cannot substitute for the experience of the work)
- Legal contracts and agreements that you or others must act on—always read these fully or consult a lawyer; a summary may miss critical terms
- Medical instructions or informed consent documents where exact wording matters
- When the entire document needs to be read for compliance, accreditation, or legal reasons
- Literary analysis (summarizing ≠ analyzing; use `academic-essay` skill for analysis)

## Quick Reference
| Task | Approach |
|------|----------|
| Executive summary | 5–10% of original length; lead with conclusion, then key findings |
| TL;DR | 1–3 sentences; one per major point |
| Bullet briefing | 5–10 bullets, each a self-contained key point |
| Abstract-style | ~250 words; background, purpose, method, findings, conclusion |
| Chapter summaries | One paragraph per chapter; maintain document order |
| Comparative | Side-by-side key points from multiple sources |
| Accuracy check | Every claim in the summary must be traceable to the source |

## Instructions

1. **Identify the summary type and length target.** Before reading, determine what the user needs: a one-sentence TL;DR, a paragraph synopsis, a structured bullet list, or a multi-page executive summary. The appropriate compression ratio and format depend on the use case. A research briefing needs different treatment than a quick article overview.

2. **Read the full source before writing.** Skim-and-summarize produces inaccurate summaries. Read completely to understand the overall structure and identify which sections carry the most weight. Pay special attention to abstracts, introductions, conclusions, and section headings—these signal the author's own view of what matters most.

3. **Identify the core claim and main supporting points.** Every document has a central argument, finding, or purpose. State it in one sentence. Then identify the 3–7 most important supporting points, findings, or sections. Everything else is context or elaboration that can be compressed or omitted.

4. **Determine what to cut.** Remove: repetition of previously made points, extended examples (unless they are the only way to understand a key concept), methodology details (in most non-technical summaries), hedging language that doesn't change the essential claim, and background information already known to the audience.

5. **Write the summary in your own words.** Do not paste phrases from the original unless quoting a definition or critical specific term. Paraphrasing forces you to actually understand the content rather than copying language that may obscure whether the meaning was captured. Use plain language—if the original is dense, the summary should be clearer.

6. **Structure the summary to match the use case.** For executive summaries: lead with the bottom line, then key supporting points, then method/scope, then recommendations. For research summaries: follow the IMRaD structure (introduction/purpose, methods, results, discussion/conclusions). For article briefings: follow the original structure or reorganize by importance.

7. **Verify accuracy.** Read each sentence in your summary and trace it back to a specific part of the source. If a claim in the summary can't be located in the original, remove it. Watch especially for: overstating certainty (the original may say "suggests" but you wrote "proves"), generalizing from a specific finding, and omitting crucial qualifications (e.g., "in a sample of college students").

8. **Add a note about what was omitted.** For important documents, briefly note what the summary does not cover: "This summary covers the main findings; detailed methodology, appendices, and case studies are not included."

## Examples

### Example 1: Research Paper Abstract-Style Summary

**Input:** "Summarize this research paper in about 200 words in abstract style: [Paper: A 35-page study on the effects of a four-day workweek pilot at 61 UK companies in 2022. 2,900 employees participated. The study found that productivity was maintained or improved at 95% of companies, employee burnout scores decreased by 71%, resignations fell by 57%, revenue grew by 35% on average, and 92% of companies planned to continue the four-day week. The researchers used a combination of weekly surveys, productivity metrics, and HR data. The study was conducted by researchers at Cambridge University, Boston College, and Oxford University.]"

**Output:**

---

**Summary**

This study examined the outcomes of a six-month, four-day workweek pilot program across 61 UK companies involving approximately 2,900 employees. Conducted by researchers at Cambridge University, Boston College, and Oxford University, the study drew on weekly employee surveys, company-reported productivity metrics, and human resources records.

Results were strongly positive across multiple dimensions. Productivity was maintained or improved at 95% of participating companies, and average revenue grew by 35% over the pilot period. Employee well-being improved markedly: burnout scores declined by 71%, and voluntary resignations fell by 57% compared to the prior year—a finding with significant implications for recruitment and retention costs. Work-life balance and job satisfaction scores rose substantially in weekly surveys.

The study's primary limitation is its non-randomized, opt-in design: companies that voluntarily joined the pilot may differ systematically from those that did not, potentially overstating benefits. Nonetheless, the breadth of the sample and the consistency of positive findings across sectors are notable. Ninety-two percent of companies indicated they planned to continue the four-day workweek after the pilot concluded.

The findings contribute substantial real-world evidence to the growing literature on alternative work arrangements, though replication across industries and geographies is needed.

---

### Example 2: Executive Summary for a Business Report

**Input:** "Write a one-page executive summary of this market analysis report for our leadership team. The full report covers: the global electric vehicle (EV) battery market is projected to reach $400B by 2030 (up from $48B in 2022), driven primarily by Asia-Pacific manufacturers. Key risks include lithium supply chain concentration (70% from three countries), rising raw material costs, and regulatory uncertainty in the US. Opportunities include solid-state battery technology (expected 2027–2030 commercialization), grid storage expansion, and EU battery regulation compliance consulting. We recommend: investing in solid-state battery startups, diversifying lithium sourcing, and building EU regulatory expertise."

**Output:**

---

#### Executive Summary: Global EV Battery Market Opportunity and Risk Analysis

**Bottom Line**
The global EV battery market presents a compelling growth opportunity—expanding from $48B (2022) to a projected $400B by 2030—but success requires proactive management of supply chain concentration risks and positioning ahead of next-generation technology shifts.

**Market Opportunity**
Growth is being driven primarily by Asia-Pacific manufacturers and accelerating EV adoption across major economies. Three adjacent opportunities merit near-term attention: (1) solid-state battery technology, projected to reach commercial scale between 2027 and 2030, which could redefine energy density and safety standards; (2) grid-scale energy storage, an emerging and rapidly expanding use case for battery technology; and (3) EU battery regulation compliance consulting, where new European mandates will create significant demand for expertise.

**Key Risks**
- **Supply chain concentration:** Approximately 70% of global lithium supply originates from just three countries, creating significant geopolitical and logistical exposure.
- **Raw material cost volatility:** Lithium, cobalt, and nickel prices have been highly variable, compressing margins across the value chain.
- **Regulatory uncertainty:** US federal policy on EV incentives and domestic content requirements remains in flux, affecting investment planning horizons.

**Recommendations**
1. Establish investment positions in solid-state battery startups ahead of the 2027–2030 commercialization window.
2. Diversify lithium sourcing through offtake agreements with suppliers in multiple geographies to reduce concentration risk.
3. Build internal EU battery regulatory expertise or acquire a consulting firm positioned in this space before demand peaks.

**Next Steps**
Review the full report's supply chain analysis (Section 3) and solid-state technology assessment (Section 5) for supporting data ahead of the Q3 strategy session.

---

### Example 3: Multi-Document Comparative Summary

**Input:** "Give me a brief comparative TL;DR of these two articles: Article A argues that remote work increases productivity by reducing commute stress and enabling deep focus. Article B argues that remote work decreases productivity due to collaboration friction, loneliness, and home distractions."

**Output:**

---

**Comparative TL;DR**

Both articles address remote work productivity but reach opposite conclusions based on which factors they emphasize.

- **Article A** focuses on individual cognitive work: reduced commute stress and fewer office interruptions enable sustained deep focus, boosting productivity for tasks done independently.
- **Article B** focuses on collaborative and social dimensions: remote work fragments communication, increases coordination overhead, and introduces home distractions, with loneliness further eroding motivation.

**The synthesis:** The two views are not necessarily contradictory—they may both be right for different types of work. Remote work likely benefits heads-down, individual-contributor roles more than roles requiring frequent real-time collaboration. Neither article engages seriously with this distinction.

---

## Best Practices
- Lead with the most important finding or conclusion—don't make the reader wait for the payoff
- Match the summary's technical level to the intended audience, not to the original document's level
- Preserve the original's hedging and uncertainty when it matters—"may reduce" is different from "reduces"
- When summarizing multiple sources, use consistent comparison criteria across all of them
- Flag what the summary excludes, especially for long, complex documents
- Use the same terminology as the original for key defined terms; don't rephrase technical concepts in ways that change meaning

## Common Mistakes
- **Copying introductory sentences:** Introductions are often throat-clearing; what the paper actually *found* is usually in the results or conclusion
- **Overstating certainty:** Adding confidence the original doesn't have ("the study proves" when the original says "suggests")
- **Under-representing limitations:** Omitting the caveats and limitations that qualify the main findings
- **Making the summary too long:** A summary that's 60% of the original hasn't been summarized—it's been lightly edited
- **Losing the structure:** Summarizing a complex document as a single paragraph when a structured breakdown (sections, bullets) would be clearer
- **Including your own opinions:** A summary reports what the source says, not what you think about it
- **Burying the main point:** Starting with background and methodology when the reader needs the conclusion first

## Tips & Tricks
- For long documents, read the abstract, introduction, and conclusion first to understand the shape of the argument, then read selectively
- Use the author's own section headings as a scaffold—they already tell you what they considered important
- Write the one-sentence core claim first; this disciplines everything else you include
- For bullet-point summaries, aim for each bullet to be independent and self-explanatory, not dependent on reading the others in sequence
- If a document has an existing executive summary or abstract, compare your summary against it—discrepancies are a signal to reread
- For meeting or transcript summaries, use a "decisions / actions / discussion" three-part structure rather than chronological order
- When asked for a TL;DR by a non-expert, eliminate all jargon and technical terms from the first sentence

## Related Skills
- [literature-reviewer](../../research/literature-reviewer/SKILL.md)
- [note-taker](../../productivity/note-taker/SKILL.md)
- [web-researcher](../../research/web-researcher/SKILL.md)
- [proofreader](../../writing/proofreader/SKILL.md)
