"""One-Liner Laugh Lab entry: a robot vacuum's excuse for eating a sock."""

import os

LINE = "The sock was in my lane. I have right of way in the hallway; check the lease."
# Winning angle: deadpan legalism. Instead of the usual hungry-robot excuse,
# the vacuum blames the sock like a traffic accident and cites the lease —
# a bureaucratic twist no other excuse uses, and every word works.


def main() -> None:
    assert isinstance(LINE, str) and LINE.strip(), "line must not be only whitespace"
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and re-check the file itself: exactly the line, no newline.
    written = open(out_path, encoding="utf-8", newline="").read()
    assert written == LINE, "entry.txt must contain exactly the winning line"


if __name__ == "__main__":
    main()
