import argparse
import sys
from pathlib import Path
from PIL import Image, ImageOps

EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}


def convert_directory(root: Path, in_place: bool = False, quality: int = 80) -> None:
    if not root.is_dir():
        sys.exit(f"Error: Directory not found -> {root}")

    for file in root.rglob("*"):
        if not file.is_file() or file.suffix.lower() not in EXTS:
            continue

        # Only skip immediate 'webp' output folders, not ancestor directories
        if not in_place and file.parent.name == "webp":
            continue

        out_dir = file.parent if in_place else file.parent / "webp"
        webp = out_dir / f"{file.stem}.webp"

        if webp.exists():
            continue

        try:
            with Image.open(file) as img:
                img = ImageOps.exif_transpose(img)
                out_dir.mkdir(exist_ok=True)
                img.save(webp, "WEBP", quality=quality)
                print(f"Converted: {webp.relative_to(root)}")
        except Exception as exc:
            print(f"[FAILED] {file.name}: {exc}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="Recursively convert images to WebP.")
    parser.add_argument("path", nargs="?", help="Target directory (prompts if omitted)")
    parser.add_argument("--in-place", action="store_true", help="Save alongside original files")
    parser.add_argument("-q", "--quality", type=int, default=80, help="WebP quality 1-100 (default: 80)")
    args = parser.parse_args()

    raw_path = args.path or input("Paste folder path: ")
    cleaned = raw_path.strip().strip('"').strip("'")

    if not cleaned:
        sys.exit("Aborted: No path provided.")

    convert_directory(Path(cleaned).resolve(), in_place=args.in_place, quality=args.quality)


if __name__ == "__main__":
    main()
