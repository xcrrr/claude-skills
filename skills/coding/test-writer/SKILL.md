---
name: test-writer
description: "Use this skill when writing unit tests, integration tests, or end-to-end tests for existing or new code. Trigger phrases: 'write tests for', 'add test coverage', 'how do I test this', 'TDD this feature'. Not for running or debugging test infrastructure or CI pipelines."
version: 1.0.0
author: community
tags: [coding, testing, unit-tests, tdd, jest]
license: MIT
---

# Test Writer

## Overview
The Test Writer skill produces comprehensive, maintainable tests following established practices: the test pyramid (unit → integration → e2e), the AAA (Arrange-Act-Assert) pattern, meaningful naming conventions, and effective mocking strategies. It helps determine what to test, how to structure test files, what to mock vs. not mock, and how to set coverage targets. Good tests serve as executable documentation that catches regressions before they reach production.

## When to Use
- Writing tests for a new function, class, or module
- Adding tests to untested legacy code before refactoring
- Following Test-Driven Development (TDD) — writing tests before implementation
- Evaluating test coverage and identifying what's missing
- Writing integration tests for API endpoints or database interactions

## When NOT to Use
- Setting up CI/CD pipelines or test runners (infrastructure concern)
- Load testing or performance benchmarking (different tooling)
- Writing end-to-end browser automation scripts (use a Playwright/Cypress skill)
- Debugging a failing test (use the debugger skill to find the root cause)

## Quick Reference
| Level | Scope | Speed | Mock? | Target % |
|-------|-------|-------|-------|----------|
| Unit | Single function/class | Fast (<1ms) | Dependencies | 70–80% of tests |
| Integration | Multiple modules + real DB/API | Medium (10–100ms) | External services only | 15–25% of tests |
| E2E | Full user journey through UI | Slow (1–30s) | Nothing | 5–10% of tests |

| Concept | Description |
|---------|-------------|
| AAA | Arrange (set up) → Act (call) → Assert (verify) |
| Naming | `describe('unit') / it('should behavior when condition')` |
| Mocking | Replace dependencies with controlled test doubles |
| Coverage target | 80% line coverage; 100% on critical paths |
| TDD cycle | Red → Green → Refactor |

## Instructions

1. **Identify the unit under test**
   - Pick a single function, method, or class as the subject.
   - List all inputs, outputs, side effects, and error conditions.
   - Identify dependencies that need to be mocked (databases, HTTP clients, file system, clocks).

2. **Choose the right test level**
   - **Unit test**: test a function in isolation with all dependencies mocked.
   - **Integration test**: test multiple real components together (e.g., service + real DB).
   - **E2E test**: test a full user-facing workflow through the actual UI or API.

3. **Identify test cases**
   - Happy path: the function works correctly with valid input.
   - Edge cases: empty string, empty array, zero, null, very large numbers, boundary values.
   - Error cases: invalid input, dependency throws, timeout.
   - State variations: first-time user vs. returning user; empty list vs. full list.

4. **Apply the AAA pattern to each test**
   ```
   // Arrange — set up test data and mocks
   // Act — call the function under test
   // Assert — verify the output or side effects
   ```

5. **Apply naming conventions**
   - Describe block: name of the unit under test — `describe('calculateDiscount')`
   - It block: "should [expected behavior] when [condition]" — `it('should return 0 when cart is empty')`
   - Test file: co-locate with source or mirror directory structure: `utils.test.ts`, `utils.spec.py`

6. **Mock strategically**
   - Mock I/O boundaries: databases, HTTP calls, file system, time, random.
   - Do NOT mock the thing you're testing.
   - Do NOT mock value objects or pure functions — use real instances.
   - Prefer dependency injection over module-level patching for testability.

7. **Assert precisely**
   - Assert on the exact expected value, not just that "something was called."
   - Verify side effects: was the correct database method called with the correct args?
   - For error cases: assert the exact error type and message.
   - Avoid asserting on internal implementation details that could change without breaking behavior.

8. **Check coverage**
   - Run coverage report; target 80%+ line coverage on business logic.
   - 100% coverage on security-critical paths (auth, payment, data validation).
   - Untested branches show up as risk — prioritize covering error paths.

## Examples

### Example 1: Write unit tests for a utility function (JavaScript/Jest)

**Input:** A `calculateDiscount` function to test:
```javascript
// discount.js
export function calculateDiscount(price, userTier) {
  if (price <= 0) throw new Error('Price must be positive');
  const rates = { silver: 0.05, gold: 0.10, platinum: 0.20 };
  const rate = rates[userTier] ?? 0;
  return Math.round(price * rate * 100) / 100;
}
```

**Output:**
```javascript
// discount.test.js
import { calculateDiscount } from './discount';

describe('calculateDiscount', () => {
  describe('happy path', () => {
    it('should apply 5% discount for silver tier', () => {
      // Arrange
      const price = 100;
      const tier = 'silver';

      // Act
      const result = calculateDiscount(price, tier);

      // Assert
      expect(result).toBe(5.00);
    });

    it('should apply 10% discount for gold tier', () => {
      expect(calculateDiscount(100, 'gold')).toBe(10.00);
    });

    it('should apply 20% discount for platinum tier', () => {
      expect(calculateDiscount(100, 'platinum')).toBe(20.00);
    });

    it('should return 0 discount for unknown tier', () => {
      expect(calculateDiscount(100, 'bronze')).toBe(0);
    });

    it('should return 0 discount when tier is undefined', () => {
      expect(calculateDiscount(100, undefined)).toBe(0);
    });

    it('should round to 2 decimal places', () => {
      // $99.99 * 5% = 4.9995 → rounds to 5.00
      expect(calculateDiscount(99.99, 'silver')).toBe(5.00);
    });
  });

  describe('error cases', () => {
    it('should throw when price is zero', () => {
      expect(() => calculateDiscount(0, 'gold')).toThrow('Price must be positive');
    });

    it('should throw when price is negative', () => {
      expect(() => calculateDiscount(-50, 'gold')).toThrow('Price must be positive');
    });
  });

  describe('edge cases', () => {
    it('should handle very small positive price', () => {
      expect(calculateDiscount(0.01, 'platinum')).toBe(0.00);
    });

    it('should handle very large price', () => {
      expect(calculateDiscount(1_000_000, 'platinum')).toBe(200_000);
    });
  });
});
```

---

### Example 2: Write an integration test for an API endpoint (Node.js/Jest + Supertest)

**Input:** An Express endpoint to test:
```javascript
// routes/users.js
router.post('/users', async (req, res) => {
  const { email, name } = req.body;
  if (!email) return res.status(422).json({ error: 'email is required' });
  const existing = await db.users.findByEmail(email);
  if (existing) return res.status(409).json({ error: 'email already in use' });
  const user = await db.users.create({ email, name });
  return res.status(201).json(user);
});
```

**Output:**
```javascript
// routes/users.integration.test.js
import request from 'supertest';
import { app } from '../app';
import { db } from '../db';

// Use a real test database — no mocking of db layer
beforeAll(async () => { await db.migrate.latest(); });
afterAll(async () => { await db.destroy(); });
afterEach(async () => { await db.raw('DELETE FROM users'); }); // clean state

describe('POST /users', () => {
  describe('successful creation', () => {
    it('should create a user and return 201 with user data', async () => {
      // Arrange
      const payload = { email: 'alice@example.com', name: 'Alice' };

      // Act
      const res = await request(app).post('/users').send(payload);

      // Assert
      expect(res.status).toBe(201);
      expect(res.body).toMatchObject({
        id: expect.any(String),
        email: 'alice@example.com',
        name: 'Alice',
        createdAt: expect.any(String),
      });
      // Verify persisted to DB
      const saved = await db.users.findByEmail('alice@example.com');
      expect(saved).not.toBeNull();
    });
  });

  describe('validation errors', () => {
    it('should return 422 when email is missing', async () => {
      const res = await request(app).post('/users').send({ name: 'Bob' });
      expect(res.status).toBe(422);
      expect(res.body.error).toBe('email is required');
    });
  });

  describe('conflict errors', () => {
    it('should return 409 when email already exists', async () => {
      // Arrange — seed an existing user
      await db.users.create({ email: 'carol@example.com', name: 'Carol' });

      // Act
      const res = await request(app)
        .post('/users')
        .send({ email: 'carol@example.com', name: 'Carol 2' });

      // Assert
      expect(res.status).toBe(409);
      expect(res.body.error).toBe('email already in use');
    });
  });
});
```

## Best Practices
- Write tests before code (TDD) to drive better API design
- One logical assertion concept per test — multiple `expect()` calls are fine if they verify the same behavior
- Tests should be deterministic: no random data, no time-dependent behavior (mock `Date.now()`)
- Keep tests fast — slow tests don't get run; unit tests should complete in milliseconds
- Use test factories or builders for complex object setup to avoid repetition
- Test the contract (what), not the implementation (how) — brittle tests couple to internals

## Common Mistakes
- Testing implementation details (private methods, internal state) instead of observable behavior
- Not testing error paths and edge cases — happy-path-only tests miss most bugs
- Over-mocking: mocking so much that tests pass even when real integrations are broken
- Using production database in tests without cleanup — tests pollute each other
- Testing framework code (e.g., testing that Express routing works) instead of your business logic
- Ignoring flaky tests — a flaky test is worse than no test (false confidence)

## Tips & Tricks
- Use `test.each` (Jest) or `@pytest.mark.parametrize` for table-driven tests with multiple input/output pairs
- Snapshot tests for complex output structures, but review snapshots on every change
- `--coverage --collectCoverageFrom` to see which lines are untested
- Use `faker` or `factory-boy` to generate realistic test data instead of hand-crafting fixtures
- Jest's `jest.useFakeTimers()` / Python's `freezegun` to control time-dependent tests

## Related Skills
- [debugger](../debugger/SKILL.md)
- [code-reviewer](../code-reviewer/SKILL.md)
- [api-designer](../api-designer/SKILL.md)
- [refactorer](../refactorer/SKILL.md)
