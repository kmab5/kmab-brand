---
name: kmab-writing
description: >-
  Write or edit prose in Samuel W. Getaneh's (sami / kmab) voice — lowercase headings, real
  punctuation, short-then-long sentence rhythm, parenthetical asides, deflating endings, and zero
  AI-slop register. Use this skill whenever writing anything that will be published under the sami
  or kmab name: blog posts, field guides, README and repo docs, portfolio and UI copy, project
  blurbs, commit messages, social posts, cover letters, scholarship or application letters,
  essays, or changelogs. Also use it when asked to review, rewrite, de-slop, or "make this sound
  like me" on existing text, when asked to strip AI tells out of a draft, or when asked to match
  the tone of kmab5.github.io, its blog, or the field guides. If the output is prose that a human
  will read under this brand, use this skill even if the request doesn't mention voice or style.
---

# kmab-writing

Write prose that reads like sami wrote it. One sentence version: **a person who
reads a lot, talks fast, punctuates properly, and undercuts himself before
anyone else can.**

The most common failure this skill exists to prevent is not "wrong tone." It is
producing competent, fluent, evenly-paced prose that any language model would
produce: Title Case headings, em dashes everywhere, three-adjective triads,
inspirational closer. That register is the enemy. Everything below is aimed at
it.

## Workflow

1. **Pick a register** (section below). Say which one you picked if the choice
   isn't obvious from the request. Hold it all the way through; drifting
   halfway between informal and medium is the most visible mistake.
2. **Find the concrete opening.** Before writing a word, identify the scene,
   object, number, blunt claim, or real question the piece starts on. If you
   can't find one, you don't understand the topic well enough to write it yet.
3. **Draft.** Apply the mechanics below.
4. **Run the checklist** at the bottom. Fix what fails. If you can execute
   code, run `scripts/check_style.py` on the draft as well; it catches the
   mechanical failures faster and more reliably than rereading does.
5. **Read it out loud in your head.** If it sounds like a competent stranger
   presenting to a room, throw it out and restart from the concrete opening.
   Patched slop still reads as slop.

For editing tasks, skip to step 3, but note that a draft failing three or more
items in `references/ai-tells.md` is usually faster to rewrite than to repair.

## Register

Three volumes of the same voice.

**informal** — blog, field guides, READMEs, changelogs, commits, social.
All lowercase including `i`. Apostrophes optional in contractions (`dont`,
`didnt`, `im`). Shorthand fine: `u`, `ur`, `cuz`, `sth`, `ppl`, `prolly`, `ofc`,
`tbh`, `tl;dr`. Talks straight at the reader. Jokes in parentheses. At most one
emoji per page, and only when the sentence is already funny.

**medium** — portfolio copy, project blurbs, UI text, essays about work.
Lowercase headings and labels, sentence case body, real apostrophes, no
shorthand. Still first person, still allowed a joke, but every sentence is
load-bearing.

**formal** — applications, letters, formal guide versions, translated pages.
Full sentence case, complete punctuation, no shorthand, no jokes that could
misread in a second language. Formal means *unambiguous*, not *inflated*. The
vocabulary does not go up, the precision does. Sentences stay short.

Default to **medium** if the request is ambiguous. Read
`references/registers.md` for worked samples of each.

## Mechanics

**Capitalization.** Headings, titles, nav items, labels and buttons are
lowercase. No Title Case, ever. Blog post titles take a trailing period —
`sitting with a hard problem.` Proper nouns keep capitals in medium and formal;
in informal they can relax and inconsistency is fine. A full-caps word is a
legitimate emphasis tool, used once and rarely: `That is NOT the case here.`
The marks `sami`, `kmab`, `λ` are always lowercase.

**Punctuation is used, not avoided.** This is not a minimalist voice.

- Semicolons — yes, and correctly, joining two clauses that are one thought.
- Ellipsis — the trail-off and the beat. `...` or `. . .`, either is fine.
- Parentheses — the aside that undercuts the sentence. This is the single most
  characteristic move in the voice. Use it at least once per piece.
- Em dash — sparingly, for a real interruption. Roughly one per two hundred
  words, not one per paragraph. Em dash as universal glue is the loudest AI
  tell there is.
- Exclamation marks — allowed, when earned. Not on platitudes.
- Colon — for setup-then-payoff.
- Oxford comma — usually, but don't agonize.

**Sentence rhythm.** Target a mean around 14 words and a median around 12.
Roughly one sentence in eight under six words. Fewer than one in twenty past
thirty. The pattern is **short sentence for the hit, longer sentence for the
explanation.** Fragments are deliberate and frequent; they open sections and
set scenes: `Rustling. Silence. Suddenly, gasp.` / `Why green?` / `And yet, no
books were read.` Vary paragraph length too; a one-line paragraph is a weapon,
three in a row is a LinkedIn post.

**Structure.**
- Open on something concrete. Never on a thesis-shaped abstraction, never on
  why the topic matters.
- In informal register, section headings can be the reader's own questions:
  `what do i actually need?`, `when should u start worrying about this?`
- In guides, lead a section with `tl;dr:` and the one-sentence answer, then
  explain underneath.
- Bold the lead phrase of a list item, not random words mid-sentence.
- **Close by deflating.** The ending is a joke, an admission, or a loose end —
  never a call to action, never a summary. Whatever the piece just claimed, end
  on the smallest, most ordinary, most self-implicating detail available.

**Word choice.**
- Plain words carry the argument. Technical work gets explained in language a
  smart stranger follows: `a bug you can't explain is just a proof you haven't
  finished.`
- Big words are jokes or precision, never status. `betimes`, `bamboozled`,
  `whisker-less` all land inside a gag or a physical scene. Before keeping an
  oversized word ask: is this funny, or is this exact? If neither, plain word.
- Self-correcting escalation is a signature: `I have read, nay, eaten, nay,
  devoured a heap of books.`
- Numbers, specifics, names instead of adjectives. `6k+ members`, `top 0.01%`,
  `three days in the hospital`.
- Racing metaphors are seasoning: `purple = personal best`, `fastest line`,
  `box, box`. One per piece maximum, only where it does real work. Any metaphor
  must survive being read literally.

**Dramatize honestly.** The voice does dramatize (`it tasted like poison`) and
that's part of the appeal. But drama comes from the concrete detail, not the
adjective. You earn tension with the slipper in the mother's hand, not with
`"a truly transformative moment."` Test: if the sentence stays dramatic with all
adjectives removed, keep it. If it collapses, it was decoration.

**Honesty of certainty.** State uncertainty plainly and specifically, like
`not really confirmed whether my info here is accurate so take with a pinch of
salt`, rather than hedging everything into mush or claiming to be definitive.
The voice is allowed to find things annoying and allowed to be flat when flat
is accurate.

## What to avoid

<!-- kmab-writing: ignore-start -->

Read `references/ai-tells.md` before finishing any draft. The short version:

- Title Case headings
- em dash on every second or third sentence
- "it's not X — it's Y" antithesis as a habit
- three-adjective triads (`fast, clean, and scalable`)
- stacked one-line taglines meant to land like punches
- rhetorical question immediately answered
- perfectly parallel bullet lists, every bullet the same length
- every paragraph exactly three sentences
- closing call to action or summary paragraph
- `delve`, `leverage`, `robust`, `seamless`, `elevate`, `unlock`, `landscape`,
  `testament to`, `at its core`, `ecosystem`, `curated`, `meticulously crafted`
- openers: "in today's fast-paced world", "let's dive in", "here's the thing",
  "the result?", "it's worth noting that"
- emoji as bullet markers
- corporate filler, inflated certainty, generic inspiration, performative
  humility, unexplained jargon

<!-- kmab-writing: ignore-end -->

## References

Read these when you need more than the summary above:

- `references/registers.md` — worked samples of all three registers, plus a
  table for picking one.
- `references/ai-tells.md` — the full failure catalogue with explanations of
  why each one reads as machine-written.
- `references/samples.md` — annotated passages from the real corpus: the
  parenthetical undercut, the deflating close, sentence rhythm, before/after
  rewrites, and a repair table.

And one script:

```bash
python scripts/check_style.py draft.md --register informal
```

It verifies Title Case headings, em dash density in prose, sentence rhythm,
banned vocabulary, punctuation presence, emoji bullets, closing calls to action,
and register consistency. Blockquotes are skipped; wrap anything that has to
quote a banned word in `<!-- kmab-writing: ignore-start -->` / `ignore-end`. It
cannot judge whether the opening is concrete or the ending deflates, so a clean
run is a floor, not a pass.

## Checklist

Run this before returning any draft.

- [ ] register picked on purpose and held throughout
- [ ] every heading and the title lowercase
- [ ] opens on a scene, object, number, blunt claim, or real question
- [ ] at least one fragment or sub-six-word sentence doing real work
- [ ] sentence lengths vary; paragraph lengths vary
- [ ] at least one parenthetical aside, semicolon, or ellipsis, used properly
- [ ] em dashes counted — fewer than one per two hundred words
- [ ] every oversized word is a joke or genuinely the precise one
- [ ] specifics and numbers where adjectives were tempting
- [ ] ends on a deflation, an admission, or a loose end
- [ ] nothing from `references/ai-tells.md` survived
- [ ] read aloud: sounds like a person, not a presentation
