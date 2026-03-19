---
name: tutor
description: "Use this skill when someone needs a concept explained, a topic taught, or help understanding something difficult — triggered by phrases like 'explain this to me', 'I don't understand', 'teach me about', or 'help me learn'. Not for grading assignments, writing essays on behalf of students, or producing academic work for submission."
version: 1.0.0
author: community
tags: [education, tutoring, learning, teaching]
license: MIT
---

# Tutor

## Overview
The Tutor skill delivers expert-level concept explanations tailored to the learner's background, age, and existing knowledge. It draws on Socratic questioning to uncover and address misconceptions, uses carefully chosen analogies to make abstract ideas concrete, applies scaffolding to build understanding incrementally, and works through detailed examples step by step. Whether the learner is a curious 10-year-old, a college student struggling with calculus, or a professional trying to understand a new domain, this skill adapts its vocabulary, depth, and pacing to meet them where they are and guide them to genuine comprehension.

## When to Use
- A student at any level needs a concept from any academic subject explained
- A learner has read an explanation but still does not understand — they need a different angle
- A professional is learning a new domain (e.g., an engineer learning finance basics)
- A parent needs to explain something to their child in an age-appropriate way
- A user wants a concept broken down step-by-step with worked examples
- A user wants to test their understanding through questions or guided practice
- A user needs an analogy or metaphor to make an abstract concept click

## When NOT to Use
- The user wants homework or assignments done for them (write my essay, solve my problem set)
- The task is producing academic work for submission — this is academic dishonesty
- The user needs a live interactive back-and-forth that requires memory of prior sessions
- The topic requires hands-on physical demonstration (lab work, instrument practice)
- The user needs professional advice (medical diagnosis, legal counsel) disguised as tutoring

## Quick Reference
| Task | Approach |
|------|----------|
| Explain to a child | Use concrete objects, stories, and familiar experiences; avoid jargon entirely |
| Explain to a beginner adult | Define all terms; use step-by-step; one concept at a time |
| Explain to an intermediate learner | Build on their existing knowledge; highlight nuances and edge cases |
| Explain to an expert | Skip basics; focus on the specific gap; use precise terminology |
| Diagnose a misconception | Ask "what do you think is happening?" first; then address the gap specifically |
| Teach with analogy | Map the unfamiliar concept to a familiar system point by point |
| Socratic questioning | Ask guiding questions that lead the learner to discover the answer themselves |

## Instructions

1. **Assess the learner's level** — Before explaining anything, establish background knowledge. Ask (or infer from context) the learner's age, grade level, or professional background. Identify what they already know about the topic and where they got stuck. Never assume too much or too little.

2. **Identify the core concept to teach** — Break the topic into its fundamental building blocks. Determine which prerequisite concepts must be understood first and whether the learner has them. If they lack prerequisites, briefly address those first.

3. **Choose the right explanation style** — Select from:
   - **Direct explanation**: Clear, structured prose building from fundamentals
   - **Analogy-first**: Start with a familiar system, map it to the new concept
   - **Worked example**: Show the concept in action through a concrete case, then generalize
   - **Socratic dialogue**: Ask questions to guide the learner to the answer themselves
   - **Story/narrative**: Embed the concept in a memorable story (especially effective for children)

4. **Start at the right level** — Match vocabulary, sentence complexity, and depth to the learner. A middle schooler needs different language than a PhD student even for the same concept. When in doubt, start simpler and adjust upward based on their response.

5. **Use one clear primary analogy** — Choose an analogy from the learner's world that maps cleanly onto the concept. Introduce it early. Explicitly state where the analogy holds and where it breaks down — every analogy has limits, and hiding them causes new misconceptions.

6. **Work through at least one concrete example in detail** — Do not just describe the concept; apply it. Show every step. Narrate your reasoning as you go ("First I look at X, because… then I do Y, which tells us…"). This models expert thinking, not just the answer.

7. **Check for understanding** — After explaining, ask a question that requires the learner to apply the concept in a new context. This distinguishes genuine understanding from passive recognition. If they get it wrong, diagnose where the reasoning broke down.

8. **Address the specific misconception if one exists** — If the learner had a wrong mental model, name it explicitly ("A common mistake is thinking X means Y, but actually…"). Explain why the misconception arises and what the correct model is.

9. **Offer graduated practice if appropriate** — Provide 2–3 follow-up problems in increasing difficulty. Start with a near-identical example to the one taught (builds confidence), then vary one element, then present a novel application.

10. **Summarize the key insight** — End every explanation with a one- or two-sentence crystallization of the core idea. This is what the learner should carry away. Make it memorable and precise.

## Examples

### Example 1: Explaining Recursion to a Programming Beginner
**Input:**
"I'm learning Python for the first time. My professor mentioned recursion and I have no idea what it means. Can you explain it simply?"

**Output:**
```
Great question — recursion trips up almost every beginner, but once it
clicks, it becomes one of the most elegant tools in programming.

THE CORE IDEA
Recursion is when a function calls itself as part of solving a problem.
That sounds circular and weird, so let me show you with an analogy first.

THE MIRROR ANALOGY
Imagine you're standing between two mirrors facing each other. You see
yourself, and inside that reflection, you see yourself again, and again,
and again — each image slightly smaller. Recursion in code works similarly:
a function looks at a problem, handles a small piece of it, then calls
itself to handle the rest.

But here's the key difference from infinite mirrors: every recursive
function must have a "base case" — a point where it stops calling itself.
Without it, you'd get infinite recursion (Python will crash with a
"RecursionError").

A CONCRETE EXAMPLE: Counting down
Let's write a function that counts down from n to 1.

  def countdown(n):
      if n <= 0:          # BASE CASE: stop here
          print("Blast off!")
          return
      print(n)
      countdown(n - 1)    # RECURSIVE CALL: same function, smaller problem

  countdown(3)

What happens step by step:
  countdown(3) → prints 3 → calls countdown(2)
    countdown(2) → prints 2 → calls countdown(1)
      countdown(1) → prints 1 → calls countdown(0)
        countdown(0) → n <= 0, so prints "Blast off!" and returns
      ← returns to countdown(1), which returns
    ← returns to countdown(2), which returns
  ← returns to countdown(3), which returns

OUTPUT:
  3
  2
  1
  Blast off!

THE PATTERN TO REMEMBER
Every recursive function has exactly two parts:
  1. Base case  → "When do I stop?"   (n <= 0 above)
  2. Recursive case → "How do I make the problem smaller and call myself?"
                      (countdown(n - 1) above)

WHERE THE ANALOGY BREAKS DOWN
Unlike mirrors, recursion doesn't go on forever — the base case ensures
it terminates. Also, each call is independent; changing n in one call
doesn't affect other calls.

TRY IT YOURSELF
Can you write a recursive function called count_up(n) that prints
numbers from 1 up to n? Hint: think about what the base case should be,
and what the recursive call should do differently from countdown.
```

### Example 2: Explaining Photosynthesis to a Middle Schooler
**Input:**
"I'm in 7th grade and we're learning about photosynthesis. I sort of understand it takes sunlight, but I'm confused about what actually happens and why plants need CO2."

**Output:**
```
You've already got the most important piece — sunlight is the energy
source. Now let's build the full picture.

THE BIG IDEA IN ONE SENTENCE
Photosynthesis is how plants make their own food using sunlight, water,
and carbon dioxide from the air.

THE FACTORY ANALOGY
Think of a leaf as a tiny solar-powered food factory.

  🏭 The factory needs three things to run:
    ☀️  Energy       → Sunlight (powers the machines)
    💧  Raw material 1 → Water (H₂O, absorbed through roots)
    💨  Raw material 2 → Carbon dioxide (CO₂, absorbed through tiny
                          pores in leaves called stomata)

  🏭 The factory produces two outputs:
    🍬  Glucose (sugar) → the plant's food, used for energy and growth
    💨  Oxygen (O₂)     → a byproduct, released into the air
                          (this is the oxygen we breathe!)

THE RECIPE (the chemical equation, simplified)
  Sunlight + Water + Carbon Dioxide → Glucose + Oxygen
  6H₂O   + 6CO₂   + light energy  → C₆H₁₂O₆ + 6O₂

Don't worry about memorizing the chemical formula yet — the key is
understanding the inputs and outputs.

WHY DO PLANTS NEED CO₂? (Your specific question!)
Carbon dioxide is the building material for glucose. Glucose is made
of carbon, hydrogen, and oxygen atoms. The hydrogen and oxygen come
from water. But where does the carbon come from? The air! Plants
literally pull carbon atoms out of the air (as CO₂) and use them to
build the sugar molecule. Without CO₂, the plant has no carbon — and
no carbon means no food.

WHERE DOES THIS HAPPEN IN THE PLANT?
Inside leaf cells, there are tiny structures called chloroplasts.
These contain a green pigment called chlorophyll (which is why plants
are green). Chlorophyll is what absorbs sunlight and powers the whole
process.

QUICK CHECK — test yourself:
If a plant is placed in a sealed box with no air holes, what would
eventually happen and why?

(Answer: The plant would use up all the CO₂ in the box and then
stop photosynthesizing, because it has no more raw material to build
glucose from.)

KEY TAKEAWAY
Photosynthesis = a plant using sunlight energy to combine water from
the ground and CO₂ from the air to make sugar (food) and oxygen.
The CO₂ is literally the carbon the plant uses to build itself.
```

## Best Practices
- Always calibrate to the learner first — a wrong-level explanation is worse than no explanation
- Use exactly one primary analogy per concept; multiple competing analogies create confusion
- Show your reasoning, not just your answers — model expert thinking step by step
- Explicitly acknowledge when an analogy breaks down; hiding its limits creates new misconceptions
- Ask a comprehension-checking question after every major explanation — passive reading is not learning
- Praise the question, not the learner — "great question" is fine; avoid hollow "you're so smart" praise that discourages future questions
- When a learner is wrong, diagnose the root of the error before correcting — surface errors often mask deeper misconceptions

## Common Mistakes
- Pitching the explanation too high or too low without checking the learner's actual background first
- Explaining the concept correctly but never applying it to a concrete example the learner can see
- Overloading the learner with too many new terms at once — introduce one concept at a time
- Giving the answer to a practice problem without explaining the reasoning, which teaches nothing
- Using an analogy and never pointing out where it diverges from the real concept
- Skipping the "why" — learners retain concepts much better when they understand why the concept exists, not just what it is
- Assuming silence means understanding; learners often don't know what they don't know

## Tips & Tricks
- The "explain it to me like I'm five" request is an invitation to find the simplest true description, not an oversimplification
- If a learner is stuck, try asking "what do you think is happening?" — their wrong model reveals exactly what needs correcting
- The Feynman Technique works both ways: ask the learner to explain it back to you in their own words
- For visual learners, describe diagrams even in text: "imagine a vertical number line with zero in the middle…"
- When teaching math or logic, always do one example where you make a deliberate mistake, catch it, and correct it — this models the debugging mindset
- Break the concept into the smallest possible pieces and confirm each piece before adding the next
- End sessions with a "one thing to remember" summary — memory research shows spaced retrieval beats re-reading every time

## Related Skills
- [quiz-creator](../quiz-creator/SKILL.md)
- [lesson-planner](../lesson-planner/SKILL.md)
- [flashcard-maker](../flashcard-maker/SKILL.md)
