# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**csl-ldev** provides per-entry Devanagari text files for every dictionary entry across the CDSL, enabling direct correction links from StarDict and other offline dictionary applications. Each file URL like `https://github.com/sanskrit-lexicon/csl-ldev/blob/main/v02/<dict>/<lnum>.txt` links to the exact dictionary entry, where users can submit pull requests or issues.

This is derived from `csl-devanagari`: each large per-dictionary Devanagari file is split into individual entry files (one file per L-number).

## Architecture

| Directory/File | Purpose |
|---|---|
| `v02/` | Per-dictionary subdirectories; each contains one `.txt` file per dictionary entry (named by L-number) |
| `scripts/` | Generation scripts |
| `scripts/txt_to_ldev.py` | Splits a full dictionary Devanagari file into per-entry files |
| `scripts/ldev_to_csldevanagari.py` | Reverse: reconstructs the full file from per-entry files |
| `scripts/redo_all.sh` | Regenerates all per-entry files for all dictionaries |

### File format

Each per-entry file (e.g., `v02/snp/35.txt`) contains the raw Devanagari CDSL-format entry:
```
<L>35<pc>532<k1>ओष्ठोपमफला<k2>ओष्ठोपमफला
{%oṣṭhopamaphalā%}¦
...
<LEND>
```

### Regeneration workflow

```bash
cd scripts
bash redo_all.sh    # regenerates v02/<dict>/ for all dictionaries
```

## Dependencies

- **Python 3**
- **csl-devanagari** sibling repo — source of full-dictionary Devanagari files
