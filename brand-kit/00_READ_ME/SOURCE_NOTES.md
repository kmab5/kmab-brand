# Research and source notes

Audit date: 2026-07-27

## User-supplied source material

- Existing brand assets and design tokens in `brand.zip`
- Personal essays and application writing in `essays.zip`
- CV in the existing brand archive

## Public sources reviewed

- Current portfolio: https://kmab5.github.io/
- New F1 portfolio: https://kmab5.github.io/f1-portfolio/
- GitHub profile and repositories: https://github.com/kmab5
- Brandkit design guidance: https://github.com/Leonxlnx/taste-skill/tree/main/skills/brandkit
- Brand framework guidance: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/brand
- Brand review framework: https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing/skills/brand-review
- Lucide icon library: https://lucide.dev/
- Inter type family: https://github.com/rsms/inter
- PT Mono: https://fonts.google.com/specimen/PT+Mono

## Interpretation decisions

- Preserved the established purple, green, amber, near-black, and off-white system.
- Formalized the uploaded lambda as the master mark.
- Created the requested primary `λ + sami` lockup.
- Created the requested secondary rotated-λ + `mab` lockup, visually reading as `kmab`.
- Evolved the typography to Inter Display / Inter / PT Mono for reliable multilingual, UI, and code-oriented use.
- Built the verbal identity from recurring traits in the user's own writing: exactness, curiosity, persistence, perspective, warmth, and understated humor.

---

## Writing style addendum

Audit date: 2026-09-07

`08_WRITING` was added after a second pass focused only on prose style — how sentences get built, rather than what they say.

### Corpus

- Personal essays and application writing (`essays.zip`) — 35 documents, ~93,000 characters, ~16,600 words.
- Portfolio and UI copy — https://kmab5.github.io/
- Blog, all three posts — https://kmab5.github.io/blog/
- Field guides, informal and formal versions of both guides — https://kmab5.github.io/field-guides and https://github.com/kmab5/field-guides
- Author's own stated preferences, supplied directly: sparse capitalization, deliberate punctuation, informality, and an explicit objection to AI register.

### Measurements

Taken across the essay corpus, so they describe the formal end of the range; informal writing runs shorter still.

- Mean sentence length 13.8 words; median 12.
- 12.5% of sentences under six words; 4.5% over thirty.
- 39 semicolons, 33 ellipses, 66 question marks, 65 exclamation marks — punctuation is actively used.
- 6 em dashes across ~93,000 characters. This is the number that most sharply separates the voice from machine-generated prose.
- Strongly first-person: 813 instances of `I`, 468 of `my`.

### Interpretation decisions

- Documented three registers rather than one voice, because the corpus clearly contains three and the author moves between them deliberately. The formal field guide and the informal field guide are the same person writing the same content twice, which made the boundaries easy to draw.
- Treated dropped apostrophes (`dont`, `im`, `ur`) as a register marker rather than an error, since they appear consistently in guides and blog and never in essays or formal pages.
- Treated oversized vocabulary (`betimes`, `bamboozled`, `whisker-less`, `indubitably`) as in-voice, because every instance sits inside a joke or a physical scene. Flagged the same words used decoratively as out of voice. This distinction is the core of `AI_TELLS.md`.
- Named the parenthetical undercut and the deflating close as signature moves — both appear across every register and every source.
- Wrote the `08_WRITING` files in the style they document, including lowercase headings, on the grounds that a style guide that violates its own guide is not usable evidence of anything.
- Packaged the spec as `skills/kmab-writing/` so the rules survive contact with agents, which are the most likely source of drift.
