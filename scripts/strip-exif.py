"""Strip EXIF metadata from all images in a directory.

Usage:
    python scripts/strip-exif.py <directory>
    python scripts/strip-exif.py content/pages/my-new-post/

Strips EXIF/metadata from all .jpg, .jpeg, and .png files in the given directory.
Images are overwritten in place. Safe to run multiple times.
"""

import os
import sys
import glob
from PIL import Image, ImageOps


def strip_exif(directory: str) -> int:
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    count = 0
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        for path in glob.glob(os.path.join(directory, ext)):
            img = Image.open(path)
            img = ImageOps.exif_transpose(img)  # bake orientation into pixels
            clean = Image.new(img.mode, img.size)
            clean.putdata(list(img.getdata()))

            if path.lower().endswith(".png"):
                clean.save(path, optimize=True)
            else:
                clean.save(path, quality=95, subsampling=0)

            count += 1
            print(f"  Stripped: {os.path.basename(path)} ({img.size[0]}x{img.size[1]})")

    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/strip-exif.py <directory>")
        sys.exit(1)

    target = sys.argv[1]
    n = strip_exif(target)
    print(f"\nDone. {n} image(s) stripped of EXIF data.")
