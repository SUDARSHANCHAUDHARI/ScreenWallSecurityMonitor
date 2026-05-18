# Security Notes

ScreenWall Security Monitor is defensive and audit-focused.

## Safe Use

- Scan only signage deployments, kiosks, and URLs you own or have permission to assess.
- Do not commit private device inventories, dashboard URLs, access tokens, or customer configurations.
- Treat generated reports as sensitive because they may identify exposed signage paths.

## Current Boundary

The MVP uses local JSON fixtures and does not perform live HTTP scans. This keeps demos safe and repeatable.

## Before Production

- Add target authorization checks.
- Add rate limits and request timeouts.
- Add redaction for private device names and internal URLs.
- Add audit logging for scans and report exports.
