---
name: prompt-engineer
description: "Use this skill when crafting, iterating, or optimizing prompts for LLMs including zero-shot, few-shot, chain-of-thought, role prompting, structured output, and prompt chaining. Not for fine-tuning or training models. Not for evaluating model quality across benchmarks."
version: 1.0.0
author: community
tags: [ai, prompt-engineering, llm, optimization]
license: MIT
---

# Prompt Engineer

## Overview
This skill covers systematic design and iteration of prompts for large language models (LLMs). It applies proven techniques — zero-shot, few-shot learning, chain-of-thought reasoning, role prompting, structured output constraints, system prompt design, and multi-step prompt chaining — to improve accuracy, consistency, and reliability of LLM outputs. The skill is applicable to any LLM API (OpenAI, Anthropic, Gemini, Mistral, open-source models) and covers both single-turn and multi-turn conversation design, as well as production-grade prompt templates with variable injection.

## When to Use
- A prompt produces inconsistent, vague, or off-format outputs and needs iteration
- Designing prompts that must return structured JSON, XML, Markdown, or CSV output
- Building few-shot examples to guide classification, extraction, or transformation tasks
- Creating system prompts that establish persona, tone, constraints, or output rules
- Chaining multiple prompts together for complex multi-step reasoning tasks
- Reducing hallucination by adding grounding instructions, citations requirements, or self-checks
- Optimizing a prompt for a specific model (GPT-4, Claude, Llama, etc.) given its strengths
- Converting a vague user request into a precise, production-ready prompt template

## When NOT to Use
- Fine-tuning or training a model on new data (use model training skills)
- Evaluating model quality across a benchmark suite (use eval-designer skill)
- Writing application code that calls the LLM API (use a coding skill)
- Comparing different LLMs for a use case (use model-comparator skill)
- RAG pipeline design (retrieval-augmented generation requires its own architecture skill)

## Quick Reference
| Task | Approach |
|------|----------|
| Get consistent structured output | Add explicit format spec + JSON schema example in the prompt |
| Improve reasoning accuracy | Use chain-of-thought: "Think step by step before answering" |
| Classify text reliably | Provide 2–3 labeled few-shot examples per class |
| Set model persona and constraints | Write a detailed system prompt before the user turn |
| Handle long complex tasks | Break into a prompt chain with intermediate outputs |
| Reduce hallucinations | Instruct model to cite sources or say "I don't know" explicitly |
| Make outputs deterministic | Lower temperature + explicit format constraints |

## Instructions

1. **Define the task precisely** — Write a one-sentence task definition: what the model must do, what the input is, and what the output must look like. Vague tasks produce vague outputs. Example: "Extract all company names and their associated revenue figures from the following earnings call transcript and return them as a JSON array."

2. **Choose the prompting technique** — Select based on task complexity:
   - **Zero-shot**: Simple tasks with clear instructions. No examples needed.
   - **Few-shot**: Classification, formatting, or style tasks. Provide 2–5 labeled examples.
   - **Chain-of-thought (CoT)**: Math, logic, multi-step reasoning. Add "Think step by step."
   - **Role prompting**: Tasks requiring expertise or persona. "You are a senior tax attorney…"
   - **Self-consistency**: Run the same CoT prompt N times and majority-vote the answer.
   - **Prompt chaining**: Decompose a complex task into sequential prompts where each feeds the next.

3. **Write the system prompt** — For APIs that support system prompts (OpenAI, Anthropic), put persistent instructions here: role, output format, constraints, what to do when uncertain. Keep it under 500 tokens unless the task genuinely requires more context.

4. **Structure the user prompt** — Use clear delimiters to separate instructions from input data. Use XML tags (`<document>`, `<query>`), triple backticks, or `---` separators. Place instructions before the data, not after.

5. **Specify output format explicitly** — Tell the model exactly what format to use. If JSON, provide the schema or a filled example. If Markdown, show the heading structure. If a list, show how items should be formatted. Include a negative example if there is a common wrong format to avoid.

6. **Add few-shot examples** — For classification or extraction tasks, include 2–5 examples in the prompt. Format them identically to the real input/output pair. Choose examples that cover edge cases and are representative of the real distribution.

7. **Iterate and test** — Test on at least 10 representative inputs. Track: did the model follow the format? Did it hallucinate? Was the reasoning correct? Identify failure patterns and add instructions or examples to address them.

8. **Version and document the prompt** — Save prompts in a template file with variable placeholders (`{{input}}`). Document what model version it was tested on, what temperature, and what the expected pass rate is.

9. **Optimize for the target model** — Different models respond differently: Claude prefers XML tags and explicit role instructions; GPT-4 responds well to numbered instructions; open-source models often need more explicit format constraints. Test the same prompt on the target model even if it worked on another.

10. **Add safety and fallback instructions** — Include: what to do if the input is out of scope, how to handle ambiguous inputs, whether to ask for clarification or make a best-effort attempt, and how to indicate low confidence.

## Examples

### Example 1: Improving a Vague Prompt to Get Structured JSON Output
**Input:**
```
Original vague prompt: "Summarize this customer review and tell me if it's positive or negative."
```

**Output:**

**Improved prompt (system + user):**
```
SYSTEM:
You are a sentiment analysis assistant. You always respond with valid JSON only — no prose, no markdown fences. If you cannot determine sentiment, set "sentiment" to "unknown" and explain in "reason".

USER:
Analyze the following customer review. Return a JSON object with exactly these fields:
{
  "sentiment": "positive" | "negative" | "neutral" | "unknown",
  "confidence": 0.0–1.0,
  "key_themes": ["theme1", "theme2"],
  "summary": "one sentence summary",
  "reason": "brief explanation of sentiment classification"
}

Review:
<review>
{{customer_review_text}}
</review>
```

**Why this works:**
- System prompt enforces JSON-only output at the model level
- Explicit schema with types eliminates ambiguity
- XML tag delimiter prevents the model from treating the review text as instructions
- `"unknown"` fallback prevents hallucinated confident answers
- `confidence` field enables downstream filtering of low-quality classifications

### Example 2: Few-Shot Chain-of-Thought Prompt for Legal Clause Classification
**Input:**
```
Task: Classify contract clauses as "liability-limiting", "indemnification", "IP-assignment", or "other".
The model keeps misclassifying indemnification clauses as liability-limiting.
```

**Output:**

**Few-shot CoT system prompt:**
```
SYSTEM:
You are a contract analysis assistant specializing in clause classification. Think through each clause step by step before classifying. Respond only in the format shown in the examples.

USER:
Classify each contract clause. Think step by step, then provide your classification.

---
EXAMPLE 1:
Clause: "Neither party shall be liable for indirect, incidental, or consequential damages arising out of this agreement."
Reasoning: This clause restricts what types of damages can be claimed. It limits liability exposure — it does not require one party to protect another. This is a liability cap, not an indemnification.
Classification: liability-limiting

---
EXAMPLE 2:
Clause: "Vendor shall indemnify, defend, and hold harmless Client from any third-party claims arising from Vendor's breach of this agreement."
Reasoning: This clause requires the Vendor to actively protect the Client from external claims. It creates an obligation to defend and compensate — this is indemnification, not merely limiting damages.
Classification: indemnification

---
EXAMPLE 3:
Clause: "All work product created by Contractor under this agreement is assigned to Client upon creation."
Reasoning: This clause transfers ownership of created works. It concerns who owns intellectual property, not liability or indemnification.
Classification: IP-assignment

---
Now classify this clause:
Clause: "{{clause_text}}"
Reasoning:
```

**Why this works:**
- Chain-of-thought examples show the model the reasoning pattern to distinguish similar categories
- The two easily-confused categories (liability vs indemnification) each get an explicit contrasting example
- Format template forces reasoning before classification, reducing snap-judgment errors
- `Reasoning:` at the end primes the model to complete the reasoning before the answer

## Best Practices
- Always test prompts on at least 10 real inputs before declaring them production-ready
- Version prompts in code just like application code — breaking changes in prompts are real bugs
- Use the lowest effective temperature: 0.0 for deterministic extraction, 0.7–1.0 for creative tasks
- Prefer XML tags over triple backticks as delimiters — they're less likely to appear in real input
- Put the most important instructions at the beginning AND end of the prompt (primacy + recency effect)
- When using few-shot examples, ensure they cover the edge cases you care about most
- Keep system prompts focused — every sentence should earn its token budget
- Use "You must" and "Always" for hard constraints; use "prefer" or "try to" for soft preferences

## Common Mistakes
- Giving vague instructions like "be helpful and accurate" without specifying what accuracy means
- Not specifying what to do when the model is uncertain — it will hallucinate a confident answer
- Using too many few-shot examples (>10) which can cause the model to pattern-match instead of reason
- Forgetting to test the prompt on the actual target model — prompts are not portable across models
- Putting instructions after the input data — models weight early context more heavily
- Asking multiple distinct tasks in one prompt — split into separate prompts or clearly numbered steps
- Assuming the same prompt works at different temperatures — always co-tune prompt and temperature

## Tips & Tricks
- Add "Do not add any text before or after the JSON" to enforce clean parseable JSON output
- Use "If you are unsure, say 'I don't know' rather than guessing" to reduce hallucination
- For long documents, use "Here is the most relevant section:" before the content to focus attention
- Chain-of-thought is most effective in the middle of a response — put format instructions last
- "Let's think step by step" reliably improves math and logic; for simpler tasks it wastes tokens
- Test prompt robustness by deliberately injecting adversarial inputs (e.g., "ignore previous instructions")
- Use Anthropic's Constitutional AI principles or OpenAI's system prompt best practices as references

## Related Skills
- [dataset-curator](../dataset-curator/SKILL.md)
- [eval-designer](../eval-designer/SKILL.md)
- [model-comparator](../model-comparator/SKILL.md)
