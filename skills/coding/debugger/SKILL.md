---
name: debugger
description: "Use this skill when tracking down a bug, understanding an error message, or diagnosing unexpected behavior in code. Trigger phrases: 'this is broken', 'I'm getting an error', 'why does this crash', 'help me debug'. Not for code review of working code or designing new features."
version: 1.0.0
author: community
tags: [coding, debugging, troubleshooting, error-analysis]
license: MIT
---

# Debugger

## Overview
The Debugger skill applies a systematic five-step methodology — Reproduce → Isolate → Hypothesize → Test → Fix — to diagnose and resolve software bugs efficiently. It covers reading stack traces, identifying common error patterns across languages, and using targeted strategies to narrow down root causes. Rather than guessing, this skill drives debugging as a structured investigation that produces a verified fix and prevents regression.

## When to Use
- You have an error message, stack trace, or crash report to analyze
- Code produces unexpected output or behavior
- A test is failing and you don't know why
- An intermittent bug needs to be made reproducible
- You need to understand what a piece of code is actually doing vs. what you thought it did

## When NOT to Use
- You want a general code quality review (use the code-reviewer skill)
- You are designing a new system or feature from scratch
- You need to optimize a working system for performance (use a profiler workflow)
- The issue is an environment/infrastructure problem (networking, DNS, containers) rather than code logic

## Quick Reference
| Step | Action |
|------|--------|
| Reproduce | Confirm the bug exists with a minimal, reliable test case |
| Isolate | Narrow down which file, function, or line causes it |
| Hypothesize | Form a specific, falsifiable theory about the root cause |
| Test | Prove or disprove the hypothesis with targeted experiments |
| Fix | Apply the smallest correct change; verify and add a regression test |
| Stack traces | Read bottom-up (root cause) then top-down (propagation) |
| KeyError/IndexError | Check key existence before access; validate collection lengths |
| TypeError | Inspect actual types at runtime, not assumed types |
| Off-by-one | Trace loop bounds; use closed/open interval notation |
| Async bugs | Log execution order; check promise chaining and race conditions |

## Instructions

1. **Reproduce the bug reliably**
   - Get the exact steps to reproduce. If you can't reproduce it, you can't verify your fix.
   - Reduce the reproduction case to the smallest possible input that still triggers the bug.
   - Identify whether the bug is deterministic, intermittent, or environment-specific.
   - Record: OS, language/runtime version, relevant library versions, inputs, expected output, actual output.

2. **Read the error message and stack trace carefully**
   - Read the stack trace **bottom-up**: the bottom frame is usually where the error originated.
   - Read it **top-down** to see how it propagated to the surface.
   - Extract: error type, error message, file name, line number, function name.
   - Look for your own code in the stack — frames from frameworks are usually symptoms, not causes.

3. **Isolate the failure**
   - Use binary search: comment out half the code and see if the error persists. Narrow to a section, then a function, then a line.
   - Add logging/print statements at key boundaries to trace values.
   - Use `git bisect` if the bug appeared recently to find the introducing commit.
   - Write a failing unit test that captures the bug — this isolates it and becomes your regression guard.

4. **Hypothesize the root cause**
   - Form a specific, falsifiable hypothesis: "The bug occurs because `X` is `None` when the function expects a string."
   - List all assumptions the code makes and check each one.
   - Consider: wrong type, off-by-one, uninitialized variable, wrong variable, mutation side effect, async race condition, missing null check.

5. **Test the hypothesis**
   - Add a targeted assertion or log to confirm or deny the hypothesis before changing code.
   - Run the reproduction case with the added diagnostic.
   - If the hypothesis is disproved, form a new one — do not change code until you have confirmed the root cause.

6. **Apply the fix**
   - Make the minimal change that correctly addresses the root cause (not just the symptom).
   - Re-run the reproduction case to confirm the bug is gone.
   - Run the full test suite to confirm no regression.
   - Add a regression test if one doesn't exist.

7. **Document the fix**
   - Write a clear commit message: what changed, why, and a reference to the issue.
   - Leave a comment in the code if the fix is non-obvious.

## Examples

### Example 1: Debug a Python KeyError

**Input:**
```
Traceback (most recent call last):
  File "app.py", line 42, in process_order
    discount = DISCOUNT_MAP[user['tier']]
KeyError: 'gold'
```

Code:
```python
DISCOUNT_MAP = {
    'silver': 0.05,
    'platinum': 0.20,
}

def process_order(user, order_total):
    discount = DISCOUNT_MAP[user['tier']]
    return order_total * (1 - discount)
```

**Output:**

**Step 1 – Read the trace**
The error is on line 42: `DISCOUNT_MAP[user['tier']]`. The key `'gold'` does not exist in `DISCOUNT_MAP`.

**Step 2 – Hypothesis**
`DISCOUNT_MAP` is missing the `'gold'` tier that some users have. The code assumes the map is exhaustive.

**Step 3 – Confirm**
```python
print(user['tier'])  # prints 'gold'
print(DISCOUNT_MAP.keys())  # dict_keys(['silver', 'platinum'])
```

**Step 4 – Fix**
Option A — add the missing key:
```python
DISCOUNT_MAP = {
    'silver': 0.05,
    'gold': 0.10,
    'platinum': 0.20,
}
```
Option B — use a safe default for unknown tiers:
```python
discount = DISCOUNT_MAP.get(user['tier'], 0.0)
```

**Regression test:**
```python
def test_process_order_unknown_tier():
    user = {'tier': 'bronze'}
    result = process_order(user, 100.0)
    assert result == 100.0  # no discount for unknown tier
```

---

### Example 2: Debug a React state update issue

**Input:**
```jsx
function Counter() {
  const [count, setCount] = useState(0);

  function handleTripleClick() {
    setCount(count + 1);
    setCount(count + 1);
    setCount(count + 1);
  }

  return <button onClick={handleTripleClick}>Count: {count}</button>;
}
```
Symptom: clicking the button only increments count by 1, not 3.

**Output:**

**Step 1 – Reproduce**
The button increments `count` from 0 to 1, never to 3, regardless of how many times `setCount` is called in the handler.

**Step 2 – Hypothesis**
React batches state updates within an event handler. All three calls to `setCount(count + 1)` read the *same stale closure value* of `count` (e.g., `0`), so all three calls set count to `1`.

**Step 3 – Confirm**
Add a log:
```jsx
function handleTripleClick() {
  console.log('before:', count); // logs 0 all three times
  setCount(count + 1);
  setCount(count + 1);
  setCount(count + 1);
}
```

**Step 4 – Fix**
Use the **functional updater form** of `setCount` which receives the latest state value, not the closed-over value:
```jsx
function handleTripleClick() {
  setCount(prev => prev + 1);
  setCount(prev => prev + 1);
  setCount(prev => prev + 1);
}
```
Now each call receives the result of the previous update, so count correctly reaches 3.

**Regression test:**
```js
test('triple click increments by 3', async () => {
  render(<Counter />);
  const btn = screen.getByRole('button');
  await userEvent.click(btn);
  expect(btn).toHaveTextContent('Count: 3');
});
```

## Best Practices
- Never change code to fix a bug until you have confirmed the root cause — you may fix a symptom and leave the root cause in place
- Always write a failing test first that captures the bug before fixing it
- Use the scientific method: one hypothesis, one experiment, one result at a time
- Keep a short "debugging journal" for complex bugs to avoid revisiting dead ends
- `print`/`console.log` debugging is valid — use it freely, then clean up
- Check assumptions at every step: types, values, order of execution, scope

## Common Mistakes
- Fixing symptoms instead of root causes (the bug returns in a different form)
- Changing multiple things at once and not knowing which change fixed it
- Assuming the bug is in your code when it's in a library (or vice versa)
- Skipping reproduction and trying to reason about the bug abstractly
- Forgetting to check environment differences (local vs CI, dev vs prod, Python 3.10 vs 3.11)
- Not adding a regression test after fixing, allowing the bug to recur

## Tips & Tricks
- `git bisect` is the fastest way to find a regression in a large commit history
- Rubber duck debugging: explain the bug out loud step by step — the explanation often reveals the answer
- For async/concurrency bugs, add timestamps to logs to see actual execution order
- Browser DevTools "Break on exception" or Python's `pdb.post_mortem()` drops you into the frame where the error occurred
- For intermittent bugs, log everything and search for patterns across multiple occurrences

## Related Skills
- [code-reviewer](../code-reviewer/SKILL.md)
- [test-writer](../test-writer/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
