---
name: documentation-writer
description: "Use this skill when writing or improving technical documentation including READMEs, docstrings, API docs, changelogs, or inline code comments. Trigger phrases: 'write a README', 'document this function', 'add docstrings', 'improve the docs'. Not for writing blog posts, marketing copy, or user-facing help articles."
version: 1.0.0
author: community
tags: [coding, documentation, readme, docstrings, comments]
license: MIT
---

# Documentation Writer

## Overview
The Documentation Writer skill produces clear, accurate, and maintainable technical documentation across all layers: project-level READMEs, module-level docstrings, function-level API docs, and inline code comments. It covers the standard formats for multiple languages (JSDoc, Python docstrings in Google/NumPy/Sphinx style, GoDoc), README structure best practices, CHANGELOG format (Keep a Changelog), and principles for writing comments that add value rather than noise. Good documentation is part of the code — it reduces onboarding time, prevents misuse, and serves as a contract with consumers.

## When to Use
- Writing a README for a new library, tool, or service
- Adding docstrings to functions, classes, or modules
- Documenting a public API for external or internal consumers
- Writing or updating a CHANGELOG when releasing a new version
- Adding inline comments to explain non-obvious logic

## When NOT to Use
- Writing user-facing help docs or tutorials (different audience and tone)
- Writing blog posts or marketing copy
- Generating API reference docs from non-annotated code (annotate first, then generate)
- Writing architectural decisions (use the architecture-designer skill for ADRs)

## Quick Reference
| Doc Type | Purpose | Format |
|----------|---------|--------|
| README | Project overview, quickstart, usage | Markdown with badges, code blocks, TOC |
| Docstring (Python) | Function/class contract | Google, NumPy, or Sphinx style |
| JSDoc | JS/TS function/class docs | `/** @param @returns @throws */` |
| GoDoc | Go package/function docs | Plain comment above declaration |
| Inline comment | Explain *why*, not *what* | Sparingly; 1-2 lines |
| CHANGELOG | User-facing change history | Keep a Changelog format |
| OpenAPI | REST API reference | YAML/JSON, generated from annotations |

## Instructions

1. **Know your audience**
   - **README**: New users who need to evaluate, install, and get started quickly.
   - **Docstrings**: Developers who will call your function — they need to know the contract (parameters, return values, exceptions, side effects), not the implementation.
   - **Inline comments**: The developer maintaining this code 6 months from now (possibly you).
   - **CHANGELOG**: Users upgrading — they need to know what changed and if they need to do anything.

2. **Write the README with this structure**
   ```
   1. Project name + one-line tagline
   2. Badges (CI, coverage, version, license)
   3. Short description (2-3 sentences, why does this exist?)
   4. Quick Start / Installation (fewest steps to get running)
   5. Usage with code examples
   6. Configuration reference
   7. API reference (or link to generated docs)
   8. Contributing guide
   9. License
   ```

3. **Write docstrings for every public function, class, and module**
   - Describe *what* it does, not *how* (don't repeat the code).
   - Document every parameter with type and description.
   - Document the return value with type and description.
   - Document every exception that can be raised and when.
   - Include a usage example for non-trivial functions.

4. **Write inline comments that explain *why*, not *what***
   - Bad: `i += 1  # increment i` (the code already says this)
   - Good: `# Skip the header row — it's not data`
   - Good: `# Retry up to 3 times to handle transient network errors`
   - Comment non-obvious algorithms, workarounds, and performance-critical decisions.

5. **Maintain the CHANGELOG**
   - Follow Keep a Changelog: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
   - Each release has a version number and date.
   - Write from the user's perspective: "what changed for me?" not "what did we do?"

6. **Review and update docs with code changes**
   - Treat outdated documentation as a bug.
   - Update docstrings when function signatures, behavior, or exceptions change.
   - Update the README when installation steps, config options, or usage patterns change.

## Examples

### Example 1: Write a README for an open-source Python library

**Input:** "Write a README for `quickcache`, a Python library that provides a simple decorator for caching function results with TTL support."

**Output:**

````markdown
# quickcache

[![CI](https://github.com/example/quickcache/actions/workflows/ci.yml/badge.svg)](https://github.com/example/quickcache/actions)
[![PyPI version](https://badge.fury.io/py/quickcache.svg)](https://pypi.org/project/quickcache/)
[![Coverage](https://codecov.io/gh/example/quickcache/branch/main/graph/badge.svg)](https://codecov.io/gh/example/quickcache)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple, zero-dependency Python decorator for caching function results with optional time-to-live (TTL) expiration. Stop re-computing expensive results on every call.

## Quick Start

```bash
pip install quickcache
```

```python
from quickcache import cache

@cache(ttl=60)  # Cache for 60 seconds
def get_user(user_id: int) -> dict:
    return database.fetch_user(user_id)

user = get_user(42)   # Hits the database
user = get_user(42)   # Returns cached result instantly
```

## Features

- ✅ Simple decorator API
- ✅ Configurable TTL (time-to-live) per function
- ✅ Supports sync and async functions
- ✅ Thread-safe in-memory cache
- ✅ Optional Redis backend for distributed caching
- ✅ Zero dependencies (in-memory mode)

## Installation

```bash
pip install quickcache          # In-memory caching (zero dependencies)
pip install quickcache[redis]   # Redis backend
```

## Usage

### Basic caching

```python
from quickcache import cache

@cache()
def expensive_computation(x: int, y: int) -> int:
    """Cached with no TTL — cached until process restarts."""
    return x ** y
```

### With TTL

```python
@cache(ttl=300)  # Cache for 5 minutes
def fetch_exchange_rate(currency: str) -> float:
    return api.get_rate(currency)
```

### Async support

```python
@cache(ttl=60)
async def fetch_user_async(user_id: int) -> dict:
    return await db.fetch_user(user_id)
```

### Redis backend (distributed)

```python
from quickcache import cache
from quickcache.backends import RedisBackend

backend = RedisBackend(host='localhost', port=6379, db=0)

@cache(ttl=120, backend=backend)
def get_product(product_id: int) -> dict:
    return db.fetch_product(product_id)
```

### Cache invalidation

```python
from quickcache import cache, invalidate

@cache(ttl=60, key='user:{user_id}')
def get_user(user_id: int) -> dict:
    return db.fetch_user(user_id)

# Invalidate a specific user's cache
invalidate('user:42')

# Invalidate by function
get_user.invalidate(42)

# Clear all cache
get_user.clear()
```

## Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ttl` | `int \| None` | `None` | Seconds before cache entry expires. `None` = never expires. |
| `backend` | `Backend` | `MemoryBackend()` | Cache backend instance. |
| `key` | `str \| None` | Auto | Cache key template. Use `{param_name}` for dynamic keys. |
| `maxsize` | `int` | `1024` | Max entries for in-memory backend (LRU eviction). |

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the development setup, coding standards, and pull request process.

```bash
git clone https://github.com/example/quickcache.git
cd quickcache
pip install -e ".[dev]"
pytest
```

## License

MIT — see [LICENSE](LICENSE).
````

---

### Example 2: Document a Python module with docstrings

**Input:** A Python module to document:
```python
import re
from typing import Optional

def validate_email(email, strict=False):
    pattern = r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$'
    if strict:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email, re.IGNORECASE))

def normalize_email(email):
    local, domain = email.rsplit('@', 1)
    local = local.split('+')[0]
    return f"{local.lower()}@{domain.lower()}"

class EmailValidator:
    def __init__(self, allowed_domains=None):
        self.allowed_domains = set(allowed_domains or [])

    def is_valid(self, email):
        if not validate_email(email):
            return False
        if self.allowed_domains:
            domain = email.rsplit('@', 1)[1].lower()
            return domain in self.allowed_domains
        return True
```

**Output (with Google-style docstrings):**
```python
"""Email validation and normalization utilities.

This module provides functions and a class for validating and normalizing
email addresses. It supports basic RFC-compliant validation, strict mode
for stricter character rules, and domain allowlisting.

Typical usage::

    from email_utils import validate_email, normalize_email, EmailValidator

    if validate_email("alice@example.com"):
        canonical = normalize_email("Alice+tag@Example.COM")
        # canonical == "alice@example.com"

    validator = EmailValidator(allowed_domains=["company.com"])
    validator.is_valid("alice@company.com")   # True
    validator.is_valid("alice@gmail.com")     # False
"""

import re
from typing import Optional


def validate_email(email: str, strict: bool = False) -> bool:
    """Validate whether a string is a well-formed email address.

    Uses a regex pattern to check that the email has a valid local part,
    an @ symbol, a domain, and a TLD of at least 2 characters. Strict mode
    disallows some special characters (e.g., `!`, `#`) in the local part.

    Args:
        email: The email address string to validate.
        strict: If True, applies stricter character rules in the local part
            (only alphanumeric, dots, underscores, percent, plus, hyphen).
            Defaults to False.

    Returns:
        True if the email matches the pattern; False otherwise.

    Examples:
        >>> validate_email("alice@example.com")
        True
        >>> validate_email("not-an-email")
        False
        >>> validate_email("alice!@example.com", strict=True)
        False
    """
    pattern = r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$'
    if strict:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email, re.IGNORECASE))


def normalize_email(email: str) -> str:
    """Normalize an email address to its canonical form.

    Strips the plus-addressing suffix from the local part and lowercases
    both the local part and the domain. This enables deduplication of
    addresses like ``Alice+newsletter@Example.COM`` and ``alice@example.com``.

    Note:
        This function does not validate the email. Call ``validate_email``
        first if you need to ensure the input is well-formed.

    Args:
        email: A well-formed email address string.

    Returns:
        The normalized email address in lowercase with plus-addressing removed.

    Raises:
        ValueError: If the email does not contain an ``@`` symbol.

    Examples:
        >>> normalize_email("Alice+tag@Example.COM")
        'alice@example.com'
        >>> normalize_email("BOB@COMPANY.ORG")
        'bob@company.org'
    """
    if '@' not in email:
        raise ValueError(f"Invalid email address (missing @): {email!r}")
    local, domain = email.rsplit('@', 1)
    local = local.split('+')[0]
    return f"{local.lower()}@{domain.lower()}"


class EmailValidator:
    """Validates email addresses with optional domain allowlisting.

    Combines format validation with domain restriction. Useful for
    ensuring that only users with addresses from specific domains
    (e.g., corporate email) can register.

    Attributes:
        allowed_domains: A set of lowercase domain strings that are
            permitted. Empty set means all domains are allowed.

    Example:
        >>> validator = EmailValidator(allowed_domains=["company.com", "company.org"])
        >>> validator.is_valid("alice@company.com")
        True
        >>> validator.is_valid("bob@gmail.com")
        False
        >>> open_validator = EmailValidator()
        >>> open_validator.is_valid("anyone@anywhere.io")
        True
    """

    def __init__(self, allowed_domains: Optional[list[str]] = None) -> None:
        """Initialize the validator with an optional domain allowlist.

        Args:
            allowed_domains: A list of permitted email domains (case-insensitive).
                If None or empty, all domains are allowed.
        """
        self.allowed_domains = {d.lower() for d in (allowed_domains or [])}

    def is_valid(self, email: str) -> bool:
        """Check whether an email address is valid and from an allowed domain.

        Args:
            email: The email address to validate.

        Returns:
            True if the email passes format validation and (if configured)
            its domain is in the allowlist. False otherwise.
        """
        if not validate_email(email):
            return False
        if self.allowed_domains:
            domain = email.rsplit('@', 1)[1].lower()
            return domain in self.allowed_domains
        return True
```

**JSDoc equivalent (TypeScript):**
```typescript
/**
 * Validates whether a string is a well-formed email address.
 *
 * @param email - The email address string to validate.
 * @param strict - If true, applies stricter character rules in the local part.
 * @returns `true` if the email matches the expected pattern; `false` otherwise.
 *
 * @example
 * ```ts
 * validateEmail("alice@example.com");       // true
 * validateEmail("not-an-email");             // false
 * validateEmail("alice!@example.com", true); // false (strict mode)
 * ```
 */
export function validateEmail(email: string, strict = false): boolean {
  const pattern = strict
    ? /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/i
    : /^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$/i;
  return pattern.test(email);
}
```

**GoDoc equivalent:**
```go
// Package email provides utilities for validating and normalizing email addresses.
//
// Example usage:
//
//	if email.IsValid("alice@example.com") {
//	    canonical := email.Normalize("Alice+tag@Example.COM")
//	    fmt.Println(canonical) // alice@example.com
//	}
package email

// IsValid reports whether s is a well-formed email address.
// It uses a regex-based heuristic and is suitable for most real-world
// validation purposes. For strict RFC 5321 compliance, use IsValidStrict.
func IsValid(s string) bool { ... }

// Normalize returns the canonical form of the email address by lowercasing
// both the local part and domain, and stripping any plus-addressing suffix
// (e.g., "Alice+tag@Example.COM" → "alice@example.com").
//
// Normalize does not validate the email. Call IsValid first if needed.
func Normalize(s string) (string, error) { ... }
```

## Best Practices
- Write docs before or alongside code, not as an afterthought
- Keep docs close to the code they describe — co-located docstrings beat separate wiki pages
- Treat documentation as code: review it in PRs, update it with behavior changes
- Use examples liberally — a usage example is worth more than three paragraphs of prose
- Make the first sentence of a docstring a complete, standalone description (it appears in IDE tooltips and auto-generated indexes)

## Common Mistakes
- Restating what the code does ("This function increments x by 1") instead of explaining purpose and contract
- Documenting parameters without types or units (is `timeout` in ms or seconds?)
- Outdated docs that contradict the current behavior — worse than no docs
- Missing exception documentation — callers can't handle errors they don't know about
- Documenting private/internal implementation details that may change vs. the stable public API

## Tips & Tricks
- `pydoc`, `sphinx`, `typedoc`, and `godoc` generate HTML API references from docstrings automatically
- Keep a Changelog (keepachangelog.com) is the standard CHANGELOG format — follow it consistently
- Use `# TODO(username): reason` format for deferred work so it's trackable
- Add examples to docstrings that are also run as doctests in Python: `pytest --doctest-modules`
- Badge generators: shields.io creates badges for README (CI status, version, license, coverage)

## Related Skills
- [api-designer](../api-designer/SKILL.md)
- [code-reviewer](../code-reviewer/SKILL.md)
- [refactorer](../refactorer/SKILL.md)
- [test-writer](../test-writer/SKILL.md)
