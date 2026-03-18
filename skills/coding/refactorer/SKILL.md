---
name: refactorer
description: "Use this skill when improving the structure, clarity, or design of existing code without changing its behavior. Trigger phrases: 'clean up this code', 'this is messy', 'refactor this', 'apply SOLID principles'. Not for adding new features or fixing bugs."
version: 1.0.0
author: community
tags: [coding, refactoring, clean-code, patterns]
license: MIT
---

# Refactorer

## Overview
The Refactorer skill provides a disciplined, step-by-step approach to improving the internal structure of code while preserving its observable behavior. It covers the most impactful refactoring patterns — including Extract Function, DRY, SOLID principles, and replacing conditionals with polymorphism — along with a decision framework for knowing when to refactor versus when to rewrite. Every refactoring step is backed by tests to ensure nothing breaks.

## When to Use
- Code is difficult to read, understand, or explain to a colleague
- The same logic appears in two or more places (DRY violation)
- A function or class has grown too large and handles too many concerns
- Adding a new feature requires touching many unrelated parts of the codebase
- Technical debt has accumulated to the point of slowing down delivery
- Code review consistently raises the same structural feedback

## When NOT to Use
- The code is throwaway/prototype quality and will be replaced soon
- You don't have tests and can't add them before refactoring (too risky)
- The behavior itself is wrong — fix the bug first, then refactor
- You are under a tight deadline — schedule refactoring as deliberate work
- You're tempted to rewrite in a new language or framework (that's not refactoring)

## Quick Reference
| Pattern | When to Apply |
|---------|--------------|
| Extract Function | Function body > 20 lines; logic block has a clear name |
| Extract Class | Class has > 1 responsibility; fields cluster into subgroups |
| Rename | Name is misleading, abbreviated, or doesn't match intent |
| DRY / Extract Common | Same logic copied in 2+ places |
| Replace Magic Number | Unexplained literals; use named constants |
| Guard Clause | Deeply nested if/else; flip condition to return early |
| Replace Conditional with Polymorphism | Long if/switch on type; open/closed principle |
| Introduce Parameter Object | Function takes 4+ related params; group into a struct/dataclass |
| Move Method | Method uses another class's data more than its own |
| Decompose Conditional | Complex boolean expression; extract to named predicate function |

## Instructions

1. **Ensure test coverage before touching code**
   - Run the existing test suite. It must be green before you start.
   - If coverage is low, write characterization tests (tests that capture current behavior) before refactoring.
   - Commit the tests separately so the refactoring diff is clean.

2. **Identify the smell** — Choose the most impactful problem to fix first:
   - **God Class**: one class that does everything
   - **Long Method**: function spans more than 20–30 lines
   - **Duplicated Code**: same or nearly same logic in multiple places
   - **Feature Envy**: a method that uses another class's data extensively
   - **Primitive Obsession**: using raw strings/ints where a domain type should exist
   - **Shotgun Surgery**: one change requires edits across many files

3. **Apply refactoring patterns incrementally**
   - Make one refactoring at a time. Run tests after each step.
   - Never mix refactoring with behavior changes in the same commit.
   - Use your IDE's automated refactoring tools (rename, extract, move) when available — they are safer than manual edits.

4. **Refactor vs. Rewrite decision**
   - **Refactor** when: the core logic is correct, tests exist, and the issues are structural.
   - **Rewrite** when: the approach is fundamentally wrong, the code can't be tested, or it would take longer to refactor than to rewrite safely.
   - The "strangler fig" pattern — incrementally replacing a module while both versions run — is often better than a big-bang rewrite.

5. **Verify behavior is unchanged**
   - Run the full test suite after each change.
   - If you introduced a regression, `git stash` or revert to the last green state immediately.
   - For critical paths, add integration or end-to-end tests before and after.

6. **Commit with intent**
   - Each commit should do one logical refactoring: "Extract `calculateDiscount` from `processOrder`"
   - Never combine a refactoring commit with a feature commit.

## Examples

### Example 1: Refactor a God Class

**Input:**
```python
class OrderProcessor:
    def __init__(self, db, email_client, stripe_client):
        self.db = db
        self.email = email_client
        self.stripe = stripe_client

    def process(self, user_id, cart):
        # Validate cart
        if not cart or len(cart) == 0:
            raise ValueError("Cart is empty")
        for item in cart:
            if item['quantity'] <= 0:
                raise ValueError(f"Invalid quantity for {item['name']}")

        # Calculate total
        subtotal = sum(i['price'] * i['quantity'] for i in cart)
        tax = subtotal * 0.08
        total = subtotal + tax

        # Charge payment
        charge = self.stripe.charge(user_id, total)
        if not charge['success']:
            raise RuntimeError("Payment failed")

        # Save order
        order = {'user_id': user_id, 'total': total, 'items': cart}
        order_id = self.db.insert('orders', order)

        # Send confirmation
        user = self.db.find('users', user_id)
        self.email.send(user['email'], f"Order {order_id} confirmed!")

        return order_id
```

**Output (refactored):**
```python
# cart_validator.py
class CartValidator:
    def validate(self, cart):
        if not cart:
            raise ValueError("Cart is empty")
        for item in cart:
            if item['quantity'] <= 0:
                raise ValueError(f"Invalid quantity for {item['name']}")

# pricing.py
class PricingCalculator:
    TAX_RATE = 0.08

    def calculate_total(self, cart):
        subtotal = sum(i['price'] * i['quantity'] for i in cart)
        return subtotal * (1 + self.TAX_RATE)

# payment_service.py
class PaymentService:
    def __init__(self, stripe_client):
        self.stripe = stripe_client

    def charge(self, user_id, amount):
        charge = self.stripe.charge(user_id, amount)
        if not charge['success']:
            raise RuntimeError("Payment failed")

# order_repository.py
class OrderRepository:
    def __init__(self, db):
        self.db = db

    def save(self, user_id, total, cart):
        return self.db.insert('orders', {'user_id': user_id, 'total': total, 'items': cart})

# order_processor.py — now thin orchestrator
class OrderProcessor:
    def __init__(self, validator, pricing, payment, repo, notifier):
        self.validator = validator
        self.pricing = pricing
        self.payment = payment
        self.repo = repo
        self.notifier = notifier

    def process(self, user_id, cart):
        self.validator.validate(cart)
        total = self.pricing.calculate_total(cart)
        self.payment.charge(user_id, total)
        order_id = self.repo.save(user_id, total, cart)
        self.notifier.confirm(user_id, order_id)
        return order_id
```

Each class now has a single responsibility and can be tested in isolation.

---

### Example 2: Extract repeated logic and apply Guard Clauses

**Input:**
```javascript
function getDisplayName(user) {
  if (user !== null && user !== undefined) {
    if (user.firstName !== null && user.firstName !== undefined) {
      if (user.lastName !== null && user.lastName !== undefined) {
        return user.firstName + ' ' + user.lastName;
      } else {
        return user.firstName;
      }
    } else {
      if (user.email !== null && user.email !== undefined) {
        return user.email;
      } else {
        return 'Anonymous';
      }
    }
  } else {
    return 'Anonymous';
  }
}
```

**Output (refactored):**
```javascript
// Step 1: Apply guard clauses to flatten nesting
// Step 2: Extract predicate helper
// Step 3: Use nullish coalescing / optional chaining (ES2020+)

function getDisplayName(user) {
  if (!user) return 'Anonymous';
  if (user.firstName && user.lastName) return `${user.firstName} ${user.lastName}`;
  if (user.firstName) return user.firstName;
  return user.email ?? 'Anonymous';
}
```

Reduced from 20 lines to 5. Logic is identical but immediately readable.

## Best Practices
- The Golden Rule: **never change behavior and structure in the same commit**
- Always start from a green test suite — refactoring without tests is rewriting under the illusion of safety
- Prefer small, frequent refactoring to large, infrequent rewrites
- Use your IDE's rename/extract tools instead of manual search-and-replace
- Read *Refactoring* by Martin Fowler for the canonical catalog of patterns
- When in doubt, extract a function — small, named functions are almost always better

## Common Mistakes
- Refactoring and adding features at the same time (mixing concerns in a commit)
- Refactoring without tests — impossible to verify behavior is preserved
- Extracting too early (premature abstraction) before patterns are clear
- Renaming things inconsistently (rename in one place, miss others)
- Treating "rewrite in a cleaner way" as refactoring when the logic changes
- Gold plating — refactoring to perfection when good enough is ready to ship

## Tips & Tricks
- Run your test suite in watch mode while refactoring so failures are instant
- `git commit --amend` or `git rebase -i` let you clean up refactoring commits before pushing
- The "rule of three": tolerate duplication once, extract on the third occurrence
- IDE shortcuts (IntelliJ `Ctrl+Alt+M`, VS Code refactor menu) are faster and safer than manual edits
- Leave code cleaner than you found it — the "boy scout rule" applied per PR

## Related Skills
- [code-reviewer](../code-reviewer/SKILL.md)
- [test-writer](../test-writer/SKILL.md)
- [architecture-designer](../architecture-designer/SKILL.md)
- [debugger](../debugger/SKILL.md)
