#!/usr/bin/env python3
"""
generate_readme.py — Auto-generates the skill library tables in README.md
from SKILL.md frontmatter across all skills directories.

Usage: python scripts/generate_readme.py
"""

import re
import sys
from pathlib import Path
import yaml

SKILLS_ROOT = Path(__file__).parent.parent / "skills"
README_PATH = Path(__file__).parent.parent / "README.md"

CATEGORY_EMOJI = {
    "writing":      "✍️",
    "coding":       "💻",
    "data":         "📊",
    "business":     "💼",
    "research":     "🔬",
    "design":       "🎨",
    "productivity": "⚡",
    "legal":        "⚖️",
    "finance":      "💰",
    "education":    "🎓",
    "devops":       "🛠️",
    "ai-ml":        "🤖",
    "files":        "📄",
}

CATEGORY_ORDER = list(CATEGORY_EMOJI.keys())


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    raw = text[3:end].strip()
    try:
        data = yaml.safe_load(raw) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def build_tables() -> str:
    categories: dict[str, list[tuple[str, str]]] = {}

    for skill_md in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        parts = skill_md.relative_to(SKILLS_ROOT).parts
        if len(parts) < 3:
            continue
        category = parts[0]
        skill_dir = parts[1]

        fm = read_frontmatter(skill_md)
        description = fm.get("description", "No description provided.")
        # Strip trailing period if present
        description = description.rstrip(".")

        rel_path = f"skills/{category}/{skill_dir}"
        entry = (skill_dir, description, rel_path)
        categories.setdefault(category, []).append(entry)

    lines = []
    for category in CATEGORY_ORDER:
        if category not in categories:
            continue
        emoji = CATEGORY_EMOJI.get(category, "")
        display = category.replace("-", "/").title().replace("Ai/Ml", "AI/ML").replace("Devops", "DevOps")
        lines.append(f"### {emoji} {display}\n")
        lines.append("| Skill | Description |")
        lines.append("|---|---|")
        for skill_dir, description, rel_path in sorted(categories[category]):
            lines.append(f"| [{skill_dir}]({rel_path}/) | {description} |")
        lines.append("")

    return "\n".join(lines)


def update_readme(new_tables: str) -> None:
    content = README_PATH.read_text(encoding="utf-8")

    # Replace everything between the "## 📚 Skill Library" heading
    # and the "## 🚀 How to Use" heading
    pattern = re.compile(
        r"(## 📚 Skill Library\n).*?(## 🚀 How to Use)",
        re.DOTALL
    )
    replacement = f"## 📚 Skill Library\n\n{new_tables}\n---\n\n## 🚀 How to Use"
    new_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        print("ERROR: Could not find the Skill Library section in README.md. "
              "Make sure the headings '## 📚 Skill Library' and '## 🚀 How to Use' exist.")
        sys.exit(1)

    README_PATH.write_text(new_content, encoding="utf-8")
    print(f"README.md updated successfully with {len(new_tables)} chars of skill tables.")


if __name__ == "__main__":
    tables = build_tables()
    update_readme(tables)
    print("Done.")
