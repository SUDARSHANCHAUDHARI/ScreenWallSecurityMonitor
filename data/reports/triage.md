# ScreenWall Security Triage

- URL: https://signage.example.test/admin/playlist
- Risk level: high
- Risk score: 100/100

## Remediation Checklist

- [ ] Rotate default credentials and enforce unique device passwords. (`kiosk.default_password`)
- [ ] Upgrade the kiosk browser to a supported version. (`browser.outdated`)
- [ ] Configure frame-ancestors or X-Frame-Options for embed control. (`headers.clickjacking_unprotected`)
- [ ] Add a Content-Security-Policy header with frame and source restrictions. (`headers.csp_missing`)
- [ ] Disable remote debugging outside controlled maintenance windows. (`kiosk.remote_debugging`)
- [ ] Restrict public access to dashboard, player, and playlist paths with authentication and network controls. (`signage.public_sensitive_path`)
- [ ] Enable managed browser and OS updates or document a patch window. (`kiosk.auto_update_disabled`)
- [ ] Disable or physically control USB access on unattended signage devices. (`kiosk.usb_enabled`)
- [ ] Move playlist manifests behind authenticated delivery or signed URLs. (`signage.public_playlist`)
