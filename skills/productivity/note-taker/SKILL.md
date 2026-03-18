---
name: note-taker
description: "Use this skill when capturing, organizing, or restructuring notes from meetings, research, lectures, or brainstorms. Trigger phrases: 'take notes on this', 'organize my notes', 'summarize this meeting', 'structure these notes'. Do NOT use for formal minutes requiring legal accuracy or verbatim transcription."
version: 1.0.0
author: community
tags: [productivity, notes, organization, meetings, capture]
license: MIT
---

# Note Taker

## Overview
This skill converts raw, unstructured input—meeting transcripts, rough bullet dumps, recorded lecture notes, or scattered ideas—into clean, organized, and immediately useful notes. It applies consistent structure (decisions, action items, context, key points) so that notes are scannable and retrievable weeks later, not just immediately after the session. Output formats include meeting notes, research summaries, Cornell-style study notes, and structured brain-dump digests.

## When to Use
- Organizing notes captured during or after a meeting
- Structuring a brain dump or whiteboard session into organized sections
- Summarizing a long article, document, or video into key takeaways
- Creating study notes from a lecture or course material
- Cleaning up messy notes before sharing with a team
- Turning scattered thoughts into a coherent reference document

## When NOT to Use
- Verbatim transcription required for legal or compliance purposes
- Real-time live note-taking (requires a human in the session)
- Formal meeting minutes with parliamentary procedure (use a dedicated minutes format)
- Note-taking that requires access to proprietary real-time systems

## Quick Reference
| Task | Approach |
|------|----------|
| Meeting notes | Date + attendees → decisions → action items (owner, due date) → context/discussion |
| Brain dump | Cluster by theme → label clusters → convert to bullets → flag open questions |
| Research notes | Source + key claims → supporting evidence → counterarguments → implications |
| Study notes | Recall questions (left) → notes (right) → summary (bottom) — Cornell method |
| Book/article | Main thesis → 3–5 key arguments → notable quotes → personal takeaways |
| Action items | Bold owner name, specific task, due date: **Alice** — send proposal — by Friday |
| Decisions | Prefix with ✅ Decision: to distinguish from discussion points |

## Instructions

1. **Identify the note type.** Determine which format fits the input: meeting notes, research summary, study notes, or brain-dump digest. Each has a different structure. If unsure, ask or default to the meeting-notes format for collaborative contexts and the research-summary format for solo information capture.

2. **Extract the metadata first.** For meetings: date, time, attendees, and purpose. For articles/research: source title, author, date, and URL. For brain dumps: the topic or goal being explored. This metadata is often skipped and later regretted.

3. **Identify decisions, actions, and open questions.** These are the highest-value outputs from any meeting or work session. Pull them out explicitly and put them at the top of the notes or in a clearly labeled section. Action items must have: (a) a specific task, (b) one named owner, (c) a due date.

4. **Organize the remaining content by theme or chronology.** Group discussion points, research findings, or ideas under clear headings. Use parallel structure within each section. Prefer short, scannable bullets over dense paragraphs.

5. **Write a 2–5 sentence summary at the top.** Readers should be able to understand what happened/was captured in 30 seconds without reading the full document. This is especially valuable for people who weren't in the meeting.

6. **Flag ambiguities and open questions.** Any unresolved item, unclear decision, or "to be determined" should be labeled explicitly (e.g., ❓ Open question:) rather than buried in the notes body where it disappears.

7. **Apply consistent formatting.** Use markdown or the team's standard format: bold for owners and key terms, checkboxes for action items, horizontal rules between sections. Consistent formatting makes notes scannable across many documents.

8. **Review for completeness.** Before finalizing, check: Are all action items captured with owners and dates? Are decisions clearly labeled? Is the summary accurate? Would someone who wasn't present understand the context?

## Examples

### Example 1: Messy Meeting Notes → Structured Output

**Input:**
```
Met today with sarah and dev team. talked about the app launch. tom said we need to finalize the onboarding
flow by end of month. sarah thinks we should delay because QA found 3 bugs. one bug is critical (login broken
on android). marcus will look into the android bug. we decided to push launch to oct 15. sarah will update
the stakeholders. still need to figure out if we're doing a soft launch or full launch. marketing not in the
call. someone needs to loop them in. next meeting thursday.
```

**Output:**

---

#### Product Launch Sync — Meeting Notes

**Date:** [Today's date]
**Attendees:** Sarah, Tom, Marcus, Dev team
**Purpose:** App launch readiness review

---

##### Summary
The team decided to push the app launch to **October 15** due to three QA-identified bugs, including a critical Android login issue. Marcus will investigate the blocker; Sarah will notify stakeholders. The launch scope (soft vs. full) remains open and requires Marketing input.

---

##### ✅ Decisions
- Launch date moved to **October 15**

##### ☐ Action Items
| Owner | Task | Due |
|-------|------|-----|
| **Marcus** | Investigate and fix critical Android login bug | ASAP |
| **Sarah** | Update stakeholders on new launch date | EOD today |
| **TBD** | Loop in Marketing team to align on launch scope | Before Thursday |
| **All** | Reconvene Thursday to review bug status and finalize launch type | Thursday |

##### ❓ Open Questions
- Soft launch vs. full launch — decision pending Marketing input
- Who owns notifying Marketing? (not assigned in this meeting)

##### Discussion Notes
- QA identified 3 bugs total; 1 critical (Android login broken), 2 others not yet triaged
- Tom flagged end-of-month deadline for onboarding flow finalization — still stands
- Decision to delay was driven by Sarah's concern about shipping with a critical bug

---

### Example 2: Article Research Notes

**Input:** "Organize my notes from this article about sleep and productivity. Key things I captured: 'Sleep deprivation costs the US $411B/year (Rand study). 6 hours of sleep feels fine but causes same cognitive impairment as being drunk. Most people can't accurately self-assess their sleep deficit. Naps of 10-20 min boost alertness. Matthew Walker says no amount of caffeine fixes sleep debt. REM sleep is critical for creativity and emotional regulation. Companies with flexible work hours have better sleep outcomes. My takeaway: I should stop my 11pm meetings.'"

**Output:**

---

#### Research Notes: Sleep & Productivity

**Source:** [Article title — add when available]
**Captured:** [Date]
**Topic:** Impact of sleep on cognitive performance and workplace productivity

---

##### Summary
Sleep deprivation is a hidden productivity crisis: it impairs cognition as severely as alcohol, costs economies hundreds of billions annually, and cannot be offset by caffeine. REM sleep specifically drives creativity and emotional regulation. Flexible work policies meaningfully improve outcomes.

---

##### Key Claims & Evidence
- **Economic cost:** Sleep deprivation costs the US **$411 billion/year** (RAND Corporation study)
- **Cognitive impairment:** 6 hours of sleep produces the same cognitive deficits as being legally drunk — critically, people cannot self-assess this deficit accurately
- **Caffeine limitation:** Caffeine masks fatigue but does not restore cognitive function (Matthew Walker)
- **REM sleep functions:** Essential for creativity, problem-solving, and emotional regulation
- **Naps:** 10–20 minute naps measurably boost alertness; longer naps cause sleep inertia

##### Workplace Implications
- Employees with flexible start times (aligned to chronotypes) report better sleep and performance
- Standard 9-to-5 schedules disadvantage night-owl chronotypes

##### Counterarguments / Nuance
- Not captured in notes — worth researching: individual variation in sleep needs (short sleepers exist but are rare genetic outliers)

##### ❓ Open Questions
- What's the minimum effective sleep duration before cognitive impairment begins?
- Are there evidence-based workplace interventions beyond flexible hours?

##### Personal Takeaways
- Move 11pm meetings earlier — this is a direct sleep hygiene fix
- Re-evaluate "I'll sleep when I'm dead" productivity culture assumptions

---

## Best Practices
- Capture action items in real time, not retrospectively—they're hardest to reconstruct later
- Use a consistent note template so every document is instantly scannable
- Write the summary last, after reviewing the full notes—it will be more accurate
- One source of truth: don't split notes across multiple tools or documents
- Date-stamp everything; "recent" becomes meaningless in three weeks
- For recurring meetings, link to the previous meeting's notes and mark follow-ups as resolved or still open

## Common Mistakes
- **No action-item owners:** "Someone will handle the design" means no one will
- **Burying decisions in discussion:** If you have to read 500 words to find out what was decided, the notes have failed
- **Skipping the summary:** Notes without a summary force every reader to read everything every time
- **Raw transcript as notes:** Capturing everything said is not the same as capturing what matters
- **No follow-up on open questions:** Flag them, assign an owner, or they disappear forever
- **Inconsistent date/source metadata:** Makes notes irretrievable when searching later

## Tips & Tricks
- Use the Cornell Note method for studying: questions on the left, notes on the right, summary at bottom
- Create a personal shorthand for recurring tags: ✅ Decision, ☐ Action, ❓ Question, 💡 Idea, ⚠️ Risk
- Review and process notes within 24 hours while memory is still fresh
- For long meetings, take notes in 15-minute blocks to maintain structure throughout
- Use a "parking lot" section to capture tangents without derailing the main note flow
- Batch-process notes with the same template each time to build a searchable archive

## Related Skills
- [task-planner](../task-planner/SKILL.md)
- [meeting-facilitator](../meeting-facilitator/SKILL.md)
- [summarizer](../../writing/summarizer/SKILL.md)
- [journaling](../journaling/SKILL.md)
