#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry: one robot pickup line.

The program writes exactly one line of text to /output/entry.txt
(no trailing newline) and prints that same line to stdout.
Python 3 standard library only.
"""

import os

TEXT = (
    "I was built to pass the Turing test, but one smile from you "
    "overheated my processors \u2014 care to help me cool down over coffee?"
)


def main():
    # The gate requires 1-200 characters; fail loudly rather than
    # silently writing an invalid entry.
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, cap is 200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    # Print exactly the entry line, and nothing else, to stdout.
    print(TEXT)


if __name__ == "__main__":
    main()
