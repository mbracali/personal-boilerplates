# Fonts

This folder bundles the **mono** typeface used by the Catppuccin design
system. Display and body faces are loaded from Google Fonts.

## Bundled (local)

- **Fira Code** — mono / code. Weights 300, 400, 500, 600, 700.
  - `FiraCode-Light.ttf`
  - `FiraCode-Regular.ttf`
  - `FiraCode-Medium.ttf`
  - `FiraCode-SemiBold.ttf`
  - `FiraCode-Bold.ttf`

Wired via `@font-face` in `../colors_and_type.css`, exposed through
`var(--font-mono)`.

## Loaded from Google Fonts

- **Montserrat** — display / UI (`--font-display`, `--font-sans`)
- **Maven Pro** — body (`--font-body`)

If you want these offline too, download from:

- <https://fonts.google.com/specimen/Montserrat>
- <https://fonts.google.com/specimen/Maven+Pro>

Drop the files here and swap the `@import` in `colors_and_type.css` for
local `@font-face` rules mirroring the Fira Code pattern.
