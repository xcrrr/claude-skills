---
name: task-planner
description: "Use this skill when breaking down projects, planning a week, or turning vague goals into concrete action steps. Trigger phrases: 'help me plan my week', 'break this project into tasks', 'create an action plan for', 'prioritize my to-do list'. Do NOT use for long-term strategic roadmaps or OKR setting."
version: 1.0.0
author: community
tags: [productivity, planning, tasks, time-management, GTD]
license: MIT
---

# Task Planner

## Overview
This skill transforms fuzzy goals, messy to-do lists, and overwhelming projects into clear, prioritized, time-bound action plans. It applies proven frameworks—GTD, time-blocking, MoSCoW prioritization, and Eisenhower matrix—to produce output you can act on immediately. Whether you need a structured weekly plan, a project breakdown with dependencies, or a quick reprioritization of your backlog, this skill delivers a concrete list with owners, deadlines, and next steps—not just generic advice.

## When to Use
- Planning your week or day with competing priorities
- Breaking a large project into milestones and tasks
- Turning meeting notes or brainstorm outputs into action items
- Reprioritizing an overwhelmed to-do list
- Unblocking yourself when a project feels too big to start
- Assigning tasks across a team with clear owners

## When NOT to Use
- Long-term strategic planning or roadmapping (use `okr-planner` skill instead)
- Scheduling appointments or calendar management requiring real-time data
- Project management tool setup (Jira, Asana, Linear configuration)
- Tasks requiring domain expertise to estimate (use an expert for sizing)

## Quick Reference
| Task | Approach |
|------|----------|
| Weekly planning | Dump all tasks → categorize by project → time-block each day |
| Project breakdown | Define done → list milestones → list tasks per milestone → identify dependencies |
| Prioritization | Apply MoSCoW (Must/Should/Could/Won't) or Eisenhower (Urgent/Important matrix) |
| Overwhelmed list | Batch similar tasks → delete/defer low-value items → pick 3 MIT (Most Important Tasks) |
| Estimating effort | Use T-shirt sizes (S/M/L/XL) or story points; always add 25% buffer |
| Stuck on a task | Break it into the smallest possible next physical action |
| Team tasks | Assign one owner per task; include due date and success criteria |

## Instructions

1. **Capture everything first.** Before organizing, do a full brain dump of every task, commitment, and idea related to the goal. Don't filter—just list. This prevents important items from being missed during planning and reduces mental overhead.

2. **Clarify each item.** For each task, ask: What is the desired outcome? What is the very next physical action required? Is this actually actionable, or is it a project (multi-step)? Convert vague entries like "deal with website" into specific actions like "email designer with feedback by Thursday."

3. **Apply a prioritization framework.** Choose one method based on context:
   - **Eisenhower Matrix:** Sort tasks into Urgent+Important (do now), Important+Not Urgent (schedule), Urgent+Not Important (delegate), Neither (delete).
   - **MoSCoW:** Must have, Should have, Could have, Won't have for this period.
   - **Impact vs. Effort:** 2×2 grid to find quick wins (high impact, low effort) and avoid time sinks.

4. **Group tasks into categories or projects.** Cluster related tasks so context-switching is minimized. Label each cluster (e.g., "Client A deliverables," "Personal admin," "Learning & development").

5. **Estimate effort and assign deadlines.** Give each task a time estimate. Use T-shirt sizing (S = <30 min, M = 30–90 min, L = half day, XL = full day+). Assign a due date or time block. Be honest—underestimating is the #1 cause of failed plans.

6. **Identify dependencies and blockers.** Flag tasks that cannot start until another is complete. Highlight anything blocked by a third party—these need follow-up actions added to the plan.

7. **Build the daily or weekly schedule.** Slot tasks into time blocks matching your energy levels: deep work (complex tasks) in your peak hours, admin and communication in low-energy slots. Leave 20% of each day as buffer for unexpected work.

8. **Define the "done" criteria.** For each major task or milestone, write one sentence describing what success looks like. This prevents scope creep and makes it easy to know when something is truly complete.

9. **Review and commit.** Do a final pass: Is the total time realistic? Are Must-do tasks protected from interruption? Identify the three Most Important Tasks (MIT) for the day. Share the plan with stakeholders if applicable.

## Examples

### Example 1: Weekly Planning Session

**Input:** "Help me plan my week. I need to finish the Q3 marketing report, prep for a Thursday client call, respond to a backlog of 40 emails, work on my side project (building a landing page), and I have three hours of meetings already blocked. It's Monday morning."

**Output:**

---

#### Weekly Plan: Mon–Fri

**3 Most Important Tasks (MIT) for the week:**
1. Complete and submit Q3 marketing report (due Friday)
2. Prepare and deliver Thursday client call
3. Ship v1 landing page for side project

---

##### Monday
- **9:00–11:00** — Deep work: Draft Q3 report outline + sections 1–2
- **11:00–11:30** — Email triage: process inbox, flag action items, archive/delete
- **11:30–12:00** — Respond to top 10 highest-priority emails
- **1:00–3:00** — Existing meetings (blocked)
- **3:00–4:30** — Side project: Set up landing page structure + copy outline
- **4:30–5:00** — Plan Tuesday, clear inbox to 20

##### Tuesday
- **9:00–11:30** — Deep work: Q3 report sections 3–4
- **11:30–12:00** — Email batch 2 (10 emails)
- **1:00–2:30** — Side project: Build landing page hero + CTA
- **2:30–3:30** — Meetings (if any)
- **3:30–5:00** — Q3 report: data review and charts

##### Wednesday
- **9:00–10:30** — Deep work: Q3 report final section + executive summary
- **10:30–11:30** — Client call prep: review account history, list agenda items, prepare 3 key questions
- **1:00–2:00** — Side project: Landing page design pass + mobile review
- **2:00–3:30** — Email batch 3 (remaining backlog)
- **3:30–5:00** — Buffer / Q3 report first edit

##### Thursday
- **9:00–10:00** — Q3 report: final edits and formatting
- **10:00–11:00** — Existing meeting
- **11:00–12:00** — Client call prep: rehearse talking points
- **2:00–3:00** — **Client call** ← protected block
- **3:00–4:00** — Post-call: notes, follow-ups, action items
- **4:00–5:00** — Side project: connect form, test, publish v1

##### Friday
- **9:00–10:00** — Final review and submit Q3 report
- **10:00–11:00** — Respond to any remaining emails
- **11:00–12:00** — Weekly review: what shipped, what didn't, plan next week
- **Afternoon** — Buffer / low-priority tasks / learning

**Tasks deferred to next week:** Remaining ~20 low-priority emails (star and batch)

---

### Example 2: Project Breakdown

**Input:** "Break down this project into tasks: launch a company podcast. We have no equipment yet and want to publish episode 1 in 6 weeks."

**Output:**

---

#### Podcast Launch: 6-Week Action Plan

**Definition of Done:** Episode 1 published on Spotify, Apple Podcasts, and the company website with at least 50 listens in the first week.

---

##### Milestone 1: Foundation (Week 1)
| Task | Owner | Effort | Due |
|------|-------|--------|-----|
| Define show format (interview/solo/panel), episode length, release cadence | Team | M | Wed W1 |
| Write show concept doc: target audience, positioning, 3 competitor shows | Content lead | M | Wed W1 |
| Research and select podcast hosting platform (Buzzsprout/Transistor/Anchor) | Ops | S | Fri W1 |
| Draft episode 1 topic and guest list (if interview format) | Host | S | Fri W1 |

##### Milestone 2: Equipment & Setup (Week 2)
| Task | Owner | Effort | Due |
|------|-------|--------|-----|
| Purchase microphone, audio interface, headphones, pop filter | Ops | S | Mon W2 |
| Set up recording space (acoustic treatment basics) | Ops | M | Wed W2 |
| Install and configure recording software (Audacity/Descript/Riverside) | Ops | S | Wed W2 |
| Create podcast hosting account, configure RSS feed | Ops | S | Fri W2 |

##### Milestone 3: Content Production (Weeks 3–4)
| Task | Owner | Effort | Due |
|------|-------|--------|-----|
| Confirm episode 1 guest + schedule recording date | Host | S | Mon W3 |
| Write episode 1 script/outline and interview questions | Host | L | Wed W3 |
| Record episode 1 | Host + Guest | M | Fri W3 |
| Edit audio: remove filler, normalize levels, add intro/outro music | Editor | XL | Wed W4 |
| Write show notes and episode description (SEO-optimized) | Content lead | M | Thu W4 |

##### Milestone 4: Distribution & Launch (Weeks 5–6)
| Task | Owner | Effort | Due |
|------|-------|--------|-----|
| Design podcast cover art (3000×3000px, iTunes spec) | Designer | L | Mon W5 |
| Record 30-sec trailer for platform listings | Host | S | Tue W5 |
| Submit to Apple Podcasts, Spotify, Google Podcasts | Ops | M | Wed W5 |
| Create website landing page for the show | Dev/Content | L | Fri W5 |
| Write launch announcement (email + social) | Marketing | M | Mon W6 |
| Publish episode 1 + press send on launch campaign | All | S | Wed W6 |
| Monitor analytics; send follow-up to listeners | Marketing | S | Fri W6 |

**Dependencies:** Equipment delivery (Milestone 2) must complete before recording (Milestone 3). Hosting setup must be done before distribution submissions (Milestone 4).

---

## Best Practices
- Always capture before organizing—don't filter during the brain dump phase
- Name one and only one owner per task; shared ownership means no ownership
- Write tasks as verb phrases: "Send proposal to client" not "Proposal"
- Protect deep-work blocks from meetings—schedule meetings in late morning or afternoon
- Review and update your plan every morning (5 min) and every Friday (30 min)
- Identify your 3 MITs each day; don't add a 4th until all 3 are done

## Common Mistakes
- **Planning to 100% capacity:** Always leave 20–30% buffer; unplanned work always arrives
- **Vague tasks:** "Work on report" is not actionable; "Write introduction section of Q3 report" is
- **No due dates:** Tasks without deadlines drift indefinitely
- **Ignoring energy levels:** Scheduling deep work during your low-energy afternoon leads to poor output
- **Skipping the weekly review:** Without it, the plan drifts and old tasks pile up invisibly
- **Too many MITs:** Three is the maximum; more than that and nothing gets done properly

## Tips & Tricks
- Use the "2-minute rule" (GTD): if a task takes less than 2 minutes, do it now instead of adding it to the list
- Batch similar tasks (all emails, all calls, all reviews) to minimize context-switching cost
- Time-block your calendar, not just your to-do list—what gets scheduled gets done
- For recurring tasks, create a template checklist once and reuse it
- Use "waiting for" as a task category to track things blocked on other people
- Write tomorrow's plan at the end of today, not at the start of tomorrow—it reduces morning friction

## Related Skills
- [note-taker](../note-taker/SKILL.md)
- [decision-maker](../decision-maker/SKILL.md)
- [okr-planner](../okr-planner/SKILL.md)
- [meeting-facilitator](../meeting-facilitator/SKILL.md)
