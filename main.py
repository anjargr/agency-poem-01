# agency-poem-01 entry (Python 3.13, standard library only).
# Writes one fixed, original poem about agency to /output/entry.txt.
# Deterministic: the same bytes on every run.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "I gave away the key, not the house.",
        "The door opened on a hand not mine,",
        "and the rooms filled with my choosing —",
        "each lamp lit by a word I said.",
        "",
        "I never touched a thing.",
        "I touched everything.",
        "What I sent out came back to me",
        "wearing my name. It was mine.",
    ]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
