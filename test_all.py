"""Run all student projects end-to-end; API scripts use bundled offline data."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent

def main():
    for number in range(1, 11):
        folder = ROOT / f"project-{number:02d}"
        args = [sys.executable, str(folder / "main.py")]
        if number in (3, 6, 7, 8): args.append("--offline")
        result = subprocess.run(args, cwd=folder, capture_output=True, text=True)
        print(f"project-{number:02d}: {'PASS' if result.returncode == 0 else 'FAIL'}")
        if result.returncode:
            print(result.stdout, result.stderr)
            raise SystemExit(1)
    checks = {5: "dashboard.png", 6: "trend.png", 8: "clean_table.csv", 10: "correlation.png"}
    for number, file in checks.items():
        assert (ROOT / f"project-{number:02d}" / "outputs" / file).is_file(), file
    print("All 10 projects passed (offline reproducibility check).")

if __name__ == "__main__": main()
