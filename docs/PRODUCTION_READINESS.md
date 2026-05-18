# Production Readiness

## Current Status

This repository has a working offline product MVP with deterministic signage fixture checks, risk summary, Markdown report, triage output, tests, and generated reports. It is portfolio-ready but not production complete yet.

## Required Before Public Release

- Add explicit authorization before live URL scanning.
- Add tests for malformed fixtures and empty scan data.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization before handling customer signage data.
- Run dependency and secret scans before release.
- Add scan rate limits, timeouts, and private URL redaction.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
- Reports include risk level, severity breakdown, recommended actions, and triage checklist.
