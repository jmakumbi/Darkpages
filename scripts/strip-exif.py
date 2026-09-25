"""Strip EXIF/XMP metadata from all images in a directory.

Usage:
    python scripts/strip-exif.py <directory> [--recursive]
    python scripts/strip-exif.py content/pages/my-new-post/
    python scripts/strip-exif.py content/ --recursive

Strips EXIF/XMP metadata from .jpg, .jpeg, .png and .webp files (extension
matching is case-insensitive) in the given directory, or in the whole tree
below it with --recursive. Images are overwritten in place. Images that
already carry no metadata are left untouched, so the script is safe to run
multiple times. Only counts and filenames are printed, never metadata values.
"""

import os
import sys
from PIL import Image, ImageOps

EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")
XMP_KEYS = ("xmp", "XML:com.adobe.xmp")


def iter_images(directory: str, recursive: bool):
    if recursive:
        for root, _dirs, files in os.walk(directory):
            for name in sorted(files):
                if name.lower().endswith(EXTENSIONS):
                    yield os.path.join(root, name)
    else:
        for name in sorted(os.listdir(directory)):
            path = os.path.join(directory, name)
            if os.path.isfile(path) and name.lower().endswith(EXTENSIONS):
                yield path


def has_metadata(img: Image.Image) -> bool:
    return bool(img.getexif()) or "exif" in img.info or any(k in img.info for k in XMP_KEYS)


def strip_exif(directory: str, recursive: bool = False) -> tuple[int, int]:
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    stripped = skipped = 0
    for path in iter_images(directory, recursive):
        with Image.open(path) as src:
            if not has_metadata(src):
                skipped += 1
                continue
            img = ImageOps.exif_transpose(src)  # bake orientation into pixels
            clean = Image.new(img.mode, img.size)
            clean.putdata(list(img.getdata()))

        lower = path.lower()
        if lower.endswith(".png"):
            clean.save(path, optimize=True)
        elif lower.endswith(".webp"):
            clean.save(path, quality=95, exif=b"")  # no EXIF, no XMP
        else:
            clean.save(path, quality=95, subsampling=0)

        stripped += 1
        print(f"  Stripped: {os.path.relpath(path, directory)} ({img.size[0]}x{img.size[1]})")

    return stripped, skipped


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--recursive"]
    if len(args) != 1:
        print("Usage: python scripts/strip-exif.py <directory> [--recursive]")
        sys.exit(1)

    n, clean = strip_exif(args[0], recursive="--recursive" in sys.argv[1:])
    print(f"\nDone. {n} image(s) stripped of metadata, {clean} already clean.")
