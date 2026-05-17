# ScreenWall Security Monitor Report

- URL: https://signage.example.test/admin/playlist
- Findings: 9
- Risk score: 100/100

## Findings

### Public signage URL exposes an admin, player, or playlist-style path.

- Severity: `high`
- Type: `signage.public_sensitive_path`
- Evidence: `{'url': 'https://signage.example.test/admin/playlist'}`

### Playlist content appears publicly accessible.

- Severity: `medium`
- Type: `signage.public_playlist`
- Evidence: `{'url': 'https://signage.example.test/admin/playlist'}`

### Remote debugging is enabled.

- Severity: `high`
- Type: `kiosk.remote_debugging`
- Evidence: `{'remote_debugging': True}`

### Kiosk configuration uses a default password.

- Severity: `critical`
- Type: `kiosk.default_password`
- Evidence: `{'default_password': True}`

### USB access is enabled and should be verified.

- Severity: `medium`
- Type: `kiosk.usb_enabled`
- Evidence: `{'usb_enabled': True}`

### Automatic browser or OS updates are disabled.

- Severity: `medium`
- Type: `kiosk.auto_update_disabled`
- Evidence: `{'auto_update_disabled': True}`

### Content-Security-Policy header is missing.

- Severity: `high`
- Type: `headers.csp_missing`
- Evidence: `{}`

### No iframe/clickjacking protection is configured.

- Severity: `high`
- Type: `headers.clickjacking_unprotected`
- Evidence: `{}`

### Kiosk browser version is below the configured minimum.

- Severity: `high`
- Type: `browser.outdated`
- Evidence: `{'chrome_major': 96, 'minimum': 120}`

