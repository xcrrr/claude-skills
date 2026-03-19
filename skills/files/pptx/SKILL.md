---
name: pptx
description: "Use this skill when planning and scripting PowerPoint or Google Slides presentations with slide titles, bullet points, speaker notes, transitions, and narrative flow, or when converting documents into slide decks. Not for designing graphic assets or custom visual themes. Not for video or animation production."
version: 1.0.0
author: community
tags: [files, presentations, powerpoint, pptx, slides]
license: MIT
---

# PPTX

## Overview
This skill covers the design, scripting, and structuring of PowerPoint-compatible presentations (.pptx) and Google Slides decks. It helps teams translate outlines, documents, or briefs into compelling slide structures with a clear narrative arc, properly scoped bullet points, effective data visualization guidance, and complete speaker notes. This skill applies to all presentation types: executive briefings, investor pitch decks, technical deep dives, training materials, project status updates, and conference talks. Outputs can be descriptions for human implementors or structured scripts for programmatic generation using `python-pptx`.

## When to Use
- Converting a document, report, or brief into a slide deck
- Designing a new presentation from an outline or topic description
- Writing speaker notes for an existing slide structure
- Creating a narrative arc and story structure for a pitch or executive presentation
- Planning a training or onboarding presentation with learning objectives
- Scripting a conference talk structure with timing guidance
- Designing a template slide structure for a recurring presentation type

## When NOT to Use
- Designing custom graphic assets, icons, or illustrations (use design tools like Figma)
- Creating custom animation sequences or video presentations (use video production tools)
- Building interactive dashboards embedded in presentations (use dashboard tools)
- Generating DOCX reports (use docx skill)
- Detailed financial modeling that belongs in a spreadsheet (use xlsx skill)

## Quick Reference
| Task | Approach |
|------|----------|
| Structure a narrative | Use the "Problem → Insight → Solution → Call to Action" framework |
| Scope bullet points | Max 5 bullets per slide; each bullet max 10 words; one idea per bullet |
| Write speaker notes | Full sentences; include transitions, emphasis cues, and timing guidance |
| Design data slides | One chart per slide; title is the insight, not the chart type |
| Create agenda slide | List section titles with timing; use visual section dividers between parts |
| Plan slide count | Rule of thumb: 1–2 slides per minute of speaking time |
| Add section dividers | Full-bleed color or image slide with section title only; no bullets |

## Instructions

1. **Define the presentation goal and audience** — Answer three questions before writing any slides: (a) What is the single most important thing the audience should remember? (b) What decision or action should the audience take after this presentation? (c) What does the audience already know and what do they need to learn? These answers shape every slide.

2. **Choose a narrative structure** — Select the framework that fits the goal:
   - **Problem → Solution → Call to Action**: Best for sales, pitches, and proposals
   - **Situation → Complication → Resolution (SCR)**: Best for executive briefings and recommendations
   - **Learning Objectives → Content → Summary → Quiz**: Best for training and education
   - **Context → Data → Insight → Implication**: Best for analytical and data-driven presentations
   - **Timeline narrative**: Best for project status and retrospectives

3. **Create the outline first** — List each slide as a one-line title. The slide titles alone should tell the story — if you read only the titles in sequence, the argument should be clear. Review and refine the title sequence before writing any slide content.

4. **Scope each slide to one idea** — Each slide should have exactly one key message. If a slide needs two points, split it into two slides. The rule of thumb: if the title doesn't clearly state the slide's point, the slide content probably covers too much.

5. **Write bullet points** — Apply the "5×10 rule": maximum 5 bullets per slide, maximum 10 words per bullet. Bullets should be parallel in grammatical structure (all verb phrases, or all noun phrases — not mixed). Lead with the most important bullet.

6. **Design data visualization slides** — For each chart or data visual: (a) write the title as the insight ("Revenue grew 40% YoY in Q4" not "Q4 Revenue Chart"), (b) specify the chart type and why (bar for comparison, line for trends, scatter for correlation), (c) annotate the key data point directly on the chart, (d) simplify — remove gridlines, legends where possible, and use color to highlight only the key series.

7. **Write complete speaker notes** — For each slide, write notes that include: a transition from the previous slide, the key point to emphasize verbally, any statistics or anecdotes not on the slide, anticipated questions, and timing cue (e.g., "Spend 2 minutes here"). Speaker notes should be complete enough for a presenter who hasn't rehearsed to deliver successfully.

8. **Add section dividers** — Between major sections, insert a section divider slide: full-bleed background color or image, section title in large text, and optional section number. These give the audience a cognitive reset and signal a topic shift.

9. **Plan the opening and closing slides** — The opening should capture attention in the first 30 seconds: a striking statistic, a provocative question, or a brief story. The closing should restate the key message and include a specific, clear call to action — not "questions?" but the decision or next step you want.

10. **Review for visual consistency** — Specify: consistent font sizes for each text level across all slides, consistent color usage (only use your color palette), alignment (left-align text for readability, center for titles and data labels), and whitespace (leave at least 20% of each slide empty to avoid clutter).

## Examples

### Example 1: 10-Slide Company Overview Deck
**Input:** A B2B SaaS company (DataFlow, automated data pipeline tool) needs a 10-slide company overview for sales meetings with potential enterprise customers.

**Output:**

**Slide structure:**
```
SLIDE 1 — Cover
  Title: "DataFlow: Automate Your Data Pipelines in Hours, Not Months"
  Subtitle: Company Overview | [Month Year]
  Visual: Clean hero image or abstract data flow graphic
  Speaker notes: "Start by asking: how long does it currently take your team to build a new data pipeline?"

SLIDE 2 — The Problem
  Title: "Data Teams Spend 70% of Their Time on Pipeline Maintenance"
  Bullets:
    • Fragile hand-coded pipelines break on every schema change
    • New pipeline takes 4–8 weeks to build and test
    • Data engineers can't focus on strategic analysis work
  Speaker notes: "This is the number one complaint we hear from data teams. Before DataFlow, your engineers are plumbers, not architects."

SLIDE 3 — The Cost of the Status Quo
  Title: "Pipeline Downtime Costs $500K per Year for a Typical 50-Person Data Team"
  Visual: Bar chart showing time breakdown (maintenance vs new builds vs strategic work)
  Speaker notes: "We commissioned a study of 200 data teams. The maintenance burden is almost always underestimated."

SLIDE 4 — [Section Divider]
  Title: "Introducing DataFlow"
  Background: Brand color full-bleed

SLIDE 5 — The Solution
  Title: "DataFlow Builds, Tests, and Heals Your Pipelines Automatically"
  Bullets:
    • Visual drag-and-drop pipeline builder — no code required
    • AI-powered schema drift detection and auto-repair
    • Runs on your cloud (AWS, GCP, Azure) — no data leaves your environment
  Speaker notes: "Three minutes to show the product. Open the live demo here."

SLIDE 6 — How It Works
  Title: "From Data Source to Dashboard in 4 Steps"
  Visual: 4-step process diagram (Connect → Map → Deploy → Monitor)
  Speaker notes: "Walk through each step. Emphasize step 4 — the monitoring dashboard is what customers love most."

SLIDE 7 — Key Differentiators
  Title: "Why DataFlow vs. Alternatives"
  Visual: Comparison table — DataFlow vs. Fivetran vs. Airbyte vs. custom code
  Columns: Feature | DataFlow | Fivetran | Airbyte | Custom
  Speaker notes: "Don't be defensive about competitors. Acknowledge where each is strong, then show where we win."

SLIDE 8 — Customer Results
  Title: "Customers Cut Pipeline Build Time by 80% in the First 30 Days"
  Three customer callouts (logo + one-line quote + key metric each):
    • Acme Corp: "Deployed 40 pipelines in the first week." — 80% time savings
    • Beta Inc: "We retired our custom ETL after 2 weeks." — $2M annual savings
    • Gamma Ltd: "Best ROI of any data tool we've bought." — 6-week payback
  Speaker notes: "Ask if they know any of these companies. Offer reference calls."

SLIDE 9 — Pricing and Packages
  Title: "Transparent Pricing That Scales With Your Data"
  Table: Starter | Growth | Enterprise
  Rows: Price, Connectors, Users, SLA, Support
  Speaker notes: "Don't linger here — offer to send a detailed pricing sheet after the call."

SLIDE 10 — Next Steps
  Title: "Start Your Free 14-Day Trial Today"
  Bullets:
    • Trial includes full Enterprise features
    • Dedicated onboarding engineer for setup
    • Decision in 14 days or we extend the trial — no pressure
  CTA box: "Try free at dataflow.io/trial"
  Speaker notes: "Ask directly: 'Would it be valuable to run a proof of concept with one of your real pipelines this week?'"
```

### Example 2: 5-Slide Project Status Update
**Input:** An engineering team needs a 5-slide project status update for a weekly exec stakeholder meeting on a mobile app redesign project.

**Output:**

**Slide structure:**
```
SLIDE 1 — Executive Summary
  Title: "Mobile Redesign: On Track for March 15 Launch | 3 Risks to Monitor"
  Dashboard layout (4 boxes):
    Box 1: Overall Status: 🟢 ON TRACK
    Box 2: Budget: 🟡 92% of allocation used at 78% completion
    Box 3: Timeline: 🟢 Week 8 of 12
    Box 4: Risks: 🔴 3 open risks (1 High, 2 Medium)
  Speaker notes: "3 minutes max. Execs only need the status boxes and then we go to risks."

SLIDE 2 — Completed This Week
  Title: "3 Milestones Delivered This Week"
  Bullets:
    • ✅ User authentication redesign shipped to staging (March 1)
    • ✅ A/B test framework integrated with analytics stack
    • ✅ Accessibility audit completed — 94/100 WCAG score
  Speaker notes: "Keep this to 60 seconds. Wins first, then move to blockers."

SLIDE 3 — Next 2 Weeks
  Title: "Payment Flow and Notifications Are the Critical Path"
  Visual: Simplified Gantt or timeline for weeks 9–10
  Bullets:
    • Week 9: Payment flow UX testing (owner: Sarah) — critical path
    • Week 9: Push notification system — integration testing begins
    • Week 10: Beta launch to 500 internal testers
  Speaker notes: "Payment flow is the make-or-break item. Flag if Sarah's team needs additional resources."

SLIDE 4 — Risks and Decisions Needed
  Title: "1 High-Priority Decision Needed from Leadership"
  Risk table:
    | Risk | Severity | Owner | Decision Needed |
    | Payment provider API rate limit | 🔴 High | Dev Lead | Upgrade plan ($8K/mo) or redesign caching layer (2 weeks delay) |
    | iOS 18 beta compatibility | 🟡 Med | Mobile Team | None — monitoring |
    | QA contractor availability | 🟡 Med | PM | Approve backup contractor ($15K) by Thursday |
  Speaker notes: "Spend 3 minutes here. Get verbal approval on the payment provider decision today."

SLIDE 5 — Key Metrics Trend
  Title: "Test Coverage at 84% — Up from 61% Last Month"
  Visual: Line chart — 3 metrics over 8 weeks: Test Coverage %, Build Success Rate, Bug Backlog
  Speaker notes: "Quality trending well. The bug backlog spike in week 5 was from the auth redesign — now resolved."
```

## Best Practices
- Slide titles should be complete sentences that state the key point, not topic labels
- Every data chart needs a title that states the insight, not just the metric name
- Speaker notes should be full sentences at normal speaking pace — test by reading aloud
- Use three colors maximum in the entire deck — brand primary, secondary, and one accent
- Leave 20% whitespace on every slide — crowded slides signal rushed thinking
- Section dividers reset audience attention — use them between every major topic shift
- The last slide should show the call to action, not a "Thank You" or "Questions?" placeholder

## Common Mistakes
- Too many bullets per slide — if it won't fit in the slide title, split the slide
- Writing speaker notes as bullets instead of prose — bullets are hard to read while speaking
- Using chart titles like "Q4 Revenue" instead of "Q4 Revenue Grew 40% Driven by Enterprise"
- Inconsistent font sizes — audience perceives hierarchy from size; randomizing it destroys clarity
- Starting with company history — audiences want to know "why does this matter to me?" first
- Ending with "Questions?" slide — end with the key message and call to action instead
- Animation overload — transitions and animations should enhance comprehension, not entertain

## Tips & Tricks
- The "billboard test": if someone driving past a billboard could read your slide in 3 seconds, it's well-scoped
- Use a dark background for evening or auditorium presentations; light background for daylight/meeting rooms
- `python-pptx` can generate data-driven decks from templates — great for weekly automated reports
- Google Slides' "Presenter view" shows speaker notes on your screen without showing them on the projector
- Record yourself doing a practice run — if you stumble on a slide, the content needs simplification
- Duplicate your deck and delete all bullets — if the slide titles alone don't tell the story, revise them
- For investor pitches, follow the Sequoia pitch deck structure: Problem → Solution → Why Now → Market → Product → Team → Traction → Financials → Ask

## Related Skills
- [docx](../docx/SKILL.md)
- [pdf](../pdf/SKILL.md)
