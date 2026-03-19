# Contributing to claude-skills

Thank you for your interest in contributing! This library grows stronger with every new skill, improvement, and fix the community provides. This document explains everything you need to know to make a great contribution.

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold a welcoming, respectful, and inclusive environment. Please report unacceptable behavior to the maintainers.

---

## How to Add a New Skill

### 1. Check for duplicates

Before starting, search the [existing skills](skills/) to make sure a similar skill doesn't already exist. If a related skill exists and your idea is an improvement, consider opening an issue to discuss whether to extend the existing skill or add a new one.

### 2. Fork and clone

```bash
git clone https://github.com/<your-username>/claude-skills.git
cd claude-skills
git checkout -b skill/your-skill-name
```

### 3. Choose the right category

Place your skill under the most appropriate category directory:

| Category | Path | Examples |
|---|---|---|
| Writing | `skills/writing/` | blog-post, copywriter |
| Coding | `skills/coding/` | debugger, test-writer |
| Data | `skills/data/` | data-analyst, excel-expert |
| Business | `skills/business/` | product-manager, okr-planner |
| Research | `skills/research/` | fact-checker, summarizer |
| Design | `skills/design/` | ux-writer, color-palette |
| Productivity | `skills/productivity/` | task-planner, decision-maker |
| Legal | `skills/legal/` | contract-reviewer |
| Finance | `skills/finance/` | budget-planner |
| Education | `skills/education/` | tutor, quiz-creator |
| DevOps | `skills/devops/` | docker-expert, ci-cd-helper |
| AI/ML | `skills/ai-ml/` | prompt-engineer, eval-designer |
| Files | `skills/files/` | docx, pdf |

If your skill doesn't fit any existing category, propose a new one in your PR description.

### 4. Create the skill directory and SKILL.md

```bash
mkdir -p skills/<category>/<skill-name>
touch skills/<category>/<skill-name>/SKILL.md
```

Skill directory names must be:
- **Lowercase** with hyphens (kebab-case), e.g., `email-drafter`
- **Descriptive** but concise (1–3 words)
- **Unique** across the entire library

### 5. Write your SKILL.md

Follow the exact format described in the [SKILL.md Format](#skillmd-format-requirements) section below.

### 6. Validate your skill

```bash
python scripts/validate_skills.py
```

All checks must pass before opening a PR. Fix any reported errors.

### 7. Update the README table

Add a row for your skill to the appropriate category table in `README.md`. Match the existing format exactly.

### 8. Open a pull request

Push your branch and open a PR against `main`. Use this PR template:

```
## New Skill: <skill-name>

**Category:** <category>
**Description:** <one-line description>

### Why this skill?
<2–3 sentences explaining the use case and who benefits>

### Checklist
- [ ] SKILL.md follows the required format
- [ ] validate_skills.py passes with no errors
- [ ] README.md table updated
- [ ] Examples are real, not fabricated
- [ ] No copyrighted content included
```

---

## SKILL.md Format Requirements

Every `SKILL.md` must begin with a YAML frontmatter block and contain all required sections in order.

### Frontmatter

```yaml
---
name: "Human-Readable Skill Name"
description: "One-sentence description of what this skill does."
version: "1.0.0"
author: "your-github-username"
tags: ["tag1", "tag2", "tag3"]
license: "MIT"
---
```

| Field | Type | Rules |
|---|---|---|
| `name` | string | Title case, max 50 characters |
| `description` | string | Single sentence, max 120 characters, no period |
| `version` | string | Semantic version (`MAJOR.MINOR.PATCH`) |
| `author` | string | GitHub username of primary author |
| `tags` | list of strings | 2–6 lowercase tags relevant to the skill |
| `license` | string | Must be `"MIT"` |

### Required Sections

All sections must appear **in this order**, with these **exact headings**:

#### 1. `## Overview`
2–4 sentences describing what the skill does, what problem it solves, and who it's for. Do not repeat the frontmatter description verbatim.

#### 2. `## When to Use`
A bullet list of 3–6 concrete scenarios where this skill delivers the most value.

#### 3. `## When NOT to Use`
A bullet list of 2–4 scenarios where this skill is a poor fit or where a different skill would serve better. Include references to related skills where applicable.

#### 4. `## Quick Reference`
A compact "cheat sheet" block — key variables, parameters, or options a user needs to know at a glance. Use a code block, table, or short bullet list.

#### 5. `## Instructions`
The full prompt template. Use `{{double_braces}}` for variables the user must fill in. This section must be self-contained: a user should be able to copy it verbatim (after filling variables) and get excellent results.

#### 6. `## Examples`
At least **2 complete, worked examples**. Each example must include:
- A `### Example N: <Title>` heading
- **Input:** the filled-in prompt (or a summary of the user's request)
- **Output:** the actual Claude response (or a realistic representative excerpt)

Examples must be realistic and non-trivial. Do not use "Lorem ipsum" or placeholder text.

#### 7. `## Best Practices`
4–8 bullet points of actionable advice for getting the most out of this skill.

#### 8. `## Common Mistakes`
3–6 bullet points describing frequent errors users make and how to avoid them.

#### 9. `## Tips & Tricks`
3–5 bullet points of advanced techniques, lesser-known options, or power-user suggestions.

#### 10. `## Related Skills`
A list of 2–5 other skills in this library that complement or extend this one. Use relative Markdown links.

---

## Quality Checklist

Before submitting, confirm every item:

- [ ] Frontmatter is valid YAML with all 6 required fields
- [ ] All 10 required sections are present and in order
- [ ] Section headings match exactly (case-sensitive)
- [ ] At least 2 worked examples with real Input/Output
- [ ] `{{variables}}` are used for all user-supplied values
- [ ] No copyrighted text, brand names, or trademarks without permission
- [ ] No personally identifiable information (PII) in examples
- [ ] No fabricated statistics or citations
- [ ] `validate_skills.py` reports PASS
- [ ] README.md table row added

---

## PR Review Criteria

Maintainers evaluate PRs on:

| Criterion | What we look for |
|---|---|
| **Correctness** | Prompt produces accurate, reliable results for its stated purpose |
| **Completeness** | All sections present, examples are substantive |
| **Clarity** | Instructions are unambiguous; variables are well-named |
| **Originality** | Not a trivial duplicate of an existing skill |
| **Quality of examples** | Examples are realistic, representative, and educational |
| **Formatting** | Consistent Markdown, correct frontmatter, passes validator |

We aim to review PRs within **7 days**. If your PR sits unreviewed for longer, feel free to ping us in the issue tracker.

---

## Improving Existing Skills

To improve an existing skill:

1. Open an **issue** first if the change is significant (e.g., restructuring Instructions, changing examples).
2. For minor fixes (typos, formatting, broken links), a direct PR is fine.
3. Bump the `version` field in frontmatter following semver:
   - Patch (`1.0.x`): typo fixes, formatting
   - Minor (`1.x.0`): new examples, expanded sections
   - Major (`x.0.0`): significant rewrite of Instructions

---

## Questions?

Open a [GitHub Discussion](https://github.com/xcrrr/claude-skills/discussions) for questions, ideas, or feedback. For bugs or concrete issues, open an [Issue](https://github.com/xcrrr/claude-skills/issues).

We're grateful for every contribution — thank you for making claude-skills better! 🙏
