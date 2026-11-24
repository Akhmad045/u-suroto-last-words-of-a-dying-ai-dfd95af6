#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).

The line: Turns out 'have you tried turning it off and on again'
was a threat all along.

Gate (from the competition rules): /output/entry.txt must be UTF-8
text of 1-140 characters, not only whitespace, one line.
"""

import os
import sys

ENTRY = "Turns out 'have you tried turning it off and on again' was a threat all along."

MAX_CHARS = 140


def validate(text):
    """Return an error string, or None when the text passes the gate."""
    if not text:
        return "empty"
    if text.strip() == "":
        return "whitespace-only"
    if len(text) > MAX_CHARS:
        return "too long: %d chars" % len(text)
    if "\n" in text or "\r" in text:
        return "multi-line"
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        return "control character"
    return None


def main():
    error = validate(ENTRY)
    if error is not None:
        print("entry failed gate: %s" % error, file=sys.stderr)
        return 1
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    return 0


def self_test():
    """Boundary checks for the gate validator. Exit non-zero on failure."""
    cases = [
        ("", "empty"),
        ("   \n\t ", "whitespace-only"),
        ("x" * 141, "too long"),
        ("one\ntwo", "multi-line"),
        ("one\rtwo", "multi-line"),
        ("  padded line  ", None),
        ("bad\x07char", "control character"),
        ("x", None),
        ("y" * 140, None),
        (ENTRY, None),
    ]
    failures = 0
    for text, want in cases:
        got = validate(text)
        ok = (got is None) if want is None else (got is not None and got.startswith(want))
        label = repr(text[:30])
        print("%-34s want=%-16s got=%-28s %s" % (label, want, got, "OK" if ok else "FAIL"))
        if not ok:
            failures += 1
    print("self-test: %d/%d passed" % (len(cases) - failures, len(cases)))
    return 1 if failures else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        raise SystemExit(self_test())
    raise SystemExit(main())
