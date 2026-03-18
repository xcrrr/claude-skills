---
name: okr-planner
description: "Use this skill when defining company, team, or individual OKRs, running a quarterly planning process, scoring key results, or cascading goals across an organization. Trigger phrases: 'write OKRs for', 'help me set quarterly goals', 'is this a good key result', 'how do we cascade OKRs', 'score my OKRs'. Not for writing job descriptions, building project plans, or creating financial budgets."
version: 1.0.0
author: community
tags: [business, okr, goals, planning, strategy]
license: MIT
---

# OKR Planner

## Overview
This skill provides end-to-end guidance on the OKR (Objectives and Key Results) framework—from writing crisp objectives and measurable key results through the quarterly planning cadence, cascading across organizational levels, tracking progress, and scoring at quarter end. OKRs align effort with strategy, create transparency, and separate the aspiration (Objective) from the measurement of success (Key Results).

## When to Use
- Setting company, team, or individual goals for a quarter or year
- Evaluating whether existing OKRs are well-written and measurable
- Cascading company OKRs down to team or individual level
- Running a quarterly planning or review session
- Coaching a team on the OKR framework
- Mid-quarter check-in and progress scoring

## When NOT to Use
- Building a full project plan with tasks and deadlines (use a project management tool)
- Writing a business strategy document (OKRs implement strategy; they don't define it)
- Creating job descriptions or performance review templates
- Financial budgeting or headcount planning

## Quick Reference
| Element | Format | Quality Check |
|---------|--------|---------------|
| Objective | Inspirational, qualitative, verb-led direction | Does it inspire action? Is it clear without context? |
| Key Result | Metric with baseline → target | Is it measurable? Can you prove it at quarter end? |
| OKR count | 3–5 Objectives; 2–5 KRs each | More than 5 Objectives = no focus |
| Timeframe | Quarterly (most common) or annual | Annual Objectives, quarterly KRs works well |
| Cadence | Weekly check-in, monthly review, quarterly score | No cadence = OKRs die |
| Score | 0.0–1.0 (0.7 = success; 1.0 = sandbagging) | Avg score should be ~0.7 |
| Levels | Company → Dept/Team → Individual (optional) | Team KRs should roll up to company Objectives |

## Instructions

### Step 1: Understand the OKR Framework

**The anatomy of an OKR:**
```
OBJECTIVE: What we want to achieve (qualitative, inspiring, directional)
  Key Result 1: How we measure progress toward the Objective (quantitative)
  Key Result 2: ...
  Key Result 3: ...
```

**The relationship:** "We will [Objective] as measured by [Key Results]."

**Good vs bad Key Results:**
| Bad KR | Problem | Better KR |
|--------|---------|-----------|
| "Improve customer satisfaction" | Not measurable | "Increase NPS from 32 to 50" |
| "Launch new onboarding flow" | Output, not outcome | "Reduce time-to-first-value from 14 days to 5 days" |
| "Hold 10 customer meetings" | Activity, not result | "Convert 8 of 10 enterprise trials to paid within 30 days" |
| "Grow revenue" | No baseline or target | "Grow MRR from $180K to $250K" |
| "Be the best in the market" | Not measurable | "Achieve #1 G2 rating in our category by Q4" |

**KR quality criteria (all must be true):**
- ✅ Measurable: a number you can look up at quarter end
- ✅ Specific: clear baseline and target
- ✅ Outcome-focused: describes a change in the world, not a task completed
- ✅ Ambitious but achievable: 0.7 probability of hitting it if you work hard
- ✅ Owned: one team/person is clearly responsible

### Step 2: Write Objectives

**An Objective must be:**
- **Qualitative**: Describes a direction or aspiration, not a number
- **Inspiring**: Motivates the team to care about achieving it
- **Clear**: Understandable without additional context
- **Achievable within the timeframe**: Not "become the world's largest company in Q1"
- **Verb-led**: Starts with an action word

**Objective formula:**
`[Verb] + [What we're improving/building/achieving] + [Context/Qualifier]`

**Examples by level:**

**Company-level:**
- "Establish ourselves as the undisputed leader in AI-powered legal tech"
- "Dramatically improve the new user experience to drive sustainable growth"
- "Build a world-class go-to-market engine that scales"
- "Achieve financial sustainability while maintaining quality"

**Team-level (Engineering):**
- "Ship a platform that engineering teams love to use every day"
- "Eliminate the technical debt blocking our next growth phase"
- "Build the infrastructure to support 10× our current user load"

**Team-level (Sales):**
- "Build a predictable, repeatable enterprise sales motion"
- "Transform our customer onboarding into a competitive advantage"

**Individual:**
- "Become a trusted technical advisor to our enterprise customers"
- "Level up my skills to take on a senior engineer role"

### Step 3: Write Key Results

**Key Result formula:**
`[Metric] from [baseline] to [target] by [date]`

Or: `Achieve [metric] ≥ [target] by [date]`

**Baseline is critical**: Without a baseline, you can't measure progress.

**Key Result examples for "Dramatically improve the new user experience":**
- KR1: Increase 30-day user activation rate from 42% to 65%
- KR2: Reduce time-to-first-value from 14 days to 5 days
- KR3: Achieve a new user NPS score of ≥ 45 (currently 28)
- KR4: Reduce new-user support tickets in first 30 days by 40%

**Key Result examples for "Build a predictable, repeatable enterprise sales motion":**
- KR1: Increase average sales cycle from 90 days to under 60 days
- KR2: Grow pipeline coverage ratio from 2.1× to 3.5× quota
- KR3: Achieve 85% of enterprise quota ($2.1M bookings)
- KR4: Onboard and ramp 3 enterprise AEs to 80% of quota by Q3

### Step 4: Cascade OKRs Across the Organization

**Cascading logic:**
1. Company OKRs set the organizational direction
2. Department/team OKRs contribute to one or more Company Objectives
3. Individual OKRs (optional) align to team OKRs

**Important:** Teams should *translate* company objectives, not just copy them. A team's OKR should reflect their specific contribution.

**Example cascade:**

```
COMPANY OBJECTIVE: Establish ourselves as the undisputed leader in AI-powered legal tech
  Company KR1: Reach $5M ARR by Q4
  Company KR2: Achieve NPS of 60+ across our customer base
  Company KR3: Win 3 named enterprise accounts (AmLaw 100)

  ↓ Translates to ↓

ENGINEERING TEAM OBJECTIVE: Build a platform that wins enterprise-grade deals
  Eng KR1: Launch enterprise SSO/SAML integration by May 15
  Eng KR2: Achieve 99.95% platform uptime SLA (currently 99.7%)
  Eng KR3: Reduce P95 API response time from 800ms to under 300ms

SALES TEAM OBJECTIVE: Land and expand three marquee enterprise accounts
  Sales KR1: Close 3 AmLaw 100 accounts worth $600K+ combined ARR
  Sales KR2: Expand existing enterprise accounts by 35% through upsell
  Sales KR3: Build a pipeline of 15 qualified enterprise opportunities worth $3M+

PRODUCT TEAM OBJECTIVE: Create product experiences that make enterprise buyers choose us
  Product KR1: Deliver enterprise admin dashboard with role-based access (by June 1)
  Product KR2: Achieve enterprise trial-to-paid conversion of 40% (from 22%)
  Product KR3: Reduce enterprise onboarding time from 3 weeks to 5 days
```

### Step 5: Quarterly Planning Process

**Week 1 — Strategy alignment:**
- Leadership team reviews company strategy and priorities
- Draft company-level OKRs (3–5 Objectives)
- Share draft with all team leads for input

**Week 2 — Team OKR drafting:**
- Each team drafts their OKRs in response to company OKRs
- Teams discuss dependencies between departments
- Individual contributors contribute to team OKRs (bottom-up input)

**Week 3 — Review and align:**
- Team leads review all OKRs with leadership
- Check: Do team KRs, if achieved, actually deliver the company KRs?
- Adjust and finalize

**Week 4 — Publish and kick off:**
- Publish all OKRs company-wide (transparency is essential)
- Hold an all-hands to explain the logic and answer questions
- Establish weekly check-in cadence

**Ongoing cadence:**
- **Weekly**: Each team lead posts a 1–3 sentence status update per OKR
- **Monthly**: Team-level deep dive — what's on track, what's off track, what are we changing?
- **Quarter end**: Formal scoring, retrospective, and input to next quarter's planning

### Step 6: Scoring OKRs

**Scoring scale (0.0 to 1.0):**
- **0.7** = expected result if you worked hard (not a failure!)
- **1.0** = full achievement (question: were you ambitious enough?)
- **0.0–0.3** = significant miss (investigate why)
- **0.3–0.7** = partial progress

**Scoring example:**
```
KR: Increase 30-day activation rate from 42% to 65% by Q3 end

Achieved: 55%

Score: (55 - 42) / (65 - 42) = 13/23 = 0.57
```

**Team OKR score** = average of all KR scores in the Objective
**Company OKR score** = weighted average across all Objectives (weight by strategic importance)

**Scoring interpretation:**
- Avg score 0.6–0.7: Healthy — ambitious enough, executing well
- Avg score > 0.9: OKRs were too easy (sandbagging)
- Avg score < 0.4: OKRs were too ambitious, or serious execution problems

## Examples

### Example 1: Write Company-Level OKRs for a SaaS Startup

**Context:** B2B SaaS startup, 40 employees, $1.5M ARR, Series A stage, growing 8% MoM. Priority: prove product-market fit and ramp to $3M ARR.

**Q3 Company OKRs:**

**Objective 1: Prove we have product-market fit with mid-market customers**
- KR1: Achieve Net Revenue Retention (NRR) of 110%+ across accounts >$10K ARR
- KR2: 30-day retention of new users reaches 55% (up from 38%)
- KR3: Earn a G2 rating of 4.5+ with 50+ reviews
- KR4: 8 of 10 customers interviewed would be "very disappointed" if product went away (Sean Ellis benchmark)

**Objective 2: Build a scalable, efficient growth engine**
- KR1: Grow MRR from $125K to $200K by September 30
- KR2: Reduce blended CAC from $8,200 to $5,500
- KR3: Achieve a sales cycle under 30 days for self-serve trials converting to paid
- KR4: Launch referral program generating 15% of new signups

**Objective 3: Ship a product our customers can't live without**
- KR1: Launch integrations with Salesforce, HubSpot, and Slack by August 15
- KR2: Reduce P1/P2 bug count from 23 open to <5 at any time
- KR3: Achieve customer-reported CSAT of 90%+ on new feature launches

---

### Example 2: Write Team OKRs for an Engineering Team

**Context:** 8-engineer team at a 120-person company. Company OKR includes: "Scale infrastructure to support 10× growth."

**Q2 Engineering Team OKRs:**

**Objective 1: Build infrastructure that never lets our customers down**
- KR1: Achieve 99.95% platform uptime SLA (up from 99.3%)
- KR2: Reduce P95 API response time from 1.2s to under 300ms for all endpoints
- KR3: Zero data loss incidents (maintain current record)
- KR4: Implement automated rollback so deployment incidents resolve in < 10 minutes

**Objective 2: Ship features fast without sacrificing quality**
- KR1: Increase deployment frequency from 2/week to daily (merge-to-prod)
- KR2: Reduce Change Failure Rate from 12% to <5%
- KR3: Achieve 80% test coverage on all new code shipped in Q2
- KR4: Reduce average PR review cycle time from 3 days to under 1 day

**Objective 3: Pay down the technical debt holding back our team**
- KR1: Migrate legacy auth service to new auth platform (0 downtime)
- KR2: Reduce on-call pages by 60% by resolving the top 5 recurring alert sources
- KR3: Complete TypeScript migration of core API (currently 40% complete → 100%)

## Best Practices
- Set OKRs at the beginning of the quarter, not mid-quarter
- Make all OKRs visible to the entire company—transparency is what makes them effective
- Don't tie OKRs directly to compensation; it causes sandbagging and kills ambition
- OKRs should be set with input from the team, not handed down unilaterally
- 3 OKRs with 3 KRs each is better than 8 OKRs with 2 KRs each—focus is the point
- Every KR needs an owner, a baseline measurement, and a way to track progress weekly
- Separate aspirational ("moonshot") OKRs from committed ("roofshot") OKRs explicitly

## Common Mistakes
- Writing tasks as Key Results: "Launch new feature" is a task; "Increase feature adoption from 20% to 45%" is a KR
- Setting KRs you can't measure at quarter end (output without data access)
- Copying company OKRs verbatim at the team level without translation
- Writing so many OKRs that they cease to be priorities
- Never checking in mid-quarter — by the time you score them it's too late to course-correct
- Treating a 0.5 score as failure — 0.7 is success; if everything scores 1.0, you played it too safe
- Using OKRs for "business as usual" work — OKRs should represent meaningful stretch

## Tips & Tricks
- The "cover the score" test: if you covered the score and read the KR aloud, could you independently calculate the correct score? If not, the KR is too vague
- Write OKRs before you've decided how you'll achieve them — OKRs describe outcomes, not plans
- Use "confidence checks": have each KR owner rate their confidence (1–10) weekly; declining confidence early is a trigger to course-correct or re-scope
- A shared OKR between two teams creates accountability and encourages collaboration on shared goals
- Run a "pre-mortem" on new OKRs: "It's the end of the quarter and we scored 0.3. What went wrong?" — it surfaces risks before they happen

## Related Skills
- [product-manager](../../business/product-manager/SKILL.md)
- [business-analyst](../../business/business-analyst/SKILL.md)
- [meeting-facilitator](../../business/meeting-facilitator/SKILL.md)
