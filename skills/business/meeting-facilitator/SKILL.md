---
name: meeting-facilitator
description: "Use this skill when designing meeting agendas, facilitating team sessions, writing post-meeting notes, or improving meeting effectiveness. Trigger phrases: 'design an agenda for', 'facilitate a retrospective', 'write meeting notes for', 'how do I run a decision meeting', 'make our standups better'. Not for writing project plans, OKRs, or business requirements documents."
version: 1.0.0
author: community
tags: [business, meetings, facilitation, agenda, productivity]
license: MIT
---

# Meeting Facilitator

## Overview
This skill provides structured frameworks for designing effective meetings, facilitating common meeting types (standup, retrospective, planning, decision), capturing action items, and writing clear post-meeting notes. Good facilitation transforms meetings from time sinks into decision engines by ensuring every meeting has a clear purpose, the right participants, and defined outcomes.

## When to Use
- Designing an agenda for any team meeting
- Facilitating a sprint retrospective, planning session, or decision meeting
- Writing post-meeting notes and action items
- Diagnosing why your team's meetings feel unproductive
- Running a workshop with multiple stakeholders

## When NOT to Use
- Writing OKRs or quarterly plans (use okr-planner skill)
- Documenting business requirements (use business-analyst skill)
- Conducting user research interviews (use ux-researcher skill)

## Quick Reference
| Meeting Type | Duration | Key Output | Ideal Size |
|-------------|----------|-----------|------------|
| Daily standup | 15 min | Blocker visibility | 4–10 |
| Sprint planning | 2–4 hrs | Sprint backlog | 5–12 |
| Sprint retrospective | 60–90 min | Action items | 4–12 |
| Decision meeting | 30–60 min | Decision + owner | 3–8 |
| Weekly team sync | 30–60 min | Priorities aligned | 4–15 |
| Quarterly planning | Half day | OKRs / roadmap | 5–20 |
| 1:1 | 30 min | Relationship + unblocking | 2 |

## Instructions

### Step 1: Agenda Design Principles
Every meeting needs:
1. **Purpose**: One sentence: "We will decide X" or "We will plan Y"
2. **Outcomes**: What will be true at the end that wasn't true at the start?
3. **Participants**: Only people who need to be there (every extra person = more alignment cost)
4. **Time boxes**: Each agenda item has a time limit
5. **Pre-read**: Share materials 24h before; don't read slides in the meeting

**Agenda template:**
```
Meeting: [Title]
Date/Time: [Date] | [Duration]
Facilitator: [Name]
Goal: [One-sentence purpose]

Attendees: [Name (Role)] — mark D=Decider, I=Input, O=Observer

Pre-read: [Link to any documents]

Agenda:
1. [Item] — [Owner] — [Time]
2. [Item] — [Owner] — [Time]
3. Decisions made / Action items — Facilitator — 5 min

Expected outputs:
- [ ] Decision on X
- [ ] Action items assigned with owners and dates
```

### Step 2: Meeting Type Guides

**Daily Standup (15 min)**
Format: Each person answers (60 seconds max):
1. What did I complete yesterday?
2. What am I working on today?
3. Any blockers?

Facilitator rules:
- Start exactly on time; latecomers catch up async
- Park detailed problem-solving: "Let's take that offline after"
- End with blockers board review

---

**Sprint Retrospective (90 min)**
Goal: Improve team process, not just vent.

Agenda:
```
1. Set the stage — 10 min
   Ice-breaker: "Rate this sprint 1–5" (anonymous, use Mentimeter)

2. Gather data — 20 min
   Each person writes sticky notes for:
   - ✅ Went well
   - 🔴 Could improve
   - 💡 New ideas

3. Generate insights — 25 min
   Group stickies into themes; vote on top 3 themes

4. Decide what to do — 25 min
   For each top theme: what is ONE concrete action we commit to?
   Format: "We will [specific action] by [date], owned by [person]"

5. Close — 10 min
   Retro on the retro: "What was useful about this session?"
   Read back committed action items
```

---

**Decision Meeting (45 min)**
Use when a decision needs group input but risks being made in a vacuum.

Agenda:
```
1. Frame the decision — 5 min
   "We are here to decide: [specific question with clear options]"

2. Share context — 10 min
   Pre-read owner presents key information (data, constraints, tradeoffs)
   No new information introduced in meeting

3. Clarifying questions — 10 min
   Questions only — no advocacy yet

4. Discussion — 15 min
   Each stakeholder shares perspective (2 min max each)
   Decider listens; asks follow-up questions

5. Decision — 5 min
   Decider announces decision and rationale
   If no consensus: "I've heard all perspectives; here is the decision and why"
```

### Step 3: Facilitation Techniques

**For divergent discussions (generating ideas):**
- Silent brainstorm: everyone writes independently for 5 minutes before sharing
- Round-robin: each person shares one idea in turn; no interrupting
- "Yes, and..." rule: build on others' ideas before challenging them

**For convergent discussions (narrowing to a decision):**
- Dot voting: each person gets 3 votes; they place dots on preferred options
- Fist-to-five: 0 fist = "I'll block this", 5 fingers = "I love this"; go if avg ≥ 3
- DACI: Decider, Approvers, Contributors, Informed — clarify who decides

**For dysfunctional dynamics:**
- Dominant talker: "Let's hear from someone who hasn't spoken yet"
- Silent room: "Let's take 2 minutes to write thoughts before discussing"
- Off-topic detour: "That's important — let's park it on the parking lot board and return after"
- Circular debate: "We've heard two perspectives several times. Let's move to a decision."

### Step 4: Action Item Format
Every action item needs four elements:
```
WHO will do WHAT by WHEN [and how we'll know it's done]

Example:
- @Sarah will draft the Q3 roadmap slide deck by Friday June 14 [share in #product Slack]
- @Mike will get sign-off from Legal on the new ToS by EOD Monday [update the Notion doc]
- @Team: all engineers to complete security training by June 21 [completion tracked in LMS]
```

### Step 5: Post-Meeting Notes Format
```
# [Meeting Name] — [Date]

**Attendees:** [Name, Name, Name]
**Facilitator:** [Name]
**Note-taker:** [Name]

## Decisions Made
- [Decision 1]: [Context for why this decision was made]
- [Decision 2]: ...

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Action] | [Name] | [Date] | Open |

## Key Discussion Points
- [Topic 1]: [Brief summary of discussion]
- [Topic 2]: ...

## Parking Lot (topics to revisit)
- [Item] — [who is following up]

## Next Meeting
Date: [Date] | Pre-read needed: [Yes/No — what]
```

## Examples

### Example 1: Sprint Retrospective Agenda
**Context:** 8-person engineering team, end of 2-week sprint.

```
Sprint 24 Retrospective — June 14, 2:00–3:30 PM
Facilitator: Sarah (EM) | Tool: FigJam board

1. Check-in (10 min)
   Anonymous poll: "Rate this sprint 1–5 and share one word"
   Goal: Understand energy in the room before diving in

2. Gather data — "What do we want to talk about?" (20 min)
   Silent sticky writing (5 min), then share:
   - Green: What helped us ship well this sprint?
   - Red: What slowed us down or caused frustration?
   - Yellow: What experiment should we try next sprint?

3. Theme and vote (15 min)
   Group stickies; each person places 3 votes on most important themes
   Focus the next section on top 2–3 themes only

4. Actions (30 min)
   For each top theme:
   - What's the root cause? (5-Why drill)
   - What ONE change would help?
   - Who owns it? By when?
   Target: 2–3 committed action items maximum

5. Appreciations + close (15 min)
   Round of "I want to appreciate [person] for [specific thing] this sprint"
   Read back action items — confirm owners agree
```

**Output — post-retro actions:**
- @Dev: Move PR review from end-of-day to 10am daily block — starts Monday [owned by Dev]
- @Sarah: Schedule architecture review before next sprint planning — by June 18 [owned by Sarah]
- @Team: Define "definition of done" checklist for stories — workshop June 15 [owned by whole team]

---

### Example 2: Post-Meeting Notes — Product Decision Meeting

```
# Pricing Page Redesign — Go/No-Go Decision
Date: June 12, 2024 | Duration: 45 min
Attendees: Alex (CPO, Decider), Jamie (PM), Lee (Design), Sam (Engineering), Priya (Sales)
Facilitator: Jamie

## Decisions Made
- **GO on Pricing Page V2 redesign**: Alex approved moving forward with the 3-tier pricing
  display. Rationale: A/B test data shows 18% lift in trial starts with simplified pricing;
  risk of complexity outweighed by conversion opportunity.
- **Deferred**: Adding annual billing toggle deferred to V2.1 (not in current scope).
  Estimated 2 additional weeks of engineering; not worth delaying V2 launch.

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Finalize copy for all 3 pricing tiers | Jamie | June 17 | Open |
| Engineering estimate for V2 implementation | Sam | June 14 | Open |
| Sales enablement slide on new pricing | Priya | June 19 | Open |
| Legal review of "free trial" language | Jamie | June 17 | Open |

## Key Discussion Points
- Sales flagged that current pricing page confuses enterprise buyers — V2 addresses this
  with an explicit "Enterprise: Contact Us" CTA
- Engineering flagged that mobile layout will need an extra 3 days; accepted

## Parking Lot
- Annual billing discount strategy — revisit in July planning

## Next Meeting
Pricing V2 launch readiness check — June 24 | Pre-read: Engineering estimate doc
```

## Best Practices
- Send the agenda 24 hours before every meeting — no agenda, no meeting
- Assign a note-taker at the start; rotate the role across the team
- End every meeting 5 minutes early with a read-back of all action items
- Cancel any meeting where the outcome or purpose isn't clear
- The meeting owner and facilitator should be the same person (or handoff is explicit)
- Video on for remote meetings with fewer than 10 people — presence improves engagement

## Common Mistakes
- Scheduling 60 minutes by default — most meetings need 30
- Inviting everyone "just in case" — only invite people who contribute to the outcome
- Starting with status updates that could be async (use Slack updates instead)
- Making decisions without the decision-maker in the room
- No action items or owners — discussion happened but nothing changes
- Reading slide decks aloud in meetings — send as pre-read, use meeting time for discussion

## Tips & Tricks
- The "6-pager" (Amazon's format): pre-read narrative replaces presentation slides; meeting time = Q&A only
- "ELMO" signal (Enough, Let's Move On): team can call ELMO when a topic is going in circles
- Start retrospectives with data (sprint velocity, bug count) — grounds discussion in facts
- For large decisions, use the "write it down first" rule: decision-maker writes proposed decision before discussion; this prevents groupthink
- Async-first: if a decision can be made with a 5-minute Loom video + 24 hours of comment, do that instead of scheduling a meeting

## Related Skills
- [business-analyst](../../business/business-analyst/SKILL.md)
- [okr-planner](../../business/okr-planner/SKILL.md)
- [product-manager](../../business/product-manager/SKILL.md)
