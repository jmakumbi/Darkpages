"""Install a pre-commit hook that blocks images carrying GPS or EXIF metadata.

Usage (run once per clone, from the repository root):
    python scripts/install-hooks.py

The hook runs scripts/check-image-metadata.py --staged against the images
staged for each commit, using the Python interpreter that ran this installer.
An existing pre-commit hook is backed up to pre-commit.bak.
"""

import os
import shutil
import stat
import subprocess
import sys

HOOK = """#!/bin/sh
# Installed by scripts/install-hooks.py — blocks images with GPS/EXIF metadata.
exec "{python}" scripts/check-image-metadata.py --staged
"""


def main() -> int:
    hooks_dir = subprocess.run(
        ["git", "rev-parse", "--git-path", "hooks"], check=True, capture_output=True, text=True,
    ).stdout.strip()
    os.makedirs(hooks_dir, exist_ok=True)
    hook_path = os.path.join(hooks_dir, "pre-commit")

    if os.path.exists(hook_path):
        with open(hook_path, encoding="utf-8", errors="replace") as f:
            if "install-hooks.py" not in f.read():
                shutil.copy2(hook_path, hook_path + ".bak")
                print(f"Backed up existing hook to {hook_path}.bak")

    python = sys.executable.replace("\\", "/")
    with open(hook_path, "w", newline="\n", encoding="utf-8") as f:
        f.write(HOOK.format(python=python))
    os.chmod(hook_path, os.stat(hook_path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f"Installed pre-commit hook: {hook_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
