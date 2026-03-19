---
name: lesson-planner
description: "Use this skill when designing structured lesson plans with clear learning objectives, warm-up activities, direct instruction, guided practice, independent practice, and formative assessment. Triggers: 'create a lesson plan', 'plan a class on', 'design a unit for', 'align to Common Core/NGSS'. Not for grading student work, writing full curriculum maps, or producing parent newsletters."
version: 1.0.0
author: community
tags: [education, lesson-planning, teaching, curriculum]
license: MIT
---

# Lesson Planner

## Overview
The Lesson Planner skill produces complete, classroom-ready lesson plans structured around research-backed instructional design principles. Each plan includes a clear learning objective tied to educational standards (Common Core, NGSS, TEKS, etc.), a warm-up or hook to activate prior knowledge, direct instruction with key vocabulary, guided and independent practice activities, and a formative assessment to gauge student understanding. Plans are scaffolded for the specified grade level and differentiated to support diverse learners, including English Language Learners (ELLs) and students with IEPs.

## When to Use
- Designing a single-day or multi-day lesson for K–12 or higher education
- Aligning instruction to a specific standard (e.g., CCSS.MATH.5.NF.A.1, NGSS MS-PS1-1)
- Creating a lesson that includes differentiated activities for mixed-ability classrooms
- Structuring project-based or inquiry-based learning experiences
- Planning substitute-teacher-ready lesson materials with minimal setup

## When NOT to Use
- Writing full semester or year-long curriculum maps (use a curriculum-design skill instead)
- Grading or evaluating completed student work
- Creating individualized education programs (IEPs) or 504 plans
- Producing parent communication letters or newsletters
- Designing professional development sessions for adult educators (adult learning principles differ significantly)

## Quick Reference
| Task | Approach |
|------|----------|
| Align to a standard | Provide the standard code (e.g., CCSS.ELA-LITERACY.RI.7.1) and grade; plan objectives are reverse-engineered from it |
| Differentiate instruction | Specify learner tiers (below grade, on grade, above grade) and ELL/IEP accommodations needed |
| Choose activity types | Specify hands-on, discussion-based, tech-integrated, or direct instruction preference |
| Set lesson duration | State total class period length (e.g., 45 min, 90 min block) so pacing is realistic |
| Add formative assessment | Specify format preference: exit ticket, think-pair-share, whiteboard check, digital poll |

## Instructions

1. **Gather lesson context** — Before generating the plan, confirm: grade level, subject, topic or standard code, class period length (in minutes), available materials/technology, and any known learner needs (ELL, IEP, gifted).

2. **Write the learning objective** — Craft one or two measurable objectives using Bloom's Taxonomy action verbs (e.g., "Students will be able to *compare* fractions with unlike denominators using visual models"). Explicitly link each objective to the target standard.

3. **Design the warm-up / hook (5–10 min)** — Create an engagement activity that activates prior knowledge or poses a compelling question. Options: number talks, quick writes, short video clips, think-pair-share prompts, or a puzzling real-world scenario.

4. **Write the direct instruction segment (10–15 min)** — Outline key vocabulary with student-friendly definitions, an I Do (teacher models) demonstration, and anchor examples. Include comprehension checks (e.g., "thumbs up/down") to monitor understanding in real time.

5. **Build guided practice (10–15 min)** — Design collaborative activities (pair work, small groups, stations) where students apply the concept with teacher facilitation. Include sentence frames or graphic organizers for scaffolding.

6. **Create independent practice (10–15 min)** — Provide problems or tasks students complete individually. Vary complexity: include below-grade, on-grade, and extension questions to serve all learners.

7. **Develop the formative assessment / exit ticket (5 min)** — Write a 1–3 question check that directly measures the learning objective. Describe how the teacher will use results (e.g., flexible grouping the next day).

8. **List materials and technology** — Enumerate everything needed: handouts, manipulatives, slides, online tools, graph paper, etc. Flag items that require advance preparation.

9. **Add differentiation notes** — Explicitly state scaffolds for struggling learners (sentence frames, reduced problem sets, visual aids) and extensions for advanced students (open-ended tasks, cross-disciplinary connections).

10. **Include standards alignment** — List the primary standard and any supporting standards addressed in the lesson.

## Examples

### Example 1: 5th Grade Fractions — Adding with Unlike Denominators
**Input:** "Create a 60-minute 5th grade math lesson on adding fractions with unlike denominators, aligned to CCSS.MATH.CONTENT.5.NF.A.1. Class has 28 students, 6 are ELL, no tech available."

**Output:**
```
Grade: 5 | Subject: Math | Duration: 60 min
Standard: CCSS.MATH.CONTENT.5.NF.A.1 — Add and subtract fractions with unlike denominators.

Learning Objective:
Students will be able to add fractions with unlike denominators by finding equivalent fractions
using the least common denominator, achieving at least 4/5 correct on the exit ticket.

Warm-Up (8 min):
Post on board: "Which is larger — 1/3 or 1/4? How do you know?"
Students write on mini whiteboards → brief whole-class share. Teacher probes: "What if we
need to add them?"

Direct Instruction (12 min):
Key Vocabulary: denominator, numerator, equivalent fraction, least common denominator (LCD).
I Do: Model 1/3 + 1/4 using fraction bar manipulatives. Think aloud: "I need a common
language — both fractions need the same denominator." Show LCD = 12 → 4/12 + 3/12 = 7/12.
Comprehension check: "Show me thumbs up if 2/6 is the same as 1/3."

Guided Practice (15 min):
Partners complete 4 problems on "Fraction Addition Mats" (pre-drawn fraction bars).
Problems: 1/2 + 1/3, 2/5 + 1/4, 3/8 + 1/6, 1/3 + 3/4.
ELL scaffold: Bilingual vocabulary card; sentence frame: "The LCD of ___ and ___ is ___."
Teacher circulates, targets struggling pairs first.

Independent Practice (15 min):
Below grade: 1/2 + 1/4, 1/3 + 1/6 (denominators are multiples of each other)
On grade: 2/5 + 3/8, 5/6 + 1/4, 1/3 + 2/7
Extension: Word problem — "Maria ate 2/5 of a pizza and James ate 3/8. What fraction did
they eat together? What fraction is left?"

Exit Ticket (5 min — remaining time):
1. Solve: 3/4 + 2/5 = ___
2. Explain in one sentence how you found the common denominator.

Materials: Fraction bar manipulatives (class set), mini whiteboards & markers, Fraction
Addition Mats (printed), bilingual vocabulary cards (Spanish/English).

Differentiation:
- Struggling: Allow use of fraction bars throughout; reduce independent practice to 3 problems.
- Advanced: Extension word problem + create their own word problem for a partner.

Standards: Primary — CCSS.MATH.5.NF.A.1 | Supporting — CCSS.MATH.4.NF.A.1 (equivalent fractions)
```

### Example 2: High School CS — Introduction to Python Variables and Data Types
**Input:** "Make a 90-minute intro lesson for a 9th/10th grade Computer Science class covering Python variables and data types (int, float, str, bool). Students have Chromebooks and access to repl.it. No prior programming experience."

**Output:**
```
Grade: 9–10 | Subject: Computer Science | Duration: 90 min
Standard: CSTA K-12 CS Standards 2-AP-11 — Create clearly named variables that store data.

Learning Objectives:
1. Students will be able to declare variables in Python and assign values of four data types.
2. Students will be able to use type() to identify a variable's data type and explain why
   data types matter in programs.

Warm-Up (10 min):
"Real-World Variables" activity: Show 4 objects (a ruler, a name tag, a light switch, a
price tag). Ask: "What kind of information does each store?" Connect to idea that computers
need to store different *types* of data. Poll: "Have you ever filled out a form online?
What did it ask for?"

Direct Instruction (20 min):
Key Vocabulary: variable, data type, integer (int), float, string (str), boolean (bool),
assignment operator (=).
I Do: Open repl.it, live-code on projected screen:
  age = 15          # int
  gpa = 3.85        # float
  name = "Alex"     # str
  is_enrolled = True  # bool
  print(type(age))  # <class 'int'>
Explain: "Variables are labeled containers. Data types tell Python what *kind* of data
lives in each container." Demo common mistake: age = "15" vs age = 15.

Guided Practice (25 min):
Pair programming on repl.it — "About Me" starter template:
Students fill in 6 variables about themselves (first_name, age, favorite_number,
gpa_goal, is_morning_person, favorite_color), then print all with descriptive labels.
Pairs swap and peer-review: "Did they use the right data type for each?"
Teacher circulates; posts common errors on board for class discussion.

Independent Practice (20 min):
"Debug the Code" worksheet (digital): 5 code snippets each containing 1 type-related bug.
Students identify the bug, explain why it's wrong, and write the corrected version.
Extension: Write a 10-variable "profile" for a fictional character, using all 4 data types
at least twice, then write a print statement that combines variables using f-strings.

Formative Assessment / Exit Ticket (10 min):
On repl.it, students write and run:
  1. A variable storing their birth year as an int.
  2. A variable storing their full name as a str.
  3. Print both with type() to prove the types.
  4. Answer in comments: "What would go wrong if you stored your age as a str?"
Teacher reviews replits before next class; students below 70% accuracy join a small
group reteach station.

Materials: Chromebooks (1:1), repl.it accounts (pre-created), projected teacher repl.it,
"Debug the Code" Google Doc, vocabulary reference card.

Differentiation:
- Support: Vocabulary reference card with syntax examples; sentence starters for exit ticket.
- ELL: Allow native-language comments in code; partner with bilingual peer during guided practice.
- Advanced: f-string extension task; challenge — research and demonstrate one additional data
  type (list or dict) to the class next session.

Standards: CSTA 2-AP-11, 2-AP-19 | Supporting: CSTA 2-AP-12 (user input with input())
```

## Best Practices
- Always start with the standard, then reverse-engineer the objective and activities — never the other way around
- Keep direct instruction to 15 minutes maximum; students learn by doing, not listening
- Build in at least one comprehension check during direct instruction to catch misconceptions early
- Write exit ticket questions before planning activities to ensure alignment between assessment and instruction
- Specify exact timing for each segment so the plan is usable by a substitute teacher
- Differentiate by task complexity, not by giving struggling students less work — reduce complexity, not quantity

## Common Mistakes
- Writing objectives that are too vague ("Students will understand fractions") — use measurable verbs
- Overloading direct instruction with too much content, leaving no time for practice
- Skipping the warm-up to save time — engagement at the start significantly impacts retention
- Creating independent practice that is identical to guided practice — it should require transfer
- Forgetting to align the exit ticket to the stated learning objective
- Ignoring diverse learner needs until after the plan is written — differentiation should be built in from the start

## Tips & Tricks
- Use the "I Do → We Do → You Do" (gradual release) structure as a default scaffold
- For 90-minute block periods, add a second mini-lesson or a collaborative application project after independent practice
- Embed choice wherever possible (e.g., students choose their word problem context) to increase engagement
- Keep exit tickets to 3 questions or fewer — data is only useful if you can review it before next class
- Annotate your plan with anticipated student misconceptions so you can address them proactively
- Label each plan segment with its purpose (hook, model, practice) so the instructional rationale is clear

## Related Skills
- [tutor](../tutor/SKILL.md)
- [quiz-creator](../quiz-creator/SKILL.md)
- [flashcard-maker](../flashcard-maker/SKILL.md)
