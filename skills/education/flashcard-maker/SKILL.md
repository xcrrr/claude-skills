---
name: flashcard-maker
description: "Use this skill when creating Q&A flashcard decks optimized for spaced repetition and memorization. Triggers: 'make flashcards for', 'create an Anki deck', 'turn these notes into flashcards', 'I need to memorize'. Not for writing practice tests with multiple-choice options, generating essay prompts, or producing study guides with explanatory prose."
version: 1.0.0
author: community
tags: [education, flashcards, spaced-repetition, memorization]
license: MIT
---

# Flashcard Maker

## Overview
The Flashcard Maker skill generates high-quality Q&A flashcard decks designed for efficient long-term memorization through spaced repetition. Each card follows atomicity principles — one discrete fact per card — with clear, unambiguous questions and precise answers. Cards include optional context notes or mnemonics to aid encoding. Output is formatted for compatibility with Anki (tab-separated or CSV import), Quizlet, or plain text. The skill handles vocabulary, definitions, formulas, processes, dates, anatomy, code syntax, and more across any academic or professional domain.

## When to Use
- Memorizing vocabulary in a foreign language or technical domain
- Learning medical, legal, or scientific terminology for professional certification
- Studying historical dates, names, events, and cause-effect relationships
- Memorizing programming syntax, API methods, keyboard shortcuts, or command flags
- Converting lecture notes, textbook chapters, or study guides into discrete, reviewable facts
- Building Anki decks for spaced repetition study schedules

## When NOT to Use
- Creating multiple-choice practice exams or quiz assessments (use the quiz-creator skill)
- Writing explanatory study guides or concept summaries with connected prose
- Designing lesson plans or teaching materials for a classroom context
- Generating project-based learning tasks or open-ended essay prompts
- Memorizing complex multi-step processes where understanding relationships matters more than recall

## Quick Reference
| Task | Approach |
|------|----------|
| Anki-compatible output | Request tab-separated format: `Question[TAB]Answer[TAB]Note` |
| Atomic card design | One fact per card; split compound facts into separate cards |
| Mnemonic inclusion | Ask for a memory hook or acronym in the Note column |
| Cloze deletion cards | Request `{{c1::answer}}` Anki cloze syntax for fill-in-the-blank style |
| Reverse cards | Request both Q→A and A→Q pairs for bidirectional recall |
| Tagging by topic | Ask for an Anki tag column to organize decks by chapter or category |

## Instructions

1. **Identify the subject domain and scope** — Confirm the topic (e.g., "Spanish A1 vocabulary," "pharmacology drug classes," "Python built-in functions") and the source material (provided text, a list of terms, or a concept the model should generate cards for from its knowledge).

2. **Define card format requirements** — Clarify the target application (Anki tab-separated CSV, Quizlet plain text, flashcard prose), whether cloze deletions or Q&A pairs are preferred, and whether reverse cards (A→Q) are needed alongside forward cards (Q→A).

3. **Apply the atomicity principle** — Break complex facts into the smallest independently testable unit. For example, instead of "List all symptoms of appendicitis," create one card per symptom. Compound questions reduce recall efficiency.

4. **Write precise, unambiguous questions** — Frame each question so that exactly one correct answer exists. Avoid vague stems like "What is important about X?" Prefer specific prompts: "What is the primary function of the mitochondria?" or "What Python method removes and returns the last item of a list?"

5. **Craft concise, complete answers** — Answers should be short enough to hold in working memory (under 20 words when possible) but complete enough to be unambiguous. For definitions, include the core meaning and one distinguishing characteristic.

6. **Add context notes and mnemonics** — For each card, optionally include a third field: a memory hook, etymology, example sentence, or contextual note that aids encoding without being required for the recall cue.

7. **Group and tag cards by subtopic** — When generating large decks (20+ cards), organize by category using Anki tags (e.g., `Chapter1`, `Verbs`, `Pharmacology::Antibiotics`) to enable filtered review sessions.

8. **Include image or diagram references where relevant** — For anatomy, chemistry, or geography cards, note where a diagram or image would enhance the card and suggest a placeholder or source.

9. **Review for duplication and overlap** — Scan generated cards for near-duplicate questions. Merge redundant cards and eliminate any that test knowledge covered more precisely by another card in the deck.

10. **Output the final deck in the requested format** — Deliver cards in the specified format (tab-separated, numbered list, Markdown table) with a card count summary and suggested study schedule (e.g., "Start with 20 new cards/day, review due cards daily").

## Examples

### Example 1: Spanish A1 Vocabulary Deck — Common Verbs
**Input:** "Create 10 Anki flashcards for Spanish A1 common verbs: ser, estar, tener, hacer, ir, poder, querer, saber, venir, decir. Include English meaning, example sentence, and a usage note distinguishing ser vs. estar if relevant."

**Output:**
```
#separator:tab
#html:false
#deck:Spanish A1 — Common Verbs
#tags:Spanish A1 Verbs

QUESTION	ANSWER	NOTE
What does "ser" mean in Spanish, and when is it used?	To be (permanent/inherent qualities): identity, origin, time, characteristics.	Example: "Ella es médica." (She is a doctor.) Use ser for things unlikely to change. Tag: ser-vs-estar
What does "estar" mean, and when is it used instead of "ser"?	To be (temporary states/conditions): emotions, location, ongoing actions.	Example: "Estoy cansado." (I am tired.) Use estar for states that can change. Tag: ser-vs-estar
What does "tener" mean? Give an example.	To have (possession, obligation, age). Example: "Tengo veinte años." (I am twenty years old.)	Note: Spanish uses tener for age ("tener X años"), not ser. Tag: tener
What does "hacer" mean? Give an example.	To do / to make. Example: "Hago la tarea." (I do the homework.)	Also used in weather expressions: "Hace frío." (It's cold.) Tag: hacer
What does "ir" mean? Conjugate in present tense (yo form).	To go. Yo: voy. Example: "Voy al mercado." (I'm going to the market.)	Ir + a + infinitive = near future: "Voy a comer." (I'm going to eat.) Tag: ir
What does "poder" mean? Give an example.	To be able to / can. Example: "¿Puedes ayudarme?" (Can you help me?)	Stem-changing verb: o→ue (puedo, puedes, puede…). Tag: poder
What does "querer" mean? Give two uses.	To want / to love. Want: "Quiero agua." Love (person): "Te quiero." (I love you, informal.)	Stem-changing: e→ie (quiero, quieres…). Tag: querer
What does "saber" mean, and how does it differ from "conocer"?	To know (facts, information, how to do something). "Sé nadar." (I know how to swim.)	Conocer = to know/be acquainted with people/places. Saber = factual knowledge. Tag: saber
What does "venir" mean? Give an example.	To come. Example: "Vengo de España." (I come from Spain.)	Irregular yo form: vengo. Stem-changing: e→ie (vienes, viene…). Tag: venir
What does "decir" mean? Give an example.	To say / to tell. Example: "¿Qué dices?" (What are you saying?)	Irregular yo form: digo. Common phrase: "Es decir…" (That is to say…). Tag: decir

--- SUMMARY ---
Total cards: 10
Suggested schedule: 5 new cards/day × 2 days, then daily review of due cards.
Study tip: Use the ser-vs-estar tag for a focused filtered deck session.
```

### Example 2: Medical Terminology Deck — Cardiovascular System
**Input:** "Make 12 Anki flashcards on cardiovascular medical terminology for a nursing student. Include: myocardial infarction, arrhythmia, bradycardia, tachycardia, hypertension, hypotension, angina pectoris, atherosclerosis, thrombosis, embolism, ischemia, ejection fraction. Use cloze deletion format."

**Output:**
```
#separator:tab
#html:false
#deck:Medical Terminology — Cardiovascular
#tags:MedTerms Cardiovascular Nursing

CLOZE CARD	NOTE
{{c1::Myocardial infarction}} is the medical term for a heart attack, caused by prolonged blockage of a coronary artery.	From Greek: myo (muscle) + kardia (heart) + Latin: infarctus (stuffed). Key sign: elevated troponin levels.
{{c1::Arrhythmia}} refers to any abnormal heart rhythm, including rates that are too fast, too slow, or irregular.	Prefix: a- (without) + Greek rhythmos (rhythm). Includes AFib, VFib, SVT. Detected by ECG/EKG.
A heart rate below 60 beats per minute is called {{c1::bradycardia}}.	Brady- (Greek: slow) + kardia. May be normal in athletes; pathological with dizziness/syncope.
A heart rate above 100 beats per minute is called {{c1::tachycardia}}.	Tachy- (Greek: swift) + kardia. Sinus tachycardia is often a response to fever, anxiety, or blood loss.
{{c1::Hypertension}} is defined as persistent blood pressure ≥130/80 mmHg (AHA 2017 guidelines).	Hyper- (over) + Latin tensio (tension). "Silent killer" — often asymptomatic. Risk: stroke, MI, renal failure.
Blood pressure that is abnormally low (typically <90/60 mmHg) is called {{c1::hypotension}}.	Hypo- (under) + tensio. Symptoms: dizziness, syncope. Causes: dehydration, sepsis, cardiac failure.
{{c1::Angina pectoris}} is chest pain caused by reduced blood flow to the heart muscle, often relieved by rest or nitroglycerin.	Latin: angere (to strangle) + pectoris (of the chest). Stable angina = exertion; Unstable = rest.
{{c1::Atherosclerosis}} is the buildup of plaques (lipids, cholesterol, inflammatory cells) inside arterial walls, reducing lumen diameter.	Athero- (Greek: gruel/paste) + sclerosis (hardening). Primary cause of CAD, MI, and peripheral artery disease.
{{c1::Thrombosis}} is the formation of a blood clot (thrombus) inside a blood vessel, obstructing blood flow.	Thrombos (Greek: lump, clot). DVT (deep vein thrombosis) can lead to pulmonary embolism.
An {{c1::embolism}} occurs when a clot or other material travels through the bloodstream and lodges in a vessel, blocking flow.	Embolos (Greek: plug). Pulmonary embolism = clot in pulmonary artery. Contrast with thrombosis (clot forms in situ).
{{c1::Ischemia}} is insufficient blood supply to tissue, leading to oxygen deprivation and potential cell death.	Greek: ischein (to hold back) + haima (blood). Myocardial ischemia → angina or MI if prolonged.
{{c1::Ejection fraction (EF)}} is the percentage of blood the left ventricle pumps out with each contraction; normal is 55–70%.	EF < 40% = reduced EF heart failure (HFrEF). Measured via echocardiogram. Key metric for heart function assessment.

--- SUMMARY ---
Total cards: 12 (cloze deletion format)
Deck tag: Cardiovascular
Suggested schedule: 6 new cards/day × 2 days; daily review of due cards.
Study tip: Create a companion image card with a labeled heart diagram using the same tags.
```

## Best Practices
- Follow the minimum information principle: one discrete, testable fact per card
- Write questions that have exactly one correct answer — ambiguity destroys recall efficiency
- Include a mnemonic, etymology, or vivid example in the note field for abstract or arbitrary facts
- Use cloze deletions for fill-in-the-blank recall; use Q&A pairs for definition and conceptual cards
- Tag cards by chapter, difficulty, or topic so learners can create filtered review sessions
- For foreign language decks, include a native-language example sentence on every vocabulary card
- Generate reverse cards (A→Q) for vocabulary to build both recognition and production recall

## Common Mistakes
- Writing cards that are too long or test multiple facts at once — violates the atomicity principle
- Using vague question stems ("What is important about X?") that permit multiple valid answers
- Omitting context notes — bare Q&A pairs with no examples are harder to encode into long-term memory
- Creating cards for concepts that require understanding of relationships, not memorization — use a study guide instead
- Mixing cloze and Q&A formats in the same deck without labeling them — causes import errors in Anki
- Generating cards from a topic without reviewing them for duplication, especially in large decks

## Tips & Tricks
- For Anki import, always include `#separator:tab` and `#html:false` headers at the top of the file
- Use the `{{c1::}}` `{{c2::}}` syntax to create multiple cloze deletions on one card for sentence completion practice
- Request "image occlusion" card instructions when studying anatomy diagrams — Anki's Image Occlusion plugin works well
- Break large topics (50+ terms) into sub-decks by chapter or category to prevent overwhelm
- Ask for cards in both English-to-target-language AND target-language-to-English directions for vocabulary acquisition
- Add a "difficulty rating" note (Easy / Medium / Hard) so learners can prioritize review sessions
- For exam prep, request cards organized by exam topic weighting to study high-yield content first

## Related Skills
- [tutor](../tutor/SKILL.md)
- [quiz-creator](../quiz-creator/SKILL.md)
- [lesson-planner](../lesson-planner/SKILL.md)
