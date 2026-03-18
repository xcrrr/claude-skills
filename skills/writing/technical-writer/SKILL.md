---
name: technical-writer
description: "Use this skill when creating technical documentation, API references, installation guides, README files, or any content that explains how a system, tool, or process works to a technical audience. Trigger phrases: 'document this API', 'write a README', 'create a setup guide'. Do NOT use for marketing copy about a product or non-technical how-to content aimed at general audiences."
version: 1.0.0
author: community
tags: [writing, technical, documentation, api]
license: MIT
---

# Technical Writer

## Overview
This skill produces clear, accurate, and immediately usable technical documentation—from API endpoint references and SDK guides to installation walkthroughs and troubleshooting sections. It applies documentation best practices: active voice, precise language, consistent structure, and code examples that actually run. The output is calibrated to the technical level of the audience, so a developer guide reads differently from an ops runbook or a user-facing setup wizard.

## When to Use
- Writing or improving README files for code repositories
- Documenting REST APIs, GraphQL schemas, or SDK methods
- Creating installation, configuration, or deployment guides
- Writing troubleshooting guides and FAQ sections
- Producing internal runbooks, SOPs, or architecture decision records
- Documenting CLI tools and their flags/options
- Writing release notes and changelogs

## When NOT to Use
- Marketing copy about a product's features (use `copywriter` skill)
- General audience how-to content without code or system-specific steps
- Blog posts that happen to be about technical topics (use `blog-post` skill)
- Legal or compliance documentation requiring specific certified language

## Quick Reference
| Task | Approach |
|------|----------|
| Structure | Overview → Prerequisites → Steps → Code Examples → Troubleshooting |
| Voice | Active: "Run the command" not "The command should be run" |
| Code blocks | Always specify language, always include a working example |
| Prerequisites | List exact versions, dependencies, and access requirements |
| API docs | Method, endpoint, parameters (name/type/required), request example, response example, errors |
| Audience calibration | Beginner: explain why; Intermediate: explain what; Expert: show code first |
| Troubleshooting | Error message → likely cause → fix |

## Instructions

1. **Define the document type and audience.** Before writing, identify: What type of doc is this (guide, reference, tutorial, explanation)? Who is the reader (junior dev, DevOps engineer, end user)? What do they need to DO after reading it—not just know, but do?

2. **Choose the right document structure.**
   - **Tutorial:** Learning-oriented. Walk through a concrete example. Success = reader can reproduce it.
   - **How-to Guide:** Task-oriented. Steps to accomplish a specific goal. No detours.
   - **Reference:** Information-oriented. API docs, CLI flags, config options. Completeness over narrative.
   - **Explanation:** Understanding-oriented. Architecture docs, concept overviews. Answers "why."

3. **Write the document skeleton first:**
   ```
   # Document Title
   ## Overview (what this does and why it matters)
   ## Prerequisites (exact versions, tools, access)
   ## [Main Sections / Steps]
   ## Troubleshooting
   ## Related Resources
   ```

4. **Write in active voice.** Always.
   - ❌ "The configuration file can be edited to change the timeout value."
   - ✅ "Edit the configuration file to change the timeout value."
   - ❌ "It is recommended that users restart the service after changes."
   - ✅ "Restart the service after making changes."

5. **Format code examples correctly.**
   - Always use fenced code blocks with the language specified
   - Show a real, runnable command or snippet—not pseudocode unless explicitly diagramming
   - For terminal commands, use `bash` or `shell` as the language identifier
   - For multi-step processes, number the commands and show expected output where helpful

6. **Document API endpoints using this structure:**
   ```
   ## POST /endpoint-path

   Brief description of what this endpoint does.

   ### Request

   **Headers:**
   | Header | Value |
   |--------|-------|
   | Content-Type | application/json |
   | Authorization | Bearer {token} |

   **Parameters:**
   | Name | Type | Required | Description |
   |------|------|----------|-------------|
   | param | string | Yes | What it does |

   **Example Request:**
   ```json
   { ... }
   ```

   ### Response

   **Success (200):**
   ```json
   { ... }
   ```

   **Errors:**
   | Code | Meaning |
   |------|---------|
   | 400 | Bad request – missing required field |
   | 401 | Unauthorized – invalid or expired token |
   ```

7. **Write prerequisites precisely.** Don't say "you'll need Python." Say "Python 3.10 or higher (`python --version` to check)."

8. **Add a Troubleshooting section** for any procedural doc. Structure: exact error message or symptom → likely cause → fix. Users search for error text—match it exactly.

9. **Calibrate jargon to audience.** Beginner: define terms on first use. Intermediate: define only uncommon terms. Expert: skip definitions, show code first.

## Examples

### Example 1: API Endpoint Documentation

**Input:** "Document the POST /users/invite endpoint. It accepts an email (required, string), role (optional, string, defaults to 'member'), and team_id (required, string). Returns the created invitation object. Auth is required via Bearer token. Errors: 400 missing fields, 401 unauthorized, 409 user already invited."

**Output:**

---

#### POST /users/invite

Sends an invitation email and creates a pending invitation record for the specified user.

##### Authentication

Requires a valid Bearer token in the `Authorization` header.

##### Request

**Headers:**

| Header | Value |
|--------|-------|
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer {your_api_token}` |

**Body Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `email` | string | Yes | — | Email address of the user to invite |
| `role` | string | No | `"member"` | Role assigned on acceptance: `"member"` or `"admin"` |
| `team_id` | string | Yes | — | ID of the team the user is being invited to join |

**Example Request:**

```bash
curl -X POST https://api.example.com/users/invite \
  -H "Authorization: Bearer eyJhbGc..." \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jane@example.com",
    "role": "admin",
    "team_id": "team_01HXYZ"
  }'
```

##### Response

```json
{
  "id": "inv_01HABC",
  "email": "jane@example.com",
  "role": "admin",
  "team_id": "team_01HXYZ",
  "status": "pending",
  "expires_at": "2024-11-15T00:00:00Z",
  "created_at": "2024-11-01T12:34:56Z"
}
```

**Error Responses:**

| Status Code | Error | Cause |
|-------------|-------|-------|
| `400 Bad Request` | `missing_required_field` | `email` or `team_id` not provided |
| `401 Unauthorized` | `invalid_token` | Bearer token is missing, expired, or invalid |
| `409 Conflict` | `invitation_exists` | A pending invitation for this email already exists for the specified team |

**Error Response Body:**

```json
{
  "error": "invitation_exists",
  "message": "An active invitation for jane@example.com already exists.",
  "code": 409
}
```

---

### Example 2: Installation Guide

**Input:** "Write an installation guide for a Node.js CLI tool called 'deployctl' that can be installed via npm. It requires Node 18+. Users need to authenticate after installing with 'deployctl auth login'. Target: developers new to the tool."

**Output:**

---

# Installing deployctl

`deployctl` is the command-line interface for managing deployments from your terminal.

#### Prerequisites

- **Node.js 18 or higher** — check your version with:
  ```bash
  node --version
  ```
  If you need to update, download from [nodejs.org](https://nodejs.org) or use `nvm`:
  ```bash
  nvm install 18 && nvm use 18
  ```
- **npm 8 or higher** (included with Node 18)
- An active account at [app.example.com](https://app.example.com)

#### Installation

Install `deployctl` globally with npm:

```bash
npm install -g deployctl
```

Verify the installation:

```bash
deployctl --version
# Expected output: deployctl/2.1.0 linux-x64 node-v18.19.0
```

#### Authentication

Log in to connect the CLI to your account:

```bash
deployctl auth login
```

This opens a browser window to complete authentication. After authorizing, you'll see:

```
✓ Logged in as your@email.com
```

If you're working in a headless environment (CI/CD, remote server), use a token instead:

```bash
deployctl auth login --token YOUR_API_TOKEN
```

Generate an API token at **Settings → API Tokens** in the dashboard.

#### Verify Your Setup

Run a quick check to confirm everything is connected:

```bash
deployctl status
```

You should see your account details and available projects.

#### Troubleshooting

**`command not found: deployctl` after installation**
Your npm global bin directory isn't in your PATH. Find it with `npm bin -g`, then add it to your shell profile:
```bash
export PATH="$(npm bin -g):$PATH"
```

**`EACCES: permission denied` during install**
Avoid using `sudo`. Instead, configure npm to use a directory you own:
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

**Authentication window doesn't open**
Copy the URL printed in the terminal and open it manually in your browser.

#### Next Steps

- [Deploy your first project](./first-deployment.md)
- [Configure environment variables](./env-vars.md)
- [CLI command reference](./commands.md)

---

## Best Practices
- Write for the reader who will search for your docs in a moment of frustration—make every section findable
- Test every code example before publishing; broken examples destroy trust instantly
- Use admonition blocks (`> **Note:**`, `> **Warning:**`) to call out gotchas and important caveats
- Keep reference docs and tutorial docs separate—mixing them creates confusion
- Version your docs alongside your code; stale docs are worse than no docs
- Use consistent terminology throughout—pick one word for a concept and stick to it

## Common Mistakes
- **Missing prerequisites:** Assuming the reader has the same environment as you
- **Pseudocode instead of runnable code:** If they can't copy-paste and run it, it's not documentation
- **Passive voice:** Makes docs feel bureaucratic and harder to follow
- **No troubleshooting section:** Every procedural doc should have one—things will go wrong
- **Documenting implementation instead of interface:** Users need to know what it does, not how it works internally
- **Long paragraphs:** Technical docs should be scannable; use tables, bullets, and headers liberally

## Tips & Tricks
- Write the code example first, then write the prose around it
- Use a "Try it yourself" section early in tutorials to build confidence
- For CLI tools, document the most common use case first, then flags and advanced options
- If a step is optional, label it clearly: "Optional: Configure TLS"
- Include the expected output for commands so users know what success looks like
- Use `>` blockquotes for notes and `>⚠️` for warnings to visually distinguish them

## Related Skills
- [blog-post](../../writing/blog-post/SKILL.md)
- [proofreader](../../writing/proofreader/SKILL.md)
- [academic-essay](../../writing/academic-essay/SKILL.md)
