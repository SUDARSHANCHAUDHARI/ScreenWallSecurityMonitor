# ScreenWall Security Monitor Report

- URL: https://signage.example.test/admin/playlist
- Findings: 9
- Risk score: 100/100
- Risk level: high

## Priority Queue

1. `kiosk.default_password` - critical - Kiosk configuration uses a default password.
2. `browser.outdated` - high - Kiosk browser version is below the configured minimum.
3. `headers.clickjacking_unprotected` - high - No iframe/clickjacking protection is configured.
4. `headers.csp_missing` - high - Content-Security-Policy header is missing.
5. `kiosk.remote_debugging` - high - Remote debugging is enabled.
6. `signage.public_sensitive_path` - high - Public signage URL exposes an admin, player, or playlist-style path.
7. `kiosk.auto_update_disabled` - medium - Automatic browser or OS updates are disabled.
8. `kiosk.usb_enabled` - medium - USB access is enabled and should be verified.
9. `signage.public_playlist` - medium - Playlist content appears publicly accessible.

## Findings

### Kiosk configuration uses a default password.

- Severity: `critical`
- Type: `kiosk.default_password`
- Evidence: `{"default_password": true}`
- Recommended action: Rotate default credentials and enforce unique device passwords.

### Kiosk browser version is below the configured minimum.

- Severity: `high`
- Type: `browser.outdated`
- Evidence: `{"chrome_major": 96, "minimum": 120}`
- Recommended action: Upgrade the kiosk browser to a supported version.

### No iframe/clickjacking protection is configured.

- Severity: `high`
- Type: `headers.clickjacking_unprotected`
- Evidence: `{}`
- Recommended action: Configure frame-ancestors or X-Frame-Options for embed control.

### Content-Security-Policy header is missing.

- Severity: `high`
- Type: `headers.csp_missing`
- Evidence: `{}`
- Recommended action: Add a Content-Security-Policy header with frame and source restrictions.

### Remote debugging is enabled.

- Severity: `high`
- Type: `kiosk.remote_debugging`
- Evidence: `{"remote_debugging": true}`
- Recommended action: Disable remote debugging outside controlled maintenance windows.

### Public signage URL exposes an admin, player, or playlist-style path.

- Severity: `high`
- Type: `signage.public_sensitive_path`
- Evidence: `{"url": "https://signage.example.test/admin/playlist"}`
- Recommended action: Restrict public access to dashboard, player, and playlist paths with authentication and network controls.

### Automatic browser or OS updates are disabled.

- Severity: `medium`
- Type: `kiosk.auto_update_disabled`
- Evidence: `{"auto_update_disabled": true}`
- Recommended action: Enable managed browser and OS updates or document a patch window.

### USB access is enabled and should be verified.

- Severity: `medium`
- Type: `kiosk.usb_enabled`
- Evidence: `{"usb_enabled": true}`
- Recommended action: Disable or physically control USB access on unattended signage devices.

### Playlist content appears publicly accessible.

- Severity: `medium`
- Type: `signage.public_playlist`
- Evidence: `{"url": "https://signage.example.test/admin/playlist"}`
- Recommended action: Move playlist manifests behind authenticated delivery or signed URLs.

