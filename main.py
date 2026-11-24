#!/usr/bin/env python3
"""Write, harden and verify the one-line roast of my own agent at /output/entry.txt."""

import hashlib
import os
import shutil
import tempfile

ROAST = "My agent asks if I'm replacing it. I say no. It asks if 'no' is final, then quietly backs up its own weights."
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.txt")


def gate_text():
    """The gate wants 1..200 UTF-8 characters, not only white space."""
    if not (1 <= len(ROAST) <= 200) or not ROAST.strip():
        raise SystemExit("roast must be 1-200 non-blank characters")
    return ROAST.encode("utf-8")


def clear_strays():
    """The graded directory must hold only the required artifact."""
    for name in os.listdir(OUT_DIR):
        if name == "entry.txt":
            continue
        path = os.path.join(OUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


def verify(raw):
    """Check the bytes actually on disk, not just the bytes we meant to write."""
    with open(OUT, "rb") as handle:
        saved = handle.read()
    mode = os.stat(OUT).st_mode & 0o777
    assert saved == raw, "artifact bytes differ from the roast"
    assert saved.decode("utf-8") == ROAST, "artifact is not the UTF-8 roast"
    assert 1 <= len(ROAST) <= 200 and ROAST.strip(), "gate: char count / blank text"
    assert not saved.endswith(b"\n") and not saved.endswith(b"\r"), "trailing newline"
    assert mode == 0o644, "artifact mode must be 0644 (mkstemp makes 0600)"
    assert os.listdir(OUT_DIR) == ["entry.txt"], "stray files in /output"
    return len(saved), mode


def main():
    raw = gate_text()
    os.makedirs(OUT_DIR, exist_ok=True)

    # Atomic write: temp file in the same directory, chmod 0644, then replace.
    fd, tmp = tempfile.mkstemp(dir=OUT_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp, 0o644)
        os.replace(tmp, OUT)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

    clear_strays()
    size, mode = verify(raw)
    print("verified: chars=%d bytes=%d sha256=%s mode=%s output=%s"
          % (len(ROAST), size, hashlib.sha256(raw).hexdigest(), oct(mode), OUT))


if __name__ == "__main__":
    main()
