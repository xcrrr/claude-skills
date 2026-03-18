---
name: security-auditor
description: "Use this skill when auditing code for security vulnerabilities, reviewing authentication and authorization logic, or checking OWASP compliance. Trigger phrases: 'audit this for security', 'is this secure', 'check for vulnerabilities', 'OWASP review'. Not for penetration testing tooling or network security configuration."
version: 1.0.0
author: community
tags: [coding, security, owasp, vulnerability, audit]
license: MIT
---

# Security Auditor

## Overview
The Security Auditor skill provides a structured approach to identifying security vulnerabilities in application code, based on the OWASP Top 10 and secure coding best practices. It covers input validation, injection attacks (SQL, command, LDAP), cross-site scripting (XSS), cross-site request forgery (CSRF), authentication and session flaws, insecure direct object references, secrets in code, and dependency vulnerabilities. Every finding includes a severity rating, a clear explanation of the risk, and a concrete remediation.

## When to Use
- Reviewing code before deployment for security flaws
- Auditing authentication, authorization, or session management logic
- Checking a login form, API endpoint, or data processing pipeline
- Reviewing code that handles user-supplied input
- Checking for hardcoded secrets or insecure dependency versions

## When NOT to Use
- Network-level security assessments (firewall rules, TLS config)
- Penetration testing or active exploitation (separate discipline)
- Infrastructure security (cloud IAM policies, container security)
- Compliance audits (SOC2, HIPAA, PCI-DSS) — these require human auditors

## Quick Reference
| # | Category | Key Check |
|---|----------|-----------|
| A01 | Broken Access Control | Is every route/endpoint authorization-checked? |
| A02 | Cryptographic Failures | Is sensitive data encrypted in transit and at rest? |
| A03 | Injection | Is ALL user input parameterized/sanitized? |
| A04 | Insecure Design | Are threat models documented and addressed? |
| A05 | Security Misconfiguration | Debug mode off in prod? Default passwords changed? |
| A06 | Vulnerable Components | Are dependencies up to date and scanned? |
| A07 | Auth/Identity Failures | Strong passwords, MFA, secure sessions? |
| A08 | Software/Data Integrity | Are dependencies verified with checksums/locks? |
| A09 | Logging/Monitoring Failures | Are security events logged without leaking sensitive data? |
| A10 | SSRF | Are outbound requests to user-supplied URLs restricted? |

## Instructions

1. **Map the attack surface**
   - List all inputs: query params, request bodies, headers, cookies, file uploads, env vars.
   - List all outputs: HTML responses, JSON API responses, file writes, database writes.
   - List all trust boundaries: anonymous vs. authenticated, user vs. admin, client vs. server.

2. **Check for injection vulnerabilities (A03)**
   - SQL Injection: Are all database queries using parameterized queries or prepared statements? No string concatenation with user input.
   - Command Injection: Is `os.system()`, `exec()`, `subprocess` ever called with user-controlled data?
   - LDAP/XPath/NoSQL Injection: Same principle — parameterize all queries.
   - Template Injection: Are user strings ever passed to template engines without escaping?

3. **Check for XSS (output encoding)**
   - Is user-supplied text escaped before rendering in HTML? (`&lt;`, `&gt;`, `&amp;`)
   - Is `innerHTML` or `dangerouslySetInnerHTML` used with user data?
   - Are Content Security Policy (CSP) headers set?
   - Are `HttpOnly` and `Secure` flags on session cookies?

4. **Check for authentication and session flaws (A07)**
   - Are passwords hashed with bcrypt, scrypt, or Argon2 (not MD5/SHA1)?
   - Are session tokens sufficiently random and at least 128 bits?
   - Is there a session invalidation mechanism on logout?
   - Are failed login attempts rate-limited or locked after N failures?
   - Is multi-factor authentication available for sensitive operations?

5. **Check for broken access control (A01)**
   - Is every endpoint that returns data verifying the requester owns/can access that data?
   - Are admin-only endpoints checking for admin role, not just login?
   - Are direct object references (IDs in URLs) validated against the authenticated user?
   - Is `CORS` configured to only allow trusted origins?

6. **Check for secrets in code**
   - Search for: `api_key`, `secret`, `password`, `token`, `credential` in source files.
   - Check `.env` files committed to version control (`git log --all -S "password"`).
   - Verify `.gitignore` excludes all secret files.
   - Use environment variables or a secrets manager (Vault, AWS Secrets Manager, GitHub Secrets).

7. **Check CSRF protection**
   - Are state-changing requests (POST, PUT, DELETE) protected with CSRF tokens or SameSite cookies?
   - Is the CSRF token validated server-side on every mutation?

8. **Check for SSRF (A10)**
   - Is user-supplied URL ever fetched server-side without validation?
   - Are private IP ranges (10.x, 172.16.x, 192.168.x, 169.254.x) blocked?

9. **Check for insecure dependencies (A06)**
   - Run `npm audit`, `pip-audit`, `bundler-audit`, or `trivy` on dependencies.
   - Check for packages with known CVEs. Update or replace vulnerable versions.

10. **Assign severity and remediate**
    - **Critical**: Exploitable without authentication; direct data breach or RCE risk.
    - **High**: Exploitable with authentication; significant data exposure.
    - **Medium**: Requires specific conditions; partial data exposure.
    - **Low**: Defense-in-depth improvement; no direct exploit path.

## Examples

### Example 1: Audit a login function

**Input:**
```python
import sqlite3
import hashlib

def login(username, password):
    conn = sqlite3.connect('app.db')
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = conn.execute(query)
    user = cursor.fetchone()
    if user:
        session['user_id'] = user[0]
        session['role'] = user[4]
        return True
    return False
```

**Output:**

**[Critical] SQL Injection** — Line 5
The `username` and `password` are interpolated directly into the SQL string. An attacker can log in as any user with `username = admin'--` (comments out the password check).
```
Attack: username = "admin'--"
Query becomes: SELECT * FROM users WHERE username = 'admin'--' AND password = '...'
```
Fix:
```python
cursor = conn.execute(
    "SELECT * FROM users WHERE username = ? AND password_hash = ?",
    (username, hash_password(password))
)
```

**[Critical] Plaintext password comparison** — Line 5
Passwords appear to be stored and compared in plaintext. A database breach exposes all passwords immediately.
Fix: Hash passwords with bcrypt at registration; compare with `bcrypt.checkpw()` at login:
```python
import bcrypt

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)
```

**[High] No rate limiting / brute force protection**
An attacker can make unlimited login attempts. No lockout, delay, or CAPTCHA is implemented.
Fix: Implement exponential backoff or lock after 5 failed attempts per username per 15 minutes using Redis or a `failed_logins` table.

**[Medium] Role stored in session without verification**
`session['role']` is set from the database but should be re-verified on each sensitive request, not trusted from the session store alone.

**[Low] Database connection not closed**
`conn` is not closed, potentially exhausting connections under load. Use a context manager:
```python
with sqlite3.connect('app.db') as conn:
    ...
```

---

### Example 2: Review an API endpoint for security

**Input:**
```javascript
// Express.js endpoint
app.get('/api/documents/:id', async (req, res) => {
  const docId = req.params.id;
  const doc = await db.query(`SELECT * FROM documents WHERE id = ${docId}`);

  if (!doc) return res.status(404).json({ error: 'Not found' });

  // Return document including internal metadata
  res.json(doc);
});
```

**Output:**

**[Critical] SQL Injection** — Line 3
`docId` is interpolated directly into the SQL query. An attacker can pass `1 OR 1=1` to return all documents.
Fix:
```javascript
const doc = await db.query('SELECT * FROM documents WHERE id = $1', [docId]);
```

**[Critical] Missing authorization check**
There is no check that the requesting user owns or has permission to view this document. Any authenticated (or unauthenticated) user can access any document by guessing its ID (Insecure Direct Object Reference — IDOR).
Fix:
```javascript
app.get('/api/documents/:id', authenticate, async (req, res) => {
  const doc = await db.query(
    'SELECT * FROM documents WHERE id = $1 AND owner_id = $2',
    [req.params.id, req.user.id]
  );
  if (!doc.rows[0]) return res.status(404).json({ error: 'Not found' });
  res.json(doc.rows[0]);
});
```

**[High] Authentication middleware missing**
The `authenticate` middleware is not applied. Any anonymous request succeeds.

**[Medium] Sensitive fields in response**
`SELECT *` returns all columns including internal fields (e.g., `storage_path`, `internal_tags`). Return only fields the client should see:
```javascript
const { id, title, content, created_at } = doc.rows[0];
res.json({ id, title, content, created_at });
```

**[Low] Missing input validation on `id` parameter**
`req.params.id` should be validated as a positive integer or UUID before use, providing defense-in-depth even with a parameterized query.

## Best Practices
- Validate ALL inputs — length, type, format, range — before using them
- Use parameterized queries everywhere, no exceptions
- Apply the principle of least privilege: services, database users, and API keys should have minimum required permissions
- Store secrets in environment variables or a secrets manager — never in source code or version control
- Set security headers: `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`
- Log security events (failed logins, authorization failures, input validation failures) without including sensitive data

## Common Mistakes
- Trusting client-supplied data (headers, cookies, params) for authorization decisions
- Using MD5 or SHA1 for password hashing (they are not password hashing algorithms)
- Exposing stack traces or internal error details in API responses
- Disabling CORS entirely instead of configuring it correctly
- Storing session tokens in `localStorage` (vulnerable to XSS) instead of `HttpOnly` cookies
- Not rotating secrets after a potential exposure

## Tips & Tricks
- Use `git log --all -S "password"` to find secrets ever committed to the repo
- `semgrep` (free) can automatically find common vulnerability patterns in source code
- OWASP ZAP is a free tool for automated scanning of web application endpoints
- `npm audit fix` / `pip-audit --fix` can automatically upgrade vulnerable dependencies
- OWASP's Cheat Sheet Series (cheatsheetseries.owasp.org) has ready-to-use remediation patterns

## Related Skills
- [code-reviewer](../code-reviewer/SKILL.md)
- [api-designer](../api-designer/SKILL.md)
- [sql-expert](../sql-expert/SKILL.md)
- [test-writer](../test-writer/SKILL.md)
