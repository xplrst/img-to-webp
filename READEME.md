# Recursive WebP Image Converter

A lightweight, fault-tolerant Python CLI utility to batch-convert images (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`) to WebP format across nested directories.

## Features
* **Recursive Conversion:** Scans target directories and all nested subdirectories automatically.
* **Non-Destructive by Default:** Saves converted images into a `webp/` subfolder inside each scanned directory without touching originals (with an optional `--in-place` flag).
* **EXIF Orientation Safe:** Automatically transposes mobile/camera EXIF rotation tags so portrait photos never save sideways.
* **Flexible Input:** Pass a directory path directly via CLI arguments or run the script interactively and paste/drag-and-drop a folder path.
* **Idempotent:** Skips already-converted files and ignores existing `webp/` output folders on repeat runs.

---

## Prerequisites

* Python 3.8+
* [Pillow](https://python-pillow.org)

```bash
pip install Pillow
```

---

## Usage

### Interactive Mode (Paste or Drag-and-Drop)
Run the script without arguments and paste your directory path when prompted:
```bash
python to_webp.py
```

### Direct CLI Mode
Pass the target directory directly as a positional argument:
```bash
python to_webp.py "/path/to/images"
```

### Options

| Flag | Description | Default |
| :--- | :--- | :--- |
| `path` | Target directory path (prompts interactively if omitted) | `None` |
| `--in-place` | Save `.webp` files alongside original files instead of a `webp/` subfolder | `False` |
| `-q`, `--quality` | Output WebP compression quality (`1`–`100`) | `80` |
| `-h`, `--help` | Show help message and exit | — |

### Examples

Convert all images recursively into per-folder `webp/` subdirectories at quality `90`:
```bash
python to_webp.py "C:\Users\Alex\Pictures\Assets" -q 90
```

Convert images in-place alongside original files:
```bash
python to_webp.py ./assets --in-place
```

---

## Supported Formats
* **Input:** `.jpg`, `.jpeg`, `.png` (preserves alpha transparency), `.bmp`, `.tiff`
* **Output:** `.webp`
