# Catppuccin Design System

> 😸 *Soothing pastel theme for the high-spirited!*

Catppuccin is a **community-driven pastel color scheme** that aims to sit in
the sweet spot between low- and high-contrast themes. It's not a product —
it's a **palette, a philosophy, and a huge ecosystem of ports**
(editors, terminals, apps, websites). This design system packages the
palette, the voice, and a small set of reference UI components so a designer
or agent can produce interfaces that feel unmistakably Catppuccin.

## Sources

This system was built from:

- **Uploaded reference** — `uploads/catppuccin-palette.md` (full 26-color
  palette × 4 flavors + suggested semantic mapping).
- **Official site** — <https://catppuccin.com/> (voice, tagline, footer).
- **Official style guide** — `catppuccin/catppuccin/docs/style-guide.md` on
  GitHub (palette principles).
- **Logo exports** — `catppuccin/catppuccin/assets/logos/exports/` on GitHub
  (circle / square / squircle PNGs for Latte and Macchiato; used as stand-ins
  for Mocha and Frappé until those exports are available upstream — **flag,
  see caveats**).
- **Reference ports** for interaction patterns: Catppuccin-for-VSCode,
  userstyles.catppuccin.com, webtui theme-catppuccin.

## The four flavors

One palette, four moods. Pick **one flavor per surface** and stick to it.

| Flavor     | Mood                           | Background | Accent default |
|------------|--------------------------------|------------|----------------|
| **Latte**     | Light mode / day           | `#eff1f5`  | Mauve `#8839ef` |
| **Frappé**    | Dark, muted                | `#303446`  | Mauve `#ca9ee6` |
| **Macchiato** | Dark, medium contrast      | `#24273a`  | Mauve `#c6a0f6` |
| **Mocha**     | Darkest (default)          | `#1e1e2e`  | Mauve `#cba6f7` |

Every flavor carries the **same 26 named roles** — 14 accents + 12 neutrals —
so switching flavors is a token swap, never a rewrite.

## Design principles (from the official style guide)

1. **Colorful is better than colorless.** Use color to create distinction and
   structure, not just decoration.
2. **There should be balance.** Not too dull, not too bright. Usable in all
   lighting conditions.
3. **Harmony over dissonance.** Vivacious colors must complement, never clash.

---

## Content fundamentals

**Voice:** warm, inviting, playful-but-competent. Catppuccin writes like a
friend who happens to be a color nerd — they'll use a cat emoji in a heading,
but the palette docs underneath are rigorous.

- **Person.** First-person plural — "*We are a community-driven color scheme*"
  — because Catppuccin *is* a community, not a product team. You/your when
  addressing a reader.
- **Tone.** Cozy, slightly whimsical. Keywords from their own copy:
  *soothing*, *high-spirited*, *pastel*, *eye-candy*, *vibrant*,
  *warm flavors*. The site calls the four themes "flavors" and uses a
  coffee-drink metaphor (Latte / Frappé / Macchiato / Mocha) throughout.
- **Casing.** Sentence case everywhere — UI labels, headings, buttons.
  Product and palette names capitalize: Catppuccin, Mocha, Frappé,
  Rosewater, Sapphire. Never SHOUT.
- **Emoji.** Used sparingly and on-brand. The repo headline is
  `😸 Soothing pastel theme for the high-spirited!` — one cat emoji, once.
  Heart-bandage `❤️‍🩹` is used by the userstyles index to mark
  unmaintained ports. **Rule of thumb:** zero-or-one emoji per heading,
  never in body copy.
- **Unicode & typography.** The IPA pronunciation `/ˌkætpʊˈtʃiːn/` appears
  in the footer — Catppuccin is happy to be precise and a little bookish.
- **Metaphors.** Coffee (flavors), cats (the mascot "Pepperjack", the 😸
  everywhere), sweetness ("eye-candy colors").
- **Example copy, verbatim:**
  - Headline: *Soothing pastel theme for the high-spirited!*
  - Subhead: *A community-driven color scheme meant for coding, designing,
    and much more!*
  - Microcopy for unmaintained: *Userstyles labeled with the ❤️‍🩹 emoji
    lack maintainers, and may not work as intended.*
  - CTA labels on the site: **Discover Ports · Explore Colors · View
    Community · Read Blog** (verbs + nouns, sentence case, no periods).

---

## Visual foundations

### Colors
- **One palette, four flavors.** Never invent hex values — if it isn't in the
  26 named roles, it doesn't belong.
- **Backgrounds layer low-to-high** as `crust → mantle → base → surface0 →
  surface1 → surface2`. Think "sedimentary rock" — the page sits on the
  deepest layer; chrome like sidebars/headers uses `mantle`; cards sit on
  `surface0`; hovered/raised elements step up to `surface1/2`.
- **Accents are equal in weight.** Pick one primary accent per view (we
  default to **Mauve**) and use the others sparingly for semantic meaning.
  Blue = primary/link, Green = success, Red = danger, Yellow = warning,
  Sky = info, Peach = CTA/highlight, Mauve = notice/brand.

### Typography
- **Display / UI:** **Montserrat** (600 for headings, 500 for UI).
- **Body alt:** **Maven Pro** (400/500) — used on the Catppuccin website
  for longer-form text.
- **Code / mono:** **Fira Code** (bundled in `fonts/`, weights 300–700)
  — Catppuccin's roots are in coding themes, so monospace is a first-class
  citizen. Fira Code's programming ligatures are on by default.
- **Scale** is a modular-fourth scale from 12 → 64 px. Body is 16 px,
  line-height 1.55. Headings tighten to 1.15–1.3.
- Tracking tightens slightly on display (`-0.015em`); body is 0.

### Spacing & density
- **4-pt grid.** Spacing tokens: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64.
- Density is **relaxed-but-not-airy** — Catppuccin wants breathing room
  (it's a *soothing* theme) without feeling empty.

### Backgrounds & imagery
- **Flat & solid.** No gradients on page backgrounds — the palette does
  the work. The only acceptable gradient is a subtle two-step accent fade
  on hero glyphs (mauve → pink, blue → sapphire) and even then, sparingly.
- **No photography in chrome.** Imagery (if any) is illustrative: pastel
  wallpapers, the Pepperjack cat mascot, dotted/rainbow confetti of the
  14 accents.
- **Dot-rainbow motif.** A row of 14 small circles in palette order is a
  signature Catppuccin device — used in headers, loaders, and dividers.

### Animation & motion
- **Easing:** `cubic-bezier(.2, 0, 0, 1)` (standard) for most transitions;
  a slightly springier `cubic-bezier(.22, 1, .36, 1)` for entrances.
- **Durations:** 120 ms (state changes), 180 ms (default), 280 ms (panel).
- **No bounces, no big scale pops.** Catppuccin is calm. Hovers cross-fade
  color in ~120 ms; cards lift 2 px with a shadow fade.
- **Flavor switching** is always animated — a 200 ms cross-fade between
  palettes feels like sunlight changing, which is the vibe.

### Hover, focus, press
- **Hover.** On dark flavors, raise the background one surface step
  (`surface0 → surface1`). On accent buttons, lighten the accent ~8%.
  Links increase text-decoration opacity.
- **Focus.** A 3 px outer ring of `primary @ 45% alpha`, offset 0. Always
  visible on keyboard; never suppressed.
- **Press.** Drop one surface step (`surface1 → surface0`) and translate
  `translateY(1px)`. No scale transforms.

### Borders & shadows
- **Borders** are preferred over shadows for delineation in dark flavors —
  usually `overlay-0` at 1 px. Avoid multiple concentric borders.
- **Shadows** are soft and low-opacity. Dark flavors layer translucent
  black; Latte uses a gentle gray. Max 4 shadow stops
  (xs / sm / md / lg).
- **Inner-shadow rings** (`inset 0 0 0 1px`) are used for inputs and code
  blocks to avoid heavy borders.

### Transparency & blur
- Used for **tints only** — a 14%-opacity accent wash behind badges and
  toast messages. Never for frosted-glass chrome; Catppuccin is flat.
- Modal overlays use `crust @ 60%` — a deep wash of the darkest neutral.

### Corner radii
- **10 px** default (cards, buttons, inputs) — soft but not squishy.
- 6 px for tight chips/badges, 14–20 px for hero/modal cards, pill
  (`999px`) for toggles and tags.

### Cards
Cards are `surface-0` with `shadow-ring` (inset 1 px of `border-soft`) and
*optionally* a `shadow-sm`. No left-color-accent borders — that's a
dashboard cliché we don't do. Padding is 24 px at the card level, 16 px at
the list-item level.

### Layout rules
- Sidebars and top chrome sit on `--bg-alt` (`mantle`), not the page
  background — this gives the "two-tone" app-shell feel you see in VSCode
  Catppuccin.
- **Content max-width** around 1200 px. Long-form text clamps to 66ch.
- Fixed elements (top bar, bottom toast area) use full width with a 1 px
  bottom/top border in `--border-soft`, never a drop shadow.

---

## Iconography

See also: `ICONOGRAPHY.md` below — short version:

- **Icon set:** **Lucide** (open-source, stroke-based) is the recommended
  CDN-loaded pack for prototypes. Catppuccin itself doesn't ship a
  proprietary icon font — its apps lean on whatever platform icons fit
  (VSCode's Codicons, the Nerd Font family). Lucide's 1.5-px stroke style
  sits well alongside Catppuccin's soft pastels.
- **Weight:** 1.5 px stroke, round line caps & joins — never solid fills
  for UI glyphs.
- **Size:** 16 / 20 / 24 px; match text line-height.
- **Color:** inherits `currentColor`. Pair with semantic tokens — e.g.
  success icons use `--success`.
- **The 😸 emoji** is reserved for marketing / community surfaces, not
  general UI.
- **Unicode** bullets (·), IPA, fractions, and arrows (→ ↗ ⇢) are part of
  the voice and welcome in copy.

---

### Caveats / things to iterate on

1. **Mocha & Frappé logo exports are missing upstream.** The Catppuccin
   repo only publishes Latte and Macchiato logo PNGs. For dark-flavor
   views we substitute the Macchiato squircle as a stand-in.
2. **Display / body fonts are loaded from Google Fonts.** Only Fira Code
   is bundled locally. Drop Montserrat / Maven Pro TTFs into `fonts/`
   if you want them offline-hosted.
3. **Ports list is a plausible sample**, not the real directory.
4. **No slides** were created — no template was provided.
5. **Iconography substitutes Lucide** for web prototypes.
