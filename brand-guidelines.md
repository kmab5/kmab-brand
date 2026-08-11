# Brand guidelines — Samuel W. Getaneh (λ / kmab)

Source of truth for the portfolio's visual identity. Tokens are mirrored in
`design-tokens.json` and `design-tokens.css`; the site consumes the same values
from `src/styles/global.css`.

## Logo

The mark is a lowercase lambda (λ) with a detached trailing stroke to the upper
right — a nod to both functional programming (λ) and an F1 timing screen.

| File | Use |
| --- | --- |
| `logo.svg` | Master. Uses `currentColor`, so it inherits text color. |
| `logo-purple.svg` | Primary color version (`#B24BFF`). |
| `logo-mono-dark.svg` | Ink mark for light backgrounds. |
| `logo-mono-light.svg` | Off-white mark for dark backgrounds. |
| `icon-maskable.svg` | Full-bleed square for app icons / favicons. |
| `../public/favicon.svg` | Rounded badge (dark bg + purple mark) for browser tabs. |

Rules: keep clear space around the mark equal to the height of its top hook;
don't recolor it outside the palette; don't stretch, rotate, or add effects.
On busy backgrounds use a solid mono version.

## Color

**Tiers carry meaning** (borrowed from F1 timing): purple = personal best /
signature work, green = solid, amber = side quest.

| Role | Token | Hex |
| --- | --- | --- |
| Primary — personal best | `--primary-500` | `#B24BFF` |
| Secondary — solid | `--secondary-500` | `#3DE08A` |
| Tertiary — side quest | `--tertiary-500` | `#F5C451` |
| Ink / background | `--bg` | `#0E0E11` |
| Surface | `--surface` | `#17171B` |
| Text | `--text` | `#EDEBE4` |
| Muted text | `--muted` | `#9A9AA6` |

Each accent ships a full 50–900 tint/shade scale (see `design-tokens.css` and
`palette.png`). 500 is the base; 50–400 are tints, 600–900 shades. Use 300–400
for hovers/borders and 700–900 for pressed/really-dark states.

## Typography

- **Display / UI:** Space Grotesk (400–700).
- **Mono / labels / HUD:** Space Mono (400/700) — used for eyebrows, timing
  chips, tags, and anything meant to read like telemetry.

## Voice

Precise, understated, a little playful. Show the work; let results and craft
speak. Racing metaphors are seasoning, not the meal.
