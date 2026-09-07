#!/usr/bin/env python3
"""
check_style.py — mechanical style check for kmab / sami prose.

Checks only the rules a script can honestly verify: capitalization, em dash
density, sentence rhythm, banned vocabulary, punctuation presence, and a few
structural tells. Everything else in SKILL.md needs a human or a careful read.

Usage:
    python check_style.py draft.md
    python check_style.py draft.md --register informal
    python check_style.py draft.md --json
    cat draft.md | python check_style.py -

Em dash density is measured over paragraph prose only. Headings, list items,
table rows and checklists are excluded, since a dash separating a term from its
definition is a label rather than the em-dash-as-glue tell.

Blockquoted lines are skipped by default, since quoted material is usually
someone else's prose or an example of what not to do. Pass --include-quotes to
count them. To exempt a stretch of text entirely, wrap it in:

    <!-- kmab-writing: ignore-start -->
    ...
    <!-- kmab-writing: ignore-end -->

Exit code is 0 if nothing failed, 1 otherwise. Warnings do not fail the run.
"""

import argparse
import json
import re
import sys

BANNED_WORDS = [
    "delve", "leverage", "leveraging", "robust", "seamless", "seamlessly",
    "elevate", "unlock", "harness", "tapestry", "testament to", "at its core",
    "foster", "underscore", "pivotal", "holistic", "game-changer",
    "transformative", "cutting-edge", "state-of-the-art", "best-in-class",
    "ecosystem", "synergy", "streamline", "empower", "empowers", "curated",
    "bespoke", "meticulously crafted", "navigate the", "in the realm of",
]

BANNED_PHRASES = [
    "in today's fast-paced world", "in an era where", "let's dive in",
    "let's unpack", "here's the thing", "the result?",
    "but here's where it gets interesting", "it's worth noting that",
    "what if i told you", "in the world of", "a necessary evil",
    "the art of", "ready to get started", "so what are you waiting for",
]

CTA_ENDINGS = [
    "get started", "start building", "go build", "try it today", "sign up",
    "reach out", "let's build", "what are you waiting for", "join us",
    "learn more today", "the possibilities are endless",
]

INFORMAL_SHORTHAND = re.compile(r"\b(u|ur|cuz|sth|ppl|prolly|ofc|tbh|jk)\b", re.I)


def strip_code(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    return text


def prose_only(text):
    """Keep paragraph prose. Drop headings, list items, table rows, and
    checklist lines, because a dash separating a term from its definition
    (`**semicolons - yes**`, `### informal - default for guides`) is a
    typographic label, not the em-dash-as-universal-glue tell we're hunting."""
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
    out = []
    for l in text.splitlines():
        t = l.strip()
        if not t:
            out.append(l)
            continue
        if t.startswith("#") or t.startswith("|"):
            continue
        if re.match(r"^([-*+]|\d+\.)\s", t):
            continue
        # Strip a leading bold run acting as a definition label, e.g.
        # "**semicolons - yes, and correctly.** joining two clauses..." or
        # "**informal** - blog, field guides, READMEs." The dash there is
        # separating a term from its gloss, not gluing prose together.
        t = re.sub(r"^\*\*[^*]{1,140}\*\*\s*\u2014?", "", t)
        out.append(t)
    return "\n".join(out)


def strip_quotes(text):
    """Drop blockquote lines. Quoted material is someone else's prose (or your
    own, quoted as an example), so it shouldn't count toward your style."""
    return "\n".join(l for l in text.splitlines() if not l.lstrip().startswith(">"))


def strip_ignored(text):
    """Honour <!-- kmab-writing: ignore-start --> ... ignore-end --> blocks.
    Style guides and anti-pattern catalogues need to quote the bad thing."""
    return re.sub(
        r"<!--\s*kmab-writing:\s*ignore-start\s*-->.*?<!--\s*kmab-writing:\s*ignore-end\s*-->",
        " ", text, flags=re.S)


def split_sentences(text):
    text = re.sub(r"\n{2,}", " ", text)
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def headings(text):
    out = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m:
            out.append(m.group(2).strip())
    return out


def is_title_case(h):
    """Heuristic: 2+ capitalised words that aren't obviously proper nouns."""
    h = re.sub(r"[`*_\[\]()]", "", h)
    words = [w for w in h.split() if re.match(r"^[A-Za-z]", w)]
    if len(words) < 3:
        return False
    small = {"a", "an", "the", "and", "or", "but", "of", "to", "in", "on",
             "for", "with", "as", "at", "by", "from"}
    capped = sum(1 for w in words[1:]
                 if w[0].isupper() and w.lower() not in small)
    eligible = sum(1 for w in words[1:] if w.lower() not in small)
    return eligible >= 2 and capped / max(eligible, 1) >= 0.7


def check(text, register=None, include_quotes=False):
    fails, warns, stats = [], [], {}
    body = strip_ignored(text)
    body = strip_code(body)
    if not include_quotes:
        body = strip_quotes(body)
    body_nofm = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
    words = re.findall(r"[A-Za-z']+", body_nofm)
    stats["words"] = len(words)

    # headings
    hs = headings(body_nofm)
    stats["headings"] = len(hs)
    bad = [h for h in hs if is_title_case(h)]
    if bad:
        fails.append(f"Title Case heading(s): {bad}")

    # em dash density, measured over paragraph prose only
    prose = prose_only(body_nofm)
    prose_words = len(re.findall(r"[A-Za-z']+", prose))
    em = prose.count("\u2014")
    stats["em_dashes_in_prose"] = em
    stats["prose_words"] = prose_words
    if prose_words >= 50:
        per200 = em / (prose_words / 200)
        stats["em_dashes_per_200_prose_words"] = round(per200, 2)
        # One or two em dashes in a short piece is fine; the tell is the habit.
        if em >= 3 and per200 > 1.0:
            fails.append(
                f"Em dash density {per200:.2f} per 200 words of prose "
                f"(limit 1.0). {em} found in {prose_words} prose words."
            )
        elif em == 2 and per200 > 1.5:
            warns.append(
                f"Two em dashes in {prose_words} prose words. Keep the one "
                "that's a real interruption."
            )

    # sentence rhythm
    sents = split_sentences(re.sub(r"^\s*[-*#>|].*$", "", body_nofm, flags=re.M))
    lens = [len(s.split()) for s in sents if s.split()]
    if lens:
        lens_sorted = sorted(lens)
        stats["sentences"] = len(lens)
        stats["mean_sentence_words"] = round(sum(lens) / len(lens), 1)
        stats["median_sentence_words"] = lens_sorted[len(lens_sorted) // 2]
        short = sum(1 for l in lens if l < 6) / len(lens)
        stats["pct_under_6_words"] = round(100 * short, 1)
        if len(lens) >= 8:
            if short < 0.05:
                warns.append(
                    f"Only {100*short:.0f}% of sentences under six words "
                    "(corpus is ~12%). Rhythm may be too even."
                )
            if stats["mean_sentence_words"] > 22:
                warns.append(
                    f"Mean sentence {stats['mean_sentence_words']} words "
                    "(corpus is ~14). Break some up."
                )

    # punctuation presence
    marks = {
        "semicolon": body_nofm.count(";"),
        "ellipsis": len(re.findall(r"\.\.\.|\u2026|\. \. \.", body_nofm)),
        "parenthetical": len(re.findall(r"\([^)]{4,}\)", body_nofm)),
    }
    stats.update(marks)
    if sum(marks.values()) == 0 and stats["words"] > 120:
        fails.append(
            "No semicolons, ellipses, or parenthetical asides. "
            "The absence is itself a tell — add the undercut."
        )

    # vocabulary
    low = body_nofm.lower()
    hits = [w for w in BANNED_WORDS if re.search(r"\b" + re.escape(w) + r"\b", low)]
    if hits:
        fails.append(f"Banned vocabulary: {hits}")
    ph = [p for p in BANNED_PHRASES if p in low]
    if ph:
        fails.append(f"Banned phrases: {ph}")

    # antithesis / triad tells
    ant = len(re.findall(r"(?:it'?s|this is|that'?s) not [^.;\n]{2,40}?[,\u2014-] (?:it'?s|but) ", low))
    if ant >= 2:
        warns.append(f"'not X, it's Y' antithesis used {ant} times. Keep at most one.")
    triads = len(re.findall(r"\b\w+ly?\b, \b\w+\b, and \b\w+\b", low))
    if triads >= 2:
        warns.append(f"{triads} three-item adjective triads. Cut to one item or a specific.")

    # closing
    tail = " ".join(low.strip().split()[-40:])
    cta = [c for c in CTA_ENDINGS if c in tail]
    if cta:
        fails.append(f"Closes on a call to action: {cta}. End on a deflation instead.")

    # emoji bullets
    if re.search(r"^\s*[-*]?\s*[\U0001F300-\U0001FAFF]", body_nofm, flags=re.M):
        fails.append("Emoji used as a bullet marker or list lead.")

    # register consistency
    if register:
        shorthand = INFORMAL_SHORTHAND.findall(body_nofm)
        lone_i = len(re.findall(r"(?<![\w'])i(?![\w'])", body_nofm))
        stats["informal_shorthand"] = len(shorthand)
        stats["lowercase_standalone_i"] = lone_i
        if register == "formal":
            if shorthand:
                fails.append(f"Formal register contains shorthand: {sorted(set(s.lower() for s in shorthand))}")
            if lone_i:
                fails.append(f"Formal register contains lowercase standalone 'i' ({lone_i}x).")
        if register == "medium" and shorthand:
            fails.append(f"Medium register contains informal shorthand: {sorted(set(s.lower() for s in shorthand))}")

    return fails, warns, stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="markdown/text file, or - for stdin")
    ap.add_argument("--register", choices=["informal", "medium", "formal"])
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--include-quotes", action="store_true",
                    help="count blockquoted text too (off by default)")
    a = ap.parse_args()

    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    fails, warns, stats = check(text, a.register, a.include_quotes)

    if a.json:
        print(json.dumps({"fails": fails, "warnings": warns, "stats": stats}, indent=2))
        return 1 if fails else 0

    print(f"stats: {json.dumps(stats)}\n")
    if fails:
        print("FAIL")
        for f in fails:
            print(f"  x {f}")
    if warns:
        print("\nwarnings")
        for w in warns:
            print(f"  ! {w}")
    if not fails and not warns:
        print("clean on the mechanical checks.")
    print("\nthe script cannot check: concrete opening, deflating close, whether "
          "the big words are jokes, or whether it sounds like a person. read it.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
