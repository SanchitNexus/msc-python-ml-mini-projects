## Duplicate File Finder (Local Automation)

### Problem Statement
Locate identical copies of files to help clean local storage safely.

### Dataset
`data/sample_files/` bundles three tiny fake example text files, two with identical contents. For real use, the supplied dataset is any local directory selected by the reviewer.

### Approach
Recursively visit files, hash bytes with SHA-256 in chunks, group by `(size, hash)`, and print groups containing more than one file. Read-only design.

### Result
Verified offline run: **3 files** scanned, **1 duplicate group** found.

### Key Insight
Equal filenames do not guarantee duplicate contents, while differently named files can be byte-identical; content hashes detect the latter reliably in practice.

### How to Run
`python main.py` (demo) or `python main.py "/path/to/folder"` (own folder). No external packages.
