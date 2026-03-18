---
name: api-designer
description: "Use this skill when designing or reviewing REST APIs, writing OpenAPI specifications, or making decisions about URL structure, HTTP methods, and response formats. Trigger phrases: 'design an API for', 'what endpoints do I need', 'how should I structure this API'. Not for implementing the API server code or designing GraphQL schemas."
version: 1.0.0
author: community
tags: [coding, api, rest, design, openapi]
license: MIT
---

# API Designer

## Overview
The API Designer skill produces consistent, developer-friendly REST API designs following industry conventions: RESTful resource naming, correct HTTP method semantics, standardized status codes, structured error responses, pagination patterns, and versioning strategies. It includes OpenAPI 3.0 spec snippets so designs can be immediately documented and validated. A well-designed API is intuitive to consume, easy to evolve, and resilient to misuse.

## When to Use
- Designing a new API surface for a service or microservice
- Adding endpoints to an existing API and needing consistency
- Reviewing an API design for RESTful correctness
- Writing an OpenAPI/Swagger specification
- Deciding on versioning, pagination, or error response format

## When NOT to Use
- Implementing the actual server-side logic (use a framework guide instead)
- Designing a GraphQL schema (different paradigm)
- Designing a WebSocket or streaming protocol API
- Internal function/library API design (different conventions apply)

## Quick Reference
| Concern | Convention |
|---------|-----------|
| Resource URLs | Plural nouns: `/users`, `/orders/{id}/items` |
| GET | Read; idempotent; no body |
| POST | Create; non-idempotent; returns 201 + Location header |
| PUT | Full replace; idempotent; returns 200 or 204 |
| PATCH | Partial update; returns 200 with updated resource |
| DELETE | Remove; idempotent; returns 204 |
| 200 OK | Successful GET, PUT, PATCH |
| 201 Created | Successful POST; include `Location` header |
| 204 No Content | Successful DELETE or PATCH with no body returned |
| 400 Bad Request | Client sent invalid input |
| 401 Unauthorized | Missing or invalid authentication |
| 403 Forbidden | Authenticated but not authorized |
| 404 Not Found | Resource doesn't exist |
| 409 Conflict | State conflict (duplicate, version mismatch) |
| 422 Unprocessable | Valid syntax but failed validation |
| 429 Too Many Requests | Rate limit exceeded |
| 500 Internal Server Error | Unhandled server-side error |
| Pagination | Cursor-based preferred; offset for simple cases |
| Versioning | URL path `/v1/` for breaking changes; headers for content negotiation |

## Instructions

1. **Identify resources** — List the core nouns in the domain (users, orders, products, comments). Each noun becomes a resource. Resources are plural nouns in the URL.

2. **Map operations to HTTP methods**
   - List all required operations for each resource.
   - Map each operation to the correct HTTP method (see Quick Reference).
   - Never use GET for mutations; never use POST when PUT/PATCH applies.

3. **Design URL structure**
   - Use hierarchical nesting only when the child resource is meaningfully owned by the parent: `/users/{userId}/addresses`.
   - Avoid nesting more than 2 levels deep — flatten with query params instead.
   - Use kebab-case for multi-word segments: `/shipping-addresses`, not `/shippingAddresses`.
   - Resource IDs belong in the path, not the query string: `/users/42`, not `/users?id=42`.

4. **Define request/response shapes**
   - Request bodies use camelCase JSON fields.
   - Response envelopes: return the resource directly for single items; use `{ data: [], meta: {} }` for collections.
   - Include `id`, `createdAt`, `updatedAt` on all persisted resources.
   - Never return passwords, secrets, or sensitive internal fields.

5. **Design the standard error response**
   ```json
   {
     "error": {
       "code": "VALIDATION_FAILED",
       "message": "Request validation failed",
       "details": [
         { "field": "email", "message": "Must be a valid email address" }
       ],
       "requestId": "req_abc123"
     }
   }
   ```

6. **Design pagination** — For collections:
   - **Cursor-based** (preferred for large/live data):
     ```json
     { "data": [...], "meta": { "nextCursor": "eyJpZCI6MTB9", "hasMore": true } }
     ```
   - **Offset-based** (simple, small datasets):
     ```json
     { "data": [...], "meta": { "total": 250, "page": 2, "perPage": 20 } }
     ```
   - Accept `?limit=` and `?cursor=` (or `?page=&perPage=`) as query params.

7. **Plan versioning**
   - Include `/v1/` in the URL path for the initial release.
   - Increment to `/v2/` only for breaking changes.
   - Non-breaking additions (new optional fields, new endpoints) don't require a version bump.
   - Maintain old versions for a defined deprecation window (e.g., 12 months).

8. **Write the OpenAPI spec** — Document every endpoint with summary, parameters, request body schema, and response schemas including error cases.

## Examples

### Example 1: Design a User Management API

**Input:** "Design a REST API for managing users with CRUD operations, including the ability to list users with filtering."

**Output:**

**Endpoints:**
```
POST   /v1/users              Create a user
GET    /v1/users              List users (with filters)
GET    /v1/users/{userId}     Get a user by ID
PATCH  /v1/users/{userId}     Update a user (partial)
DELETE /v1/users/{userId}     Delete a user
```

**POST /v1/users — Request:**
```json
{
  "email": "jane@example.com",
  "firstName": "Jane",
  "lastName": "Doe",
  "role": "member"
}
```

**POST /v1/users — Response (201 Created):**
```json
{
  "id": "usr_01H8X9Z",
  "email": "jane@example.com",
  "firstName": "Jane",
  "lastName": "Doe",
  "role": "member",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```
Headers: `Location: /v1/users/usr_01H8X9Z`

**GET /v1/users — Query params:**
```
?role=member&search=jane&limit=20&cursor=eyJpZCI6MTB9
```

**GET /v1/users — Response (200 OK):**
```json
{
  "data": [
    {
      "id": "usr_01H8X9Z",
      "email": "jane@example.com",
      "firstName": "Jane",
      "lastName": "Doe",
      "role": "member",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  ],
  "meta": {
    "nextCursor": "eyJpZCI6MjB9",
    "hasMore": true,
    "total": 87
  }
}
```

**OpenAPI snippet:**
```yaml
openapi: 3.0.3
info:
  title: User Management API
  version: 1.0.0
paths:
  /v1/users:
    post:
      summary: Create a user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          headers:
            Location:
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'
        '422':
          $ref: '#/components/responses/ValidationError'
components:
  schemas:
    CreateUserRequest:
      type: object
      required: [email, firstName, lastName]
      properties:
        email:
          type: string
          format: email
        firstName:
          type: string
          maxLength: 100
        lastName:
          type: string
          maxLength: 100
        role:
          type: string
          enum: [member, admin]
          default: member
    User:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
        firstName:
          type: string
        lastName:
          type: string
        role:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
```

---

### Example 2: Design a File Upload API

**Input:** "Design an API for uploading files (documents, images) attached to a project."

**Output:**

**Endpoints:**
```
POST   /v1/projects/{projectId}/files          Upload a file
GET    /v1/projects/{projectId}/files          List files for a project
GET    /v1/projects/{projectId}/files/{fileId} Get file metadata
DELETE /v1/projects/{projectId}/files/{fileId} Delete a file
GET    /v1/projects/{projectId}/files/{fileId}/download  Download file content
```

**POST /v1/projects/{projectId}/files — Request:**
```
Content-Type: multipart/form-data

file: <binary>
description: "Q4 financial report"
```

For large files (> 10 MB), use a two-step upload:
```
POST /v1/projects/{projectId}/files/upload-url
```
Request:
```json
{ "filename": "report.pdf", "contentType": "application/pdf", "sizeBytes": 15000000 }
```
Response:
```json
{
  "uploadUrl": "https://storage.example.com/signed?token=...",
  "fileId": "file_09ZA",
  "expiresAt": "2024-01-15T11:00:00Z"
}
```
Client uploads directly to the signed URL, then confirms:
```
POST /v1/projects/{projectId}/files/file_09ZA/confirm
```

**GET /v1/projects/{projectId}/files/{fileId} — Response (200 OK):**
```json
{
  "id": "file_09ZA",
  "projectId": "proj_XYZ",
  "filename": "report.pdf",
  "contentType": "application/pdf",
  "sizeBytes": 15000000,
  "description": "Q4 financial report",
  "uploadedBy": "usr_01H8X9Z",
  "url": "/v1/projects/proj_XYZ/files/file_09ZA/download",
  "createdAt": "2024-01-15T10:45:00Z"
}
```

## Best Practices
- Design for the client developer's experience — make the happy path obvious
- Be consistent: if one resource uses camelCase, all resources use camelCase
- Make error messages actionable — tell the client what to do, not just what went wrong
- Document every field in the OpenAPI spec, including optional ones
- Avoid verbs in URLs — the HTTP method is the verb (`POST /payments`, not `POST /make-payment`)
- Use HTTPS everywhere and require authentication on all non-public endpoints
- Return the created/updated resource in the response body — clients shouldn't need a second GET

## Common Mistakes
- Using GET for mutations (breaks caching, idempotency, browser behavior)
- Nesting URLs more than 2 levels deep (`/users/1/posts/5/comments/3/likes` — use `/likes?commentId=3`)
- Using 200 for all responses including errors (breaks client error handling)
- Inconsistent naming (snake_case vs camelCase mixed in the same API)
- Not versioning from day one — retrofitting versioning is painful
- Returning different shapes for the same resource depending on the endpoint
- Forgetting to document rate limits and authentication requirements

## Tips & Tricks
- Use `requestId` in every error response to correlate with server logs
- Add a `X-Request-Id` header echo in all responses for distributed tracing
- Design the SDK or client code you wish you had — that often reveals API design problems
- API-first: write the OpenAPI spec before writing any implementation code
- Use Swagger UI or Redoc to generate interactive docs from the OpenAPI spec automatically

## Related Skills
- [test-writer](../test-writer/SKILL.md)
- [security-auditor](../security-auditor/SKILL.md)
- [documentation-writer](../documentation-writer/SKILL.md)
- [architecture-designer](../architecture-designer/SKILL.md)
