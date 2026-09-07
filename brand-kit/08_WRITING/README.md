# 08_WRITING

the written half of the brand. `00_READ_ME/BRAND_VOICE_AND_MESSAGING.md` covers
what to say: positioning, values, message examples. this folder covers how it
gets typed: capitalization, punctuation, sentence rhythm, register, and the
specific habits that make a paragraph read like sami wrote it instead of a
language model.

## files

| file | what it is |
| --- | --- |
| `WRITING_STYLE.md` | the canonical spec. read this one first. |
| `AI_TELLS.md` | the failure mode. what AI-written prose does that this brand doesn't. |
| `EXAMPLES.md` | before/after rewrites, plus annotated passages from the source corpus. |
| `skills/kmab-writing/` | the same spec packaged as an agent skill. |
| `skills/kmab-writing/scripts/check_style.py` | mechanical checker. run it on a draft before publishing. |

## a note on the headings in this folder

they're lowercase. that isn't a typo and it isn't laziness; it's the house
capitalization rule, documented in `WRITING_STYLE.md`. a style guide that
doesn't follow its own style guide isn't worth much, so these files are written
in the voice they describe.

## source corpus

the rules here were pulled from actual writing, not invented:

- personal essays and application writing (`essays.zip`, ~93k characters)
- the portfolio and its ui copy — https://kmab5.github.io/
- the blog — https://kmab5.github.io/blog/
- the field guides, informal and formal versions — https://kmab5.github.io/field-guides

when a rule below and the corpus disagree, the corpus wins. update the rule.

## checking a draft

```bash
python brand-kit/08_WRITING/skills/kmab-writing/scripts/check_style.py draft.md
python brand-kit/08_WRITING/skills/kmab-writing/scripts/check_style.py draft.md --register formal
```

it checks the mechanical rules only: Title Case headings, em dash density in
prose, sentence rhythm, banned vocabulary, punctuation presence, emoji bullets,
and closing calls to action. blockquotes are skipped, and anything wrapped in
`<!-- kmab-writing: ignore-start -->` / `ignore-end` is exempt, which is how the
files in this folder get away with quoting the words they ban.

it cannot check whether the opening is concrete, whether the ending deflates, or
whether the big words are jokes. those still need eyes.
