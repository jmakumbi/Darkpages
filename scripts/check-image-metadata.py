"""Fail if any image carries GPS or EXIF metadata.

Usage:
    python scripts/check-image-metadata.py            # scan content/, static/, assets/
    python scripts/check-image-metadata.py <path>...  # scan specific files or directories
    python scripts/check-image-metadata.py --staged   # scan images staged for commit

Exit code 1 if any image has GPS metadata (EXIF GPS IFD or XMP GPS tags),
any remaining EXIF block, or cannot be read. Prints offending paths and the
reason only, never metadata values. Run strip-exif.py to fix offenders.
"""

import io
import os
import subprocess
import sys
from PIL import Image

DEFAULT_DIRS = ("content", "static", "assets")
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff")
GPS_IFD = 0x8825
EXIF_IFD = 0x8769
XMP_GPS_MARKERS = (b"exif:GPSLatitude", b"exif:GPSLongitude")


def check(data: bytes, path: str) -> str | None:
    """Return the failure reason for one image, or None if clean."""
    if any(m in data for m in XMP_GPS_MARKERS):
        return "GPS"
    try:
        with Image.open(io.BytesIO(data)) as img:
            exif = img.getexif()
            if exif.get_ifd(GPS_IFD):
                return "GPS"
            if path.lower().endswith((".tif", ".tiff")):
                # TIFF tags live in the same IFD as EXIF; only a real EXIF sub-IFD counts
                present = bool(exif.get_ifd(EXIF_IFD))
            else:
                present = bool(exif) or "exif" in img.info
            return "EXIF present" if present else None
    except Exception:
        return "unreadable"


def iter_paths(targets):
    for target in targets:
        if os.path.isfile(target):
            if target.lower().endswith(EXTENSIONS):
                yield target
        elif os.path.isdir(target):
            for root, _dirs, files in os.walk(target):
                for name in sorted(files):
                    if name.lower().endswith(EXTENSIONS):
                        yield os.path.join(root, name)


def iter_working_tree(targets):
    for path in iter_paths(targets):
        with open(path, "rb") as f:
            yield path, f.read()


def iter_staged():
    names = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
        check=True, capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    for path in names:
        if path and path.lower().endswith(EXTENSIONS):
            data = subprocess.run(
                ["git", "cat-file", "blob", f":{path}"], check=True, capture_output=True,
            ).stdout
            yield path, data


def main() -> int:
    args = sys.argv[1:]
    if args == ["--staged"]:
        images = iter_staged()
    else:
        images = iter_working_tree(args or DEFAULT_DIRS)

    scanned = 0
    failures = []
    for path, data in images:
        scanned += 1
        reason = check(data, path)
        if reason:
            failures.append((path, reason))

    for path, reason in failures:
        print(f"  {reason}: {path}")
    print(f"Image metadata check: {scanned} scanned, {len(failures)} failed.")
    if failures:
        print("Run: python scripts/strip-exif.py <directory> [--recursive]")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
