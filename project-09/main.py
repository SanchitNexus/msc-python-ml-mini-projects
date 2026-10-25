"""Find exact duplicate files using SHA-256; does not delete anything."""
import argparse
import hashlib
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent

def sha256(path):
    """Hash a file in chunks so large files need little memory."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", nargs="?", default=str(HERE / "data" / "sample_files"))
    args = parser.parse_args()
    folder = Path(args.folder)
    if not folder.is_dir():
        parser.error(f"Folder does not exist: {folder}")
    groups = defaultdict(list)
    for path in sorted(folder.rglob("*")):
        if path.is_file():
            try:
                groups[(path.stat().st_size, sha256(path))].append(path)
            except OSError as error:
                print("Skipping unreadable file:", path, error)
    duplicate_groups = [paths for paths in groups.values() if len(paths) > 1]
    print(f"Scanned {sum(len(v) for v in groups.values())} files")
    print(f"Duplicate groups: {len(duplicate_groups)}")
    for num, group in enumerate(duplicate_groups, 1):
        print(f"Group {num}:")
        for path in group: print("  ", path)
    print("Read-only: no files were deleted.")

if __name__ == "__main__":
    main()
