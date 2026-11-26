# Recursive WebP Image Converter

A lightweight, fault-tolerant Python CLI utility to batch-convert images (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`) to WebP format across nested directories.

## Features
* **Recursive Conversion:** Scans the target directory and all nested subdirectories automatically.
* **Non-Destructive by Default:** Saves converted images into a `webp/` subfolder inside each scanned directory without touching originals (with an optional `--in-place` flag).
* **Lossless by Default:** Preserves maximum image fidelity out of the box with `--lossless`, or switch to smaller lossy files anytime with `--no-lossless`.
* **EXIF Orientation Safe:** Automatically transposes mobile and camera EXIF rotation tags so portrait photos never save sideways.
* **Zero-Argument Current Directory Support:** Defaults to your current working directory (`.`), or accepts an explicit directory path via CLI arguments.
* **Idempotent:** Skips already-converted files and ignores existing `webp/` output folders on repeat runs.

---

## Prerequisites

* Python 3.9+
* [Pillow](https://python-pillow.org/)

```bash
pip install Pillow
```

---

## Global Terminal Alias (`towebp`)

Set up an alias or shell function so you can navigate to any directory in your terminal and run `towebp` directly.

### Windows (PowerShell)
1. Create and open your PowerShell profile:
   ```powershell
   New-Item -Path $PROFILE -ItemType File -Force
   notepad $PROFILE
   ```
2. Add the `towebp` function (update the path to match where you saved `to_webp.py`):
   ```powershell
   function towebp { python "C:\path\to\your\to_webp.py" @args }
   ```
3. Save the file and reload your profile:
   ```powershell
   . $PROFILE
   ```
   *(If PowerShell blocks local scripts, run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` once and reload again.)*

### macOS / Linux (Zsh or Bash)
1. Add the alias to `~/.zshrc` (macOS) or `~/.bashrc` (Linux):
   ```bash
   alias towebp='python3 "/path/to/your/to_webp.py"'
   ```
2. Reload your shell configuration:
   ```bash
   source ~/.zshrc
   ```

---

## Usage

### Convert Current Directory
Navigate to any folder containing images and run:
```bash
towebp
```

### Convert a Specific Directory
Pass any target directory path directly as a positional argument:
```bash
towebp "/path/to/images"
```

### Options

| Flag | Description | Default |
| :--- | :--- | :--- |
| `path` | Target directory path | `.` (current directory) |
| `--in-place` | Save `.webp` files alongside original files instead of a `webp/` subfolder | `False` |
| `-l`, `--lossless`, `--no-lossless` | Toggle lossless WebP compression (`--no-lossless` enables lossy compression) | `True` (`--lossless`) |
| `-q`, `--quality` | Output WebP quality (`1`–`100`); controls compression effort in lossless mode and visual quality with `--no-lossless` | `80` |
| `-h`, `--help` | Show help message and exit | — |

### Examples

Convert all images in the current directory recursively using default lossless settings:
```bash
towebp
```

Convert images in a specific folder using lossy compression at quality `85`:
```bash
towebp "C:\Users\Alex\Pictures\Assets" --no-lossless -q 85
```

Convert images in-place alongside original files:
```bash
towebp ./assets --in-place
```

---

## Supported Formats
* **Input:** `.jpg`, `.jpeg`, `.png` (preserves alpha transparency), `.bmp`, `.tiff`
* **Output:** `.webp`
