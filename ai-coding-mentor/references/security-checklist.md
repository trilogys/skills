# Security Checklist

Use only the sections relevant to the task.

## Authentication

- Is identity verified?
- Are tokens validated correctly?
- Are expiry/revocation cases handled?
- Are secrets kept out of logs?

## Authorization

- Is access checked at the correct resource level?
- Can one user access another user's object by changing an ID?
- Are admin-only operations protected?
- Is authorization enforced server-side?

## Input

- Validate type, size, format, and allowed values.
- Do not trust filenames, paths, URLs, SQL fragments, shell fragments, or serialized data.

## Injection

Check:

- SQL injection;
- command injection;
- template injection;
- expression injection;
- unsafe dynamic evaluation.

## File Upload

Check:

- file size;
- extension is not sufficient validation;
- MIME/content handling;
- filename/path traversal;
- decompression bombs;
- storage isolation;
- executable content.

## SSRF

If accepting URLs:

- restrict schemes;
- block internal/private destinations when appropriate;
- enforce timeout;
- control redirects;
- limit response size.

## Secrets / Sensitive Data

- no credentials in source;
- no sensitive values in logs;
- redact tokens;
- avoid returning internal stack traces;
- protect PII.

## Deserialization

Avoid unsafe deserialization of untrusted data.

## Dependencies

- avoid unnecessary dependencies;
- pin/lock appropriately;
- check known vulnerable packages when tooling exists.

## Rate / Resource Abuse

Consider:

- request size limits;
- rate limiting;
- timeout;
- concurrency limits;
- expensive queries;
- unbounded background jobs.
