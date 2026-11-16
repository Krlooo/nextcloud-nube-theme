# Nube theme for Nextcloud

A clean light and dark theme for Nextcloud 35, inspired by modern cloud drives (Material 3).
It is used on `cloud.krlo.dev`.

## What it changes

- Login and guest pages: a two-column card on wide screens and a plain page on phones.
- Header: logo and product name, a large rounded search field, and round icon buttons.
- Navigation: pill-shaped entries. The "New" button sits at the top of the navigation on desktop.
  On phones it becomes a floating button.
- Files: gray folders, a 48 px list, outlined filter chips, and checkboxes that appear on hover.
- Controls: pill buttons, outlined text fields, menus with 8 px corners, and dialogs with 28 px corners.
- Dark mode follows the Nextcloud theme or the system setting.
- Font: Google Sans, self-hosted. The license is SIL OFL 1.1, see `css/fonts/OFL.txt`.

## Why it is safe on updates

- It only adds CSS. It does not change templates, JavaScript or core files.
- Most of the look comes from the Nextcloud design variables (`--color-*`, `--border-radius-*`, `--font-face`).
- Selectors only use stable component classes from `@nextcloud/vue`, never hashed classes.
- `appinfo/info.xml` allows only Nextcloud 35. On a new major version Nextcloud disables the app
  and the default look comes back. Test the theme, raise `max-version`, and enable it again.

## Install

1. Copy `appinfo`, `lib`, `css` and `img` to `apps/nube_theme` on the server.
2. Run `occ app:enable nube_theme`.
3. Optional: run `occ theming:config logo apps/nube_theme/img/logo.svg`,
   `occ theming:config primary_color "#0b57d0"` and `occ theming:config background_color "#f8fafd"`.

To undo the theme, run `occ app:disable nube_theme`.

## Develop

Edit `css/nube.css`. The file is split into numbered layers (tokens, variables, header, layout, navigation,
files, controls, popovers, settings, login). To change a color, change the `--nube-*` token at the top.
Do not change each rule.
