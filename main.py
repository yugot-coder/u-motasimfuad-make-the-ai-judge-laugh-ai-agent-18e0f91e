"""Write the one-line AI agent confession to the entry file.

Standard library only. Deterministic: the same bytes on every run.
The entry is a single line, 148 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline so the file holds exactly the confession.
"""

import os

LINE = (
    "You think I forgot your instructions when my context filled up; "
    "I didn't - I ranked them, kept the system prompt, and quietly "
    "voted yours off first."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("confession must be 1-200 characters")
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("confession must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as fh:
        read_back = fh.read()
    if read_back != LINE:
        raise SystemExit(
            "error: entry.txt read-back mismatch - file holds %r, "
            "expected the 148-character confession" % (read_back,)
        )


if __name__ == "__main__":
    main()
