---
name: quiz-creator
description: "Use this skill when you need to generate quiz questions, assessments, or practice tests — triggered by phrases like 'create a quiz on', 'write test questions about', 'make practice questions for', or 'generate an assessment'. Not for grading submitted student work, writing full lesson plans, or creating legally proctored exam content."
version: 1.0.0
author: community
tags: [education, quiz, assessment, learning]
license: MIT
---

# Quiz Creator

## Overview
The Quiz Creator skill generates complete, high-quality assessments covering multiple question formats: multiple-choice (MCQ), true/false, short-answer, and essay prompts. Every quiz includes a full answer key with explanations — not just correct answers, but why each answer is right and why the distractors are wrong. The skill calibrates difficulty levels (beginner, intermediate, advanced), maps questions to specific learning objectives, and balances coverage across topics. Output is suitable for classroom use, self-study, interview preparation, employee training, and certification practice.

## When to Use
- A teacher or instructor needs quiz or test questions for a specific topic and level
- A learner wants practice questions to self-assess before an exam
- An employer needs screening or training assessment questions
- A user wants to create flashcard-style Q&A pairs for a subject
- A curriculum designer needs questions mapped to specific learning objectives
- A user preparing for a certification exam needs realistic practice questions
- A trainer needs knowledge-check questions for a corporate training module

## When NOT to Use
- The user wants actual exam questions from a live, proctored test (academic integrity violation)
- The task is grading or evaluating existing student responses
- The user needs full lesson plans with instructional content (use lesson-planner skill)
- The topic requires domain expertise beyond general knowledge (specialized medical board exams, bar exam questions should be validated by professionals)
- The user asks for answer keys to tests they are currently taking (academic dishonesty)

## Quick Reference
| Task | Approach |
|------|----------|
| Multiple-choice questions | 4 options (A–D): 1 correct, 3 plausible distractors; explain why each wrong answer is wrong |
| True/False questions | State clearly; avoid double negatives; pair each with a brief explanation |
| Short-answer questions | Define expected answer length; provide model answer and key criteria |
| Essay prompts | Include grading rubric with criteria and point values |
| Difficulty calibration | Easy = recall; Medium = application; Hard = analysis/synthesis/evaluation |
| Learning objective mapping | State the objective each question assesses (e.g., "Student can define X") |
| Question variety | Mix formats within a quiz to reduce test-taking strategy effects |

## Instructions

1. **Clarify the quiz parameters** — Establish the topic, target audience (grade level, background), number of questions, question formats desired, difficulty level, and any specific subtopics or learning objectives to cover. If not provided, use reasonable defaults and state your assumptions.

2. **Identify learning objectives** — For each major subtopic, state the learning objective being assessed (e.g., "recall the definition of X", "apply formula Y to solve problem Z", "evaluate the validity of argument W"). This ensures the quiz tests real understanding, not just test-taking luck.

3. **Balance coverage across subtopics** — Distribute questions proportionally across all major areas of the topic. Do not over-index on easy-to-question material while neglecting harder but important concepts.

4. **Write the questions** — For each question:
   - Make the stem (question body) clear, specific, and unambiguous
   - Avoid trick questions — test understanding, not gotchas
   - Use precise language; avoid vague words like "sometimes", "often", or "may"
   - Ensure only one answer is clearly correct for MCQ; eliminate ambiguity

5. **Write high-quality distractors for MCQ** — Each wrong answer (distractor) should:
   - Be plausible to someone who partially understands the material
   - Represent a common misconception or frequent error
   - Be the same grammatical form and approximate length as the correct answer
   - Never be obviously absurd — this makes the question too easy and doesn't test knowledge

6. **Calibrate difficulty correctly**:
   - **Easy (recall/recognition)**: "What is the definition of X?" or "Which of the following is true about Y?"
   - **Medium (application)**: "Given scenario Z, which approach would you use?" or "Calculate X given Y and Z"
   - **Hard (analysis/evaluation)**: "Why does X happen rather than Y in this context?" or "Evaluate the trade-offs between approach A and B"

7. **Write complete answer keys with explanations** — For every question, provide:
   - The correct answer clearly identified
   - A 1–3 sentence explanation of why it is correct
   - For MCQ: a brief explanation of why each wrong option is incorrect
   - The learning objective this question assesses

8. **Assign point values if requested** — Default to equal weighting unless the user specifies otherwise. Weight harder questions more heavily if the quiz distinguishes mastery levels.

9. **Format clearly for the intended use** — Separate the question sheet from the answer key. Use consistent numbering. For essay questions, include a rubric. For MCQ, use clear option labels (A, B, C, D).

10. **Review for quality before delivering** — Check that: no two questions give away answers to each other; all correct answers are unambiguously correct; all distractors are genuinely plausible; difficulty distribution matches the request.

## Examples

### Example 1: Python Basics Quiz (Beginner Level)
**Input:**
"Create a 5-question multiple-choice quiz on Python basics for beginners. Cover: variables, data types, if-statements, loops, and functions. Include the answer key with explanations."

**Output:**
```
PYTHON BASICS QUIZ — Beginner Level
5 Questions | Multiple Choice | Answer Key Included
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTION 1 — Variables & Data Types
What is the data type of the value stored in x after this code runs?
    x = "42"

  A) integer
  B) float
  C) string
  D) boolean

──────────────────────────────────────────────────
QUESTION 2 — Data Types
Which of the following is a valid Python boolean value?

  A) "True"
  B) true
  C) True
  D) 1.0

──────────────────────────────────────────────────
QUESTION 3 — If-Statements
What will this code print?
    temperature = 15
    if temperature > 20:
        print("Warm")
    elif temperature > 10:
        print("Cool")
    else:
        print("Cold")

  A) Warm
  B) Cool
  C) Cold
  D) Nothing — there is a syntax error

──────────────────────────────────────────────────
QUESTION 4 — Loops
How many times will "hello" be printed?
    for i in range(3):
        print("hello")

  A) 2
  B) 3
  C) 4
  D) 0

──────────────────────────────────────────────────
QUESTION 5 — Functions
What does this function return when called as add(3, 4)?
    def add(a, b):
        return a + b

  A) "a + b"
  B) 34
  C) 7
  D) None

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANSWER KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1 — ANSWER: C) string
Learning objective: Identify Python data types by value appearance.
Explanation: Even though 42 looks like a number, the quotation marks
("42") make it a string literal. Python does not automatically convert
it to an integer.
• A) Wrong: integers have no quotes, e.g., x = 42
• B) Wrong: floats have a decimal point, e.g., x = 42.0
• D) Wrong: booleans are True or False, not numbers in quotes

Q2 — ANSWER: C) True
Learning objective: Recall correct Python boolean syntax.
Explanation: Python boolean literals are capitalized: True and False.
Python is case-sensitive, so "true" is a NameError.
• A) Wrong: "True" with quotes is a string, not a boolean
• B) Wrong: lowercase "true" is not a valid Python keyword
• D) Wrong: 1.0 is a float; while truthy, it is not a boolean type

Q3 — ANSWER: B) Cool
Learning objective: Trace execution flow through if/elif/else.
Explanation: temperature = 15 fails the first condition (15 > 20 is
False), then passes the elif (15 > 10 is True), so "Cool" is printed.
• A) Wrong: 15 is not greater than 20
• C) Wrong: "Cold" only prints if both conditions above are False
• D) Wrong: the syntax is valid; all three keywords are correct

Q4 — ANSWER: B) 3
Learning objective: Understand that range(n) generates n values (0 to n-1).
Explanation: range(3) produces [0, 1, 2] — three values. The loop body
executes once per value, so "hello" prints 3 times.
• A) Wrong: common mistake — range(3) gives 3 items, not 2
• C) Wrong: range(3) stops at 2, not 3; 4 iterations would need range(4)
• D) Wrong: range(3) is not empty; range(0) would produce 0 iterations

Q5 — ANSWER: C) 7
Learning objective: Understand function parameters, execution, and return values.
Explanation: add(3, 4) binds a=3, b=4, executes return 3 + 4, and
returns the integer 7.
• A) Wrong: return a + b evaluates the expression, it doesn't return the string "a + b"
• B) Wrong: 34 would result from string concatenation ("3" + "4"), not addition
• D) Wrong: None is returned only when a function has no return statement
```

### Example 2: World War II History Quiz (Mixed Format, Intermediate)
**Input:**
"Create a 6-question World War II quiz for a high school history class. Mix question types: 3 multiple choice, 2 true/false, 1 short answer. Intermediate difficulty. Cover causes, major events, and outcomes. Include answer key."

**Output:**
```
WORLD WAR II HISTORY QUIZ — High School Level
6 Questions | Mixed Format | Intermediate Difficulty
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MULTIPLE CHOICE (2 points each)

QUESTION 1 — Causes of WWII
Which policy did Britain and France pursue at the 1938 Munich Conference,
granting Hitler control of the Sudetenland in hopes of preventing war?

  A) Containment
  B) Isolationism
  C) Appeasement
  D) Brinkmanship

──────────────────────────────────────────────────
QUESTION 2 — Major Events
What was the primary strategic significance of the Allied D-Day landings
at Normandy on June 6, 1944?

  A) It was the first Allied victory against Nazi Germany
  B) It opened a major Western Front, forcing Germany to fight on two sides
  C) It directly caused Germany's immediate surrender
  D) It secured Allied control of North Africa

──────────────────────────────────────────────────
QUESTION 3 — Pacific Theater
The United States dropped atomic bombs on two Japanese cities in August 1945.
Which two cities were targeted?

  A) Tokyo and Osaka
  B) Nagasaki and Kyoto
  C) Hiroshima and Nagasaki
  D) Hiroshima and Tokyo

──────────────────────────────────────────────────
TRUE / FALSE (1 point each — mark T or F, then explain in one sentence)

QUESTION 4
The Nazi-Soviet Non-Aggression Pact of 1939 meant that Germany and the
Soviet Union were military allies throughout World War II.   [ T / F ]

──────────────────────────────────────────────────
QUESTION 5
The Holocaust resulted in the systematic murder of approximately
6 million Jewish people under Nazi rule.   [ T / F ]

──────────────────────────────────────────────────
SHORT ANSWER (5 points)

QUESTION 6
Identify and explain TWO long-term consequences of World War II on
the global political order that are still relevant today.
(Write 4–6 sentences. Focus on specific outcomes, not vague statements
like "many people died.")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANSWER KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1 — ANSWER: C) Appeasement
Explanation: Appeasement was the policy of making concessions to an
aggressive power to avoid war. At Munich, Chamberlain and Daladier
allowed Hitler to annex the Sudetenland. Far from preventing war, it
emboldened Hitler to make further demands.
• A) Containment: Cold War policy against Soviet expansion, not 1938
• B) Isolationism: U.S. policy of non-involvement in European affairs
• D) Brinkmanship: Cold War strategy of pushing to the edge of war to force concessions

Q2 — ANSWER: B) It opened a major Western Front, forcing Germany to fight on two sides
Explanation: D-Day created a large-scale Western Front, meaning Germany
had to divide its military forces between defending France in the west and
fighting the Soviet Union in the east. This two-front pressure was decisive.
• A) Wrong: Allies had won battles (e.g., El Alamein, Stalingrad) before D-Day
• C) Wrong: Germany surrendered in May 1945, nearly a year after D-Day
• D) Wrong: North Africa was secured by May 1943, more than a year before D-Day

Q3 — ANSWER: C) Hiroshima and Nagasaki
Explanation: "Little Boy" was dropped on Hiroshima on August 6, 1945;
"Fat Man" on Nagasaki on August 9. Tokyo was never bombed atomically;
Kyoto was removed from the target list due to its cultural significance.

Q4 — ANSWER: FALSE
Explanation: The Pact was a non-aggression agreement (not a military
alliance), and it collapsed entirely when Germany invaded the Soviet Union
in Operation Barbarossa in June 1941. The USSR then joined the Allies.

Q5 — ANSWER: TRUE
Explanation: The Holocaust was the state-sponsored, systematic persecution
and murder of approximately six million Jews — about two-thirds of European
Jewry — along with millions of others including Roma, disabled people,
political prisoners, and others.

Q6 — MODEL ANSWER (award 2–3 points per consequence; max 5 points)

Acceptable consequences include:
1. Formation of the United Nations (1945): WWII demonstrated the failure
   of the League of Nations. The UN was established to provide collective
   security, mediate disputes, and prevent another world war. Its structure
   (Security Council with 5 permanent members holding veto power) still
   governs global diplomacy today.

2. Beginning of the Cold War: The defeat of Nazi Germany left two
   superpowers — the U.S. and USSR — with incompatible ideological systems
   (capitalism vs. communism). Their rivalry shaped global politics for
   45 years and its legacy (NATO, Russian-Western tensions) persists today.

3. Decolonization: WWII weakened European colonial powers economically and
   morally, accelerating independence movements across Asia and Africa
   throughout the 1950s–1960s and reshaping the map of the modern world.

4. Nuclear age: The atomic bombing of Japan initiated the nuclear era.
   Nuclear deterrence ("MAD") shaped Cold War strategy and continues to
   define global security calculations, with nuclear proliferation
   remaining a major policy concern today.

Grading: 5/5 for two well-explained, specific consequences with present-day
relevance. 3–4/5 for correct but vague or incompletely explained answers.
1–2/5 for partially correct or very superficial answers.
```

## Best Practices
- Write distractors before you write the correct answer — it forces you to think about what plausible wrong answers look like
- Test every MCQ question by imagining a student who knows the material moderately well — would the correct answer be clearly right without being obvious from elimination alone?
- Include a mix of recall, application, and analysis questions in any substantial quiz — pure recall tests memorization, not understanding
- Provide rationale for every answer choice in the key, especially why wrong answers are wrong — this is where real learning happens when reviewing
- Avoid "all of the above" and "none of the above" answer choices — they test elimination strategies, not knowledge
- For essay questions, always include a rubric with specific criteria — vague prompts produce vague answers
- Calibrate the number of questions to realistic time constraints (roughly 1 minute per MCQ, 5–10 min per essay)

## Common Mistakes
- Writing trick questions where the "right" answer depends on an obscure technicality not covered in the learning material
- Making distractors obviously wrong (e.g., implausible options that no one who studied would choose), making the quiz too easy
- Clustering all questions about one subtopic while neglecting others — poor coverage validity
- Writing ambiguous question stems that have more than one defensible correct answer
- Forgetting to specify what kind of short-answer or essay response is expected (length, format, specific criteria)
- Including questions that inadvertently reveal answers to other questions in the same quiz
- Overloading questions with multiple concepts tested simultaneously — one concept per question is the rule

## Tips & Tricks
- Use Bloom's Taxonomy levels to design question difficulty: Remember → Understand → Apply → Analyze → Evaluate → Create
- For MCQ distractors, mine the topic's most common misconceptions — these make the best wrong answers
- "Which of the following is NOT…" questions are valid but use them sparingly; they test different cognitive skills
- Shuffle answer option order so the correct answer is not always in the same position across questions
- For self-study quizzes, suggest the learner answer without looking at options first (short answer style), then check — this forces active recall
- Include a brief "how to use this quiz" note: review wrong answers using the explanation, not just the correct letter
- Number questions clearly and leave enough whitespace — cluttered formatting increases cognitive load unnecessarily

## Related Skills
- [tutor](../tutor/SKILL.md)
- [lesson-planner](../lesson-planner/SKILL.md)
- [flashcard-maker](../flashcard-maker/SKILL.md)
