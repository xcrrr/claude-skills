---
name: code-reviewer
description: "Use this skill when reviewing pull requests, auditing code quality, or providing structured feedback on code. Trigger phrases: 'review this code', 'check my PR', 'what's wrong with this', 'give feedback on'. Not for writing new code from scratch or debugging runtime errors."
version: 1.0.0
author: community
tags: [coding, code-review, quality, best-practices]
license: MIT
---

# Code Reviewer

## Overview
The Code Reviewer skill provides a structured, systematic approach to evaluating code for correctness, security, performance, readability, and maintainability. It helps deliver actionable, prioritized feedback using defined severity levels so authors know exactly what must be fixed versus what is a suggestion. This skill draws on established best practices to ensure reviews are constructive, thorough, and consistent.

## When to Use
- Reviewing a pull request before merging
- Auditing a module or file for quality issues
- Providing mentorship feedback on another developer's code
- Self-reviewing your own code before submitting
- Evaluating third-party or open-source code before adopting it

## When NOT to Use
- Writing new features from scratch (use a code-generation skill instead)
- Debugging a runtime error with a stack trace (use the debugger skill)
- Profiling performance bottlenecks with tooling (use a profiler workflow)
- Reviewing non-code artifacts like diagrams or documentation prose

## Quick Reference
| Task | Approach |
|------|----------|
| Find correctness issues | Trace logic paths, check edge cases, verify inputs/outputs |
| Find security issues | OWASP checklist, look for injection, exposure of secrets |
| Find performance issues | Check complexity, N+1 queries, unnecessary allocations |
| Find readability issues | Variable naming, function length, comment quality |
| Find maintainability issues | Coupling, cohesion, test coverage, duplication |
| Assign severity | Critical → Major → Minor → Nit |
| Write actionable feedback | State the issue, explain why, suggest the fix |

## Instructions

1. **Understand the context** — Read the PR description, linked issue, or stated goal. Know what the code is supposed to do before critiquing it.

2. **Run a high-level pass** — Scan the overall structure. Identify the files changed, the patterns used, and the approach taken. Flag architectural concerns at this stage.

3. **Apply the correctness checklist**:
   - Does the logic match the requirements?
   - Are edge cases handled (null, empty, zero, max values)?
   - Are error conditions caught and handled gracefully?
   - Are external calls (APIs, DBs) wrapped with error handling?

4. **Apply the security checklist**:
   - Is user input validated and sanitized before use?
   - Are secrets, tokens, or credentials hardcoded?
   - Is data properly escaped before rendering (XSS)?
   - Are SQL queries parameterized (no string concatenation)?
   - Are authorization checks in place on every sensitive operation?

5. **Apply the performance checklist**:
   - Are there nested loops with O(n²) or worse complexity?
   - Are database queries inside loops (N+1 problem)?
   - Are expensive operations cached where appropriate?
   - Are large payloads paginated or streamed?

6. **Apply the readability checklist**:
   - Are names descriptive and consistent with the codebase conventions?
   - Are functions short and single-purpose?
   - Is complex logic explained with comments?
   - Is dead code or commented-out code removed?

7. **Apply the maintainability checklist**:
   - Is there significant code duplication (DRY violations)?
   - Are tests included for new or changed logic?
   - Is the code properly modular and loosely coupled?
   - Does the change follow existing patterns in the project?

8. **Assign severity to each finding**:
   - **Critical** — Must fix before merge. Causes bugs, data loss, or security vulnerabilities.
   - **Major** — Should fix before merge. Significant quality or correctness problem.
   - **Minor** — Fix in a follow-up. Code smell or style inconsistency.
   - **Nit** — Optional polish. Purely aesthetic or preference-based.

9. **Write feedback** — For each finding, state: (a) what the issue is, (b) why it matters, (c) how to fix it. Use line references. Be respectful and specific.

10. **Summarize** — End with an overall assessment: Approve, Request Changes (with blockers listed), or Comment (non-blocking suggestions only).

## Examples

### Example 1: Review a Python function with bugs

**Input:**
```python
def get_user_discount(user_id, db):
    user = db.query("SELECT * FROM users WHERE id = " + user_id)
    if user['role'] == 'premium':
        discount = 0.2
    elif user['role'] == 'vip':
        discount = 0.35
    return discount
```

**Output:**

**[Critical] SQL Injection Vulnerability** (line 2)
The `user_id` is concatenated directly into the SQL string. An attacker can pass `'; DROP TABLE users; --` as `user_id`.
Fix: Use parameterized queries:
```python
user = db.query("SELECT * FROM users WHERE id = %s", (user_id,))
```

**[Critical] NameError on unmatched role** (line 6–7)
If `user['role']` is neither `'premium'` nor `'vip'` (e.g., `'standard'`), `discount` is never assigned and the `return` statement raises `UnboundLocalError`.
Fix: Add a default:
```python
discount = 0.0  # default at top of function
```

**[Major] No error handling for missing user** (line 2)
If `user_id` doesn't exist, `db.query()` likely returns `None`, causing a `TypeError` on `user['role']`.
Fix:
```python
if not user:
    return 0.0
```

**[Minor] Magic numbers** (lines 4, 6)
`0.2` and `0.35` have no explanation. Use named constants:
```python
PREMIUM_DISCOUNT = 0.20
VIP_DISCOUNT = 0.35
```

**Overall: Request Changes** — Two critical issues block merge.

---

### Example 2: Review a JavaScript React component

**Input:**
```jsx
function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/api/users')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      {users.map(u => (
        <div onClick={() => deleteUser(u.id)}>
          {u.name} - {u.email}
        </div>
      ))}
    </div>
  );
}
```

**Output:**

**[Critical] Missing key prop in list** (line 12)
React requires a unique `key` on list items. Without it, reconciliation produces incorrect UI updates.
Fix: `<div key={u.id} onClick={...}>`

**[Major] Unhandled fetch error** (lines 5–8)
If the network request fails, the error is silently swallowed. Users see a blank list with no feedback.
Fix:
```jsx
.catch(err => {
  console.error('Failed to load users:', err);
  setError('Could not load users. Please try again.');
});
```

**[Major] `deleteUser` is not defined** (line 13)
The `deleteUser` function is referenced but never imported or declared in this component. This will throw a `ReferenceError` at runtime.

**[Minor] Implicit any on fetch response**
`data` has no type annotation. If using TypeScript, add: `.then((data: User[]) => setUsers(data))`.

**[Nit] Variable name `u`**
Consider `user` instead of `u` for clarity in the map callback.

**Overall: Request Changes** — Critical key prop missing; undefined function reference.

## Best Practices
- Review for the author's benefit, not to show off your knowledge
- Always explain *why* something is an issue, not just *what* it is
- Separate objective issues (bugs, security) from subjective preferences (style)
- Acknowledge what is done well — reviews should reinforce good patterns too
- Keep individual comments concise; link to docs or RFCs for deeper context
- Batch nits at the bottom rather than peppering them throughout
- If you'd write it differently but the current approach also works, mark it `[Nit]` or `[Suggestion]`

## Common Mistakes
- Reviewing style while missing security flaws — prioritize severity order
- Writing vague feedback like "this is bad" without explaining why or how to fix it
- Blocking a PR on personal preferences dressed up as standards
- Reviewing the same code multiple times without acknowledging changes
- Missing the overall design in favor of line-by-line nitpicking
- Forgetting to check test coverage changes alongside the implementation

## Tips & Tricks
- Read the tests first — they reveal intent and what the author thought mattered
- Run the code locally if possible before reviewing; reading code misses runtime behavior
- Use a checklist template so every review covers the same dimensions consistently
- Split large PRs: ask the author to break them up if reviewing end-to-end is too costly
- Look at the git diff stat first to size the review before diving into files

## Related Skills
- [debugger](../debugger/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
- [test-writer](../test-writer/SKILL.md)
- [refactorer](../refactorer/SKILL.md)
