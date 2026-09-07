# skills

agent skills for the written brand. a skill is a folder with a `SKILL.md` at the
root, holding YAML frontmatter (`name`, `description`) plus markdown
instructions, and optional `references/`, `scripts/`, and `assets/` beside it.

## what's here

| skill | what it does |
| --- | --- |
| `kmab-writing/` | writes and edits prose in sami's voice. registers, punctuation, rhythm, and the anti-AI-slop rules from `../WRITING_STYLE.md` and `../AI_TELLS.md`, packaged so an agent can follow them. |

## using it

**claude.ai / claude desktop** — upload `kmab-writing.skill` (or the bare
`SKILL.md`) and hit *save skill*. rebuild the package any time the skill changes:

```bash
python -m scripts.package_skill brand-kit/08_WRITING/skills/kmab-writing
```

**claude code / any agent that reads a skills directory** — copy or symlink the
`kmab-writing/` folder into that project's skills path, e.g.
`.claude/skills/kmab-writing/`.

**anything else** — paste `SKILL.md` in as a system prompt. the `references/`
files are meant to be pulled in only when needed, so start with `SKILL.md`
alone and add the others if the output is drifting.

## keeping it honest

`../WRITING_STYLE.md` is canonical for humans. `kmab-writing/SKILL.md` is the
operational version for agents, and `references/ai-tells.md` is a straight copy
of `../AI_TELLS.md`. when the style changes, change the parent docs first, then
propagate. otherwise the two drift and the agent starts writing to a spec
nobody agreed to.

`kmab-writing/scripts/check_style.py` is the mechanical checker. it is
calibrated against the corpus: it passes the real blog posts and fails a
deliberately slop-written fixture. if you change the rules, re-check it against
both before trusting it.

`kmab-writing/evals/evals.json` holds test prompts. writing style is mostly a
subjective output so the useful check is reading the results, not scoring them;
the assertions in there only cover the mechanical rules (lowercase headings, em
dash density, banned vocabulary) that a script can actually verify.
