---
name: citation-formatter
description: "Use this skill when formatting references, citations, or bibliographies in academic or professional styles. Trigger phrases: 'format this citation', 'create a bibliography', 'cite this source in APA', 'convert citation to MLA'. Do NOT use for finding or verifying the accuracy of sources—only for formatting known sources into a specified citation style."
version: 1.0.0
author: community
tags: [research, citations, bibliography, APA, MLA, Chicago, IEEE]
license: MIT
---

# Citation Formatter

## Overview
This skill produces correctly formatted citations and bibliographies in the major academic and professional citation styles: APA (7th ed.), MLA (9th ed.), Chicago (Notes-Bibliography and Author-Date), IEEE, Harvard, and Vancouver. Accurate citations are not optional in academic and professional writing—errors erode credibility and can constitute academic misconduct. This skill handles the tedious work of applying style-specific rules for punctuation, capitalization, author formatting, and element order so you can focus on the content.

## When to Use
- Formatting a reference list or bibliography for a paper, thesis, or report
- Converting citations from one style to another (e.g., APA to Chicago)
- Creating in-text citations and matching reference list entries
- Formatting citations for journal articles, books, book chapters, websites, reports, or datasets
- Generating an annotated bibliography with properly formatted citations
- Checking and correcting citation formatting in a draft document
- Producing a Works Cited page for an MLA-style paper

## When NOT to Use
- Finding or discovering sources on a topic (use `web-researcher` or `literature-reviewer` skill instead)
- Verifying whether a source actually exists or its content is accurate (use `fact-checker` skill instead)
- Evaluating the quality or relevance of sources
- Managing a large reference library (use dedicated tools like Zotero, Mendeley, or EndNote)

## Quick Reference
| Style | Primary Use | In-Text Format | Reference Order |
|-------|-------------|----------------|-----------------|
| APA 7 | Social sciences, psychology, education | (Author, Year) | Alphabetical by author surname |
| MLA 9 | Humanities, literature, language arts | (Author Page) | Alphabetical by author surname |
| Chicago NB | History, humanities | Footnotes/endnotes + bibliography | Alphabetical by author surname |
| Chicago AD | Social sciences | (Author Year) | Alphabetical by author surname |
| IEEE | Engineering, computer science | [Number] | Numbered in order of appearance |
| Vancouver | Medicine, health sciences | (Number) | Numbered in order of appearance |
| Harvard | General academic (UK/Australia) | (Author, Year) | Alphabetical by author surname |

## Instructions

1. **Identify the source type.** Citation rules vary significantly by source type. Determine whether you are citing:
   - Journal article (print or online, with or without DOI)
   - Book (single or multiple authors, edited volume)
   - Book chapter in an edited volume
   - Website or web page
   - Government or organizational report
   - Conference paper or proceedings
   - Thesis or dissertation
   - Dataset or software
   - Newspaper or magazine article
   - Personal communication or interview
   Gather all available metadata before formatting: authors, year, title, journal/publisher, volume, issue, pages, DOI/URL, and access date if required.

2. **Confirm the required citation style and edition.** Many styles have multiple editions with meaningful differences. Always use the current edition unless instructed otherwise: APA 7th (2020), MLA 9th (2021), Chicago 17th (2017). When in doubt, check with the publisher or instructor.

3. **Format author names correctly for the style.** This is one of the most common error sources:
   - **APA:** Last, F. M. for all authors; use & before final author; list up to 20 authors, then use ellipsis for more
   - **MLA:** First author is Last, First; subsequent authors are First Last; "et al." after author 2 for 3+ in some contexts
   - **Chicago NB (footnote):** First M. Last; Chicago Bibliography: Last, First M.
   - **IEEE:** F. M. Last for all authors; abbreviate given names

4. **Apply style-specific punctuation and capitalization rules.** Titles are especially tricky:
   - **APA:** Sentence case for article and book titles (capitalize only first word, proper nouns, and word after colon); italicize journal names and book titles in title case
   - **MLA:** Title case for all titles; italicize book and journal titles; put article titles in quotation marks
   - **Chicago:** Title case for all titles in bibliography; sentence case only in author-date references
   - **IEEE:** Sentence case for titles; do not italicize

5. **Format in-text citations or footnotes correctly.** Every style has different in-text citation conventions. Match your in-text citations precisely to your reference list entries—the same source must be identifiable in both locations.

6. **Include DOIs and URLs when required.** APA 7 requires DOIs for journal articles whenever available, formatted as `https://doi.org/xxxxx`. MLA requires URLs for online sources. Chicago and IEEE have their own URL conventions. Always hyperlink DOIs as full URLs.

7. **Format the reference list or bibliography.** Apply hanging indents (all styles except IEEE and Vancouver use hanging indents for the reference list). Confirm alphabetization (author-based styles) or numbering (numeric styles). Check that each entry type has all required elements.

8. **Verify the final output.** Cross-check against the official style manual or a trusted online tool (Purdue OWL, style manual websites) for any source types you are uncertain about. Pay special attention to: corporate/organizational authors, sources with no author, second editions, and translated works.

## Examples

### Example 1: Formatting the Same Source in Four Styles

**Input:** "Format this in APA 7, MLA 9, Chicago (Notes-Bibliography), and IEEE: A 2021 journal article titled 'Deep Learning Approaches to Natural Language Processing' by Sarah J. Kim and David R. Patel, published in the Journal of Artificial Intelligence Research, volume 72, pages 145–189, with DOI 10.1613/jair.1.12345."

**Output:**

---

**APA 7th Edition**

*Reference list entry:*
```
Kim, S. J., & Patel, D. R. (2021). Deep learning approaches to natural language processing. Journal of Artificial Intelligence Research, 72, 145–189. https://doi.org/10.1613/jair.1.12345
```

*In-text citation:*
```
(Kim & Patel, 2021)
```
or: `Kim and Patel (2021) demonstrated…`

---

**MLA 9th Edition**

*Works Cited entry:*
```
Kim, Sarah J., and David R. Patel. "Deep Learning Approaches to Natural Language Processing." Journal of Artificial Intelligence Research, vol. 72, 2021, pp. 145–189, https://doi.org/10.1613/jair.1.12345.
```

*In-text citation:*
```
(Kim and Patel 147)
```

---

**Chicago Notes-Bibliography (17th Edition)**

*Footnote (first citation):*
```
1. Sarah J. Kim and David R. Patel, "Deep Learning Approaches to Natural Language Processing," Journal of Artificial Intelligence Research 72 (2021): 147, https://doi.org/10.1613/jair.1.12345.
```

*Footnote (subsequent citations):*
```
2. Kim and Patel, "Deep Learning Approaches," 162.
```

*Bibliography entry:*
```
Kim, Sarah J., and David R. Patel. "Deep Learning Approaches to Natural Language Processing." Journal of Artificial Intelligence Research 72 (2021): 145–189. https://doi.org/10.1613/jair.1.12345.
```

---

**IEEE**

*Reference list entry:*
```
[1] S. J. Kim and D. R. Patel, "Deep learning approaches to natural language processing," J. Artif. Intell. Res., vol. 72, pp. 145–189, 2021, doi: 10.1613/jair.1.12345.
```

*In-text citation:*
```
[1]
```

---

### Example 2: Mixed Bibliography with Multiple Source Types

**Input:** "Create an APA 7 reference list for these three sources:
1. A 2019 book called 'The Alignment Problem' by Brian Christian, published by W. W. Norton & Company in New York.
2. A webpage: 'Bias in Facial Recognition Technology' by Joy Buolamwini, published on MIT Media Lab's website on March 15, 2018. URL: https://www.media.mit.edu/articles/bias-in-facial-recognition/
3. A chapter 'Fairness and Machine Learning' by Solon Barocas and Moritz Hardt, in an edited book 'Ethics of Artificial Intelligence' edited by S. Matthew Liao, published in 2020 by Oxford University Press, pages 202–234."

**Output:**

---

**Reference List**

Barocas, S., & Hardt, M. (2020). Fairness and machine learning. In S. M. Liao (Ed.), *Ethics of artificial intelligence* (pp. 202–234). Oxford University Press.

Buolamwini, J. (2018, March 15). *Bias in facial recognition technology*. MIT Media Lab. https://www.media.mit.edu/articles/bias-in-facial-recognition/

Christian, B. (2019). *The alignment problem*. W. W. Norton & Company.

---

**Formatting notes applied:**
- Entries are in alphabetical order by first author's surname (Barocas, Buolamwini, Christian)
- Book and periodical titles are italicized; article/chapter titles are in sentence case without italics or quotation marks
- Edited book chapter format: author(s), year, chapter title, "In" + editor initial(s) + surname + "(Ed.)," book title in italics, page range in parentheses, publisher
- Webpage includes author, date, italicized page title, site name, and URL (no "Retrieved from" required in APA 7 unless content may change)
- No issue numbers for books; no DOI needed for the book (none available) or the web page

---

### Example 3: Citation Style Conversion

**Input:** "Convert this MLA citation to APA 7: Smith, John A. 'The Effects of Sleep Deprivation on Cognitive Performance.' Sleep Research Quarterly, vol. 15, no. 3, 2022, pp. 45-67."

**Output:**

---

**Original (MLA 9):**
```
Smith, John A. "The Effects of Sleep Deprivation on Cognitive Performance." Sleep Research Quarterly, vol. 15, no. 3, 2022, pp. 45–67.
```

**Converted (APA 7):**
```
Smith, J. A. (2022). The effects of sleep deprivation on cognitive performance. Sleep Research Quarterly, 15(3), 45–67.
```

**Changes made:**
- Author: MLA "John A." → APA "J. A." (initials only)
- Year moved to immediately after author in parentheses
- Article title: Title case (MLA) → Sentence case (APA); removed quotation marks
- Journal name: Retained italics and title case (both styles italicize journal names in title case)
- Volume and issue: "vol. 15, no. 3" → "15(3)" — volume italicized, issue in parentheses not italicized
- Pages: "pp. 45–67" → "45–67" (APA omits "pp." for journal articles)
- Note: No DOI was provided in the original; if one exists, add `https://doi.org/xxxxx` at the end

---

## Best Practices
- Always gather all required metadata before starting—missing an issue number or publication year forces a return trip to the source
- Use hanging indents in your reference list: first line flush left, subsequent lines indented 0.5 inches
- DOIs should always be formatted as full hyperlinked URLs (`https://doi.org/xxx`), not just the number
- When an author is an organization (e.g., World Health Organization), use the full organization name; do not abbreviate in the reference list
- For works with no author, alphabetize by the first significant word of the title
- Double-check that every in-text citation has a matching reference list entry and vice versa
- When in doubt about a source type, consult the official style manual or Purdue OWL

## Common Mistakes
- **Wrong capitalization in titles:** Applying title case to article titles in APA (should be sentence case) or forgetting to capitalize proper nouns
- **Author initials vs. full names:** APA uses initials; MLA uses full given name for first author; Chicago uses full names
- **Missing DOI or URL:** APA 7 requires DOIs for journal articles; omitting them is a formatting error
- **Incorrect volume/issue format:** APA formats as `Volume(Issue)` with volume italicized; many writers italicize both or write them out
- **Ampersand vs. "and":** APA uses & in reference list and in-text for 2 authors; MLA uses "and"; never mix styles in one document
- **Alphabetization errors:** Last names starting with "Mc" or "Mac" should be alphabetized as spelled, not as if "Mac-" or "Mc-" were standardized
- **Access dates:** APA 7 generally does not require access dates for stable web content; MLA does not require them but recommends them; Chicago usually includes them

## Tips & Tricks
- Build a template document with correctly formatted citation shells for each source type you commonly use—fill in the details rather than rebuilding from scratch
- If you receive a DOI, paste it into `https://doi.org/` in a browser to verify it resolves to the correct source before submitting
- Zotero and Mendeley can auto-generate citations, but always proofread the output—they make errors, especially for unusual source types
- For Chicago footnotes, the first citation is full; subsequent citations of the same source use a shortened form (Author, "Short Title," page)
- When citing a tweet or social media post, use the author's real name in the citation if known; handle/username goes in brackets for some styles
- For no-author sources, APA moves the title to the author position; do not use "Anonymous" unless that is the published author name
- IEEE abbreviates journal names; the official IEEE abbreviation list is available on their website for accuracy

## Related Skills
- [literature-reviewer](../../research/literature-reviewer/SKILL.md)
- [academic-essay](../../writing/academic-essay/SKILL.md)
- [fact-checker](../../research/fact-checker/SKILL.md)
