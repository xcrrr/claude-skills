#!/usr/bin/env python3
"""
validate_skills.py — Validates all SKILL.md files in the skills/ directory.

Checks:
  - YAML frontmatter presence and required fields
  - All 10 required sections present and in the correct order
  - Examples section contains at least 2 examples
  - Exits with code 1 if any validation fails
"""

import os
import re
import sys
from pathlib import Path
import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SKILLS_ROOT = Path(__file__).parent.parent / "skills"

REQUIRED_FRONTMATTER_FIELDS = ["name", "description", "version", "author", "tags", "license"]

REQUIRED_SECTIONS = [
    "Overview",
    "When to Use",
    "When NOT to Use",
    "Quick Reference",
    "Instructions",
    "Examples",
    "Best Practices",
    "Common Mistakes",
    "Tips & Tricks",
    "Related Skills",
]

# Minimum number of "### Example N" subsections required inside ## Examples
MIN_EXAMPLES = 2

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """
    Extract YAML frontmatter from a Markdown file using PyYAML.
    Returns (fields_dict, body_text). fields_dict is empty if no frontmatter found.
    """
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    raw = text[3:end].strip()
    body = text[end + 4:]

    try:
        fields = yaml.safe_load(raw) or {}
        if not isinstance(fields, dict):
            return {}, body
    except yaml.YAMLError:
        return {}, body

    return fields, body


def _mask_code_blocks(text: str) -> str:
    """
    Replace the content of fenced code blocks with spaces, preserving character positions.

    This prevents headings inside code blocks (e.g. inside a ```markdown example) from
    being mistakenly detected as section headings by the section parser.
    Handles both backtick (```) and tilde (~~~) fences, including 4-backtick fences.
    """
    result = list(text)
    lines = text.split("\n")
    pos = 0
    in_fence = False
    fence_char = ""
    fence_len = 0

    for line in lines:
        line_end = pos + len(line)
        if not in_fence:
            m = re.match(r"^(`{3,}|~{3,})", line)
            if m:
                in_fence = True
                fence_char = m.group(1)[0]
                fence_len = len(m.group(1))
        else:
            m = re.match(r"^(`{3,}|~{3,})\s*$", line)
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len:
                in_fence = False
                fence_char = ""
                fence_len = 0
            else:
                # Mask this line's non-newline characters so headings inside
                # code blocks are not detected by the section regex.
                for i in range(pos, line_end):
                    result[i] = " "
        pos = line_end + 1  # +1 for the newline character

    return "".join(result)


def extract_sections(body: str) -> dict[str, str]:
    """
    Parse ## Level-2 headings and return a mapping of heading text -> section content.

    Headings that appear inside fenced code blocks are ignored.
    """
    sections: dict[str, str] = {}
    masked = _mask_code_blocks(body)
    pattern = re.compile(r"^## (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(masked))

    for i, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        # Extract content from the original (unmasked) body using positions from masked body
        sections[heading] = body[start:end].strip()

    return sections


def count_examples(examples_body: str) -> int:
    """Count ### Example subsections within the Examples section body."""
    return len(re.findall(r"^###\s+Example", examples_body, re.MULTILINE | re.IGNORECASE))


# ---------------------------------------------------------------------------
# Validation logic
# ---------------------------------------------------------------------------


class ValidationResult:
    def __init__(self, path: Path):
        self.path = path
        self.errors: list[str] = []

    def fail(self, msg: str) -> None:
        self.errors.append(msg)

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0


def validate_file(skill_md: Path) -> ValidationResult:
    result = ValidationResult(skill_md)
    text = skill_md.read_text(encoding="utf-8")

    # ------------------------------------------------------------------
    # 1. Frontmatter
    # ------------------------------------------------------------------
    fields, body = extract_frontmatter(text)

    if not fields:
        result.fail("Missing YAML frontmatter (file must start with ---)")
    else:
        for field in REQUIRED_FRONTMATTER_FIELDS:
            if field not in fields or not fields[field]:
                result.fail(f"Frontmatter missing required field: '{field}'")

        # tags must be a list
        if "tags" in fields and not isinstance(fields["tags"], list):
            result.fail("Frontmatter 'tags' must be a list (e.g. [\"tag1\", \"tag2\"])")

        # license must be MIT
        if "license" in fields and fields.get("license", "").upper() != "MIT":
            result.fail(f"Frontmatter 'license' must be 'MIT', got: '{fields.get('license')}'")

        # version must look like semver
        version = fields.get("version", "")
        if version and not re.match(r"^\d+\.\d+\.\d+$", version):
            result.fail(f"Frontmatter 'version' must be semver (e.g. 1.0.0), got: '{version}'")

    # ------------------------------------------------------------------
    # 2. Required sections — presence
    # ------------------------------------------------------------------
    sections = extract_sections(body)

    for section in REQUIRED_SECTIONS:
        if section not in sections:
            result.fail(f"Missing required section: '## {section}'")

    # ------------------------------------------------------------------
    # 3. Required sections — correct order
    # ------------------------------------------------------------------
    present_sections = [s for s in REQUIRED_SECTIONS if s in sections]
    section_positions: dict[str, int] = {}
    masked_body = _mask_code_blocks(body)
    for section in present_sections:
        pattern = re.compile(rf"^## {re.escape(section)}$", re.MULTILINE)
        m = pattern.search(masked_body)
        if m:
            section_positions[section] = m.start()

    ordered_positions = [section_positions[s] for s in present_sections if s in section_positions]
    if ordered_positions != sorted(ordered_positions):
        result.fail("Required sections are out of order. Expected order: " +
                    ", ".join(REQUIRED_SECTIONS))

    # ------------------------------------------------------------------
    # 4. Examples section — minimum count
    # ------------------------------------------------------------------
    if "Examples" in sections:
        n = count_examples(sections["Examples"])
        if n < MIN_EXAMPLES:
            result.fail(
                f"'## Examples' must contain at least {MIN_EXAMPLES} '### Example' subsections, "
                f"found {n}"
            )

    # ------------------------------------------------------------------
    # 5. Instructions section — must contain at least one {{variable}} or non-trivial content
    # ------------------------------------------------------------------
    if "Instructions" in sections:
        instructions_body = sections["Instructions"]
        if len(instructions_body.strip()) < 50:
            result.fail("'## Instructions' section appears too short (< 50 characters). "
                        "Provide a complete prompt template.")

    # ------------------------------------------------------------------
    # 6. Related Skills — verify linked files exist
    # ------------------------------------------------------------------
    if "Related Skills" in sections:
        related_body = sections["Related Skills"]
        link_pattern = re.compile(r'\[.*?\]\((.*?\.md)\)')
        for match in link_pattern.finditer(related_body):
            link_path = match.group(1)
            resolved = (skill_md.parent / link_path).resolve()
            if not resolved.exists():
                result.fail(f"Broken link in '## Related Skills': '{link_path}' does not exist")

    return result


# ---------------------------------------------------------------------------
# Scanner
# ---------------------------------------------------------------------------


def find_skill_files(root: Path) -> list[Path]:
    """Recursively find all SKILL.md files under root."""
    return sorted(root.rglob("SKILL.md"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 60)
    print("claude-skills validator")
    print("=" * 60)

    if not SKILLS_ROOT.exists():
        print(f"\n[ERROR] Skills directory not found: {SKILLS_ROOT}")
        return 1

    skill_files = find_skill_files(SKILLS_ROOT)

    if not skill_files:
        print("\n[WARN] No SKILL.md files found. Nothing to validate.")
        return 0

    print(f"\nFound {len(skill_files)} SKILL.md file(s) to validate.\n")

    results: list[ValidationResult] = []
    for skill_file in skill_files:
        result = validate_file(skill_file)
        results.append(result)

        relative = skill_file.relative_to(SKILLS_ROOT.parent)
        status = "✅ PASS" if result.passed else "❌ FAIL"
        print(f"  {status}  {relative}")

        for error in result.errors:
            print(f"           └─ {error}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    passed = [r for r in results if r.passed]
    failed = [r for r in results if not r.passed]

    print()
    print("=" * 60)
    print(f"Results: {len(passed)} passed, {len(failed)} failed out of {len(results)} total")
    print("=" * 60)

    if failed:
        print("\nFailed files:")
        for r in failed:
            relative = r.path.relative_to(SKILLS_ROOT.parent)
            print(f"  • {relative}")
            for error in r.errors:
                print(f"      - {error}")
        print()
        return 1

    print("\nAll skills passed validation! 🎉")
    return 0


if __name__ == "__main__":
    sys.exit(main())
