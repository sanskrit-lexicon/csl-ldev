# csl-ldev

_Created: 15-05-2026 · Last updated: 11-07-2026_

Per-entry (`lnum`-wise) data store for the Cologne Digital Sanskrit Lexicon
(CDSL). Every dictionary entry from [csl-devanagari](https://github.com/sanskrit-lexicon/csl-devanagari)
is split out into its own small file so a single entry can be linked, viewed, and
corrected directly — without having to open the multi-megabyte per-dictionary source
files.

## Why this repository exists

The per-dictionary Devanagari sources in [csl-devanagari](https://github.com/sanskrit-lexicon/csl-devanagari)
are single text files, some larger than 50 MB — impractical for a reader who wants to
propose a correction to one entry, and too large for many editors to open. To make
per-entry correction submission feasible (including from StarDict applications — see
[indic-dict/stardict-sanskrit#122](https://github.com/indic-dict/stardict-sanskrit/issues/122)),
each entry is copied out into its own file keyed by its `L`-number (`lnum`). A reader who
finds an error in one entry can then edit or open a pull request against just that file.

## Data organization

- Files are laid out as `v02/<dictcode>/<lnum>.txt`. For example,
  [v02/snp/35.txt](https://github.com/sanskrit-lexicon/csl-ldev/blob/main/v02/snp/35.txt)
  is entry `L=35` of the `snp` dictionary.
- Each file is the verbatim `<L>…<LEND>` section copied from the corresponding
  csl-devanagari source (e.g.
  [snp.txt](https://github.com/sanskrit-lexicon/csl-devanagari/blob/master/v02/snp/snp.txt)).
  A typical entry:

  ```
  <L>35<pc>532<k1>ओष्ठोपमफला<k2>ओष्ठोपमफला
  {%oṣṭhopamaphalā%}¦
  <div n="lb"/>= {%bimbī.%}
  <LEND>
  ```

- Dictionary codes currently present under
  [v02/](https://github.com/sanskrit-lexicon/csl-ldev/tree/main/v02): `acc` `ae` `ap90`
  `armh` `ben` `bhs` `bop` `bor` `bur` `cae` `ccs` `gra` `gst` `ieg` `inm` `krm` `lan`
  `mci` `md` `mw` `mw72` `mwe` `pe` `pgn` `pui` `pw` `pwg` `sch` `shs` `skd` `snp` `stc`
  `vcp` `vei` `wil` `yat`.

## Scripts

See [scripts/](https://github.com/sanskrit-lexicon/csl-ldev/tree/main/scripts):

- [txt_to_ldev.py](https://github.com/sanskrit-lexicon/csl-ldev/blob/main/scripts/txt_to_ldev.py)
  — generate the `lnum`-wise entries for one dictionary code from its csl-devanagari
  source, e.g. `python3 txt_to_ldev.py mw` populates `v02/mw/`.
- [redo_all.sh](https://github.com/sanskrit-lexicon/csl-ldev/blob/main/scripts/redo_all.sh)
  — regenerate every dictionary from the latest csl-devanagari data: `bash redo_all.sh`.
- [ldev_to_csldevanagari.py](https://github.com/sanskrit-lexicon/csl-ldev/blob/main/scripts/ldev_to_csldevanagari.py)
  — carry a correction made here back into csl-devanagari, taking `dictId` and `lnum`,
  e.g. `python3 ldev_to_csldevanagari.py skd 15140` integrates `v02/skd/15140.txt` into
  csl-devanagari's `v02/skd/skd.txt`.

After a change is transferred back into csl-devanagari, propagate it onward to csl-orig
from `csl-devanagari/scripts/`: `python3 to_slp1.py <dictId>`, then copy
`../slp1/<dict>.txt` to `../../csl-orig/v02/<dictId>/<dictId>.txt`.

## Operational warning — do not run `git status` here

This repository holds well over a million small files. Running `git status` (or a full
`git fetch`/clone with a working-tree checkout) at the CLI will try to index every file
and can hang or exhaust the machine. Stage changed files by path directly
(`git add <path>`) rather than relying on `git status`, and prefer editing individual
files through the GitHub web/API rather than checking out the whole tree.

## Relationship to other repositories

- **Upstream source:** [csl-devanagari](https://github.com/sanskrit-lexicon/csl-devanagari)
  — the base from which every entry file here is derived.
- **Correction destination:** corrections flow back through csl-devanagari to
  [csl-orig](https://github.com/sanskrit-lexicon/csl-orig), the canonical Cologne source.

## License

Content is released under **CC-BY-SA-4.0** (see
[LICENSE](https://github.com/sanskrit-lexicon/csl-ldev/blob/main/LICENSE)), per the
RH1 license policy approved 2026-06-17.

## GitHub issue conventions

This is a tooling/data repository in the `sanskrit-lexicon` org and follows the
[Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md).
Each issue carries exactly one type label, one severity, and one milestone (see
[CLAUDE.md](https://github.com/sanskrit-lexicon/csl-ldev/blob/main/CLAUDE.md) for the
label lists); data-specific issues additionally use `domain:` labels
(`domain:schema`, `domain:migration`, `domain:integrity`, `domain:storage`). Tool work
across the org is tracked in the
[Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9) project.

### Open-issue snapshot (11-07-2026)

**7 open · 2 closed.** All open issues concern svara/accent rendering and are labelled
`domain:integrity`:

| Type | Count |
|---|---:|
| bug | 5 |
| enhancement | 1 |
| question | 1 |

| Severity | Count |
|---|---:|
| minor | 6 |
| trivial | 1 |

See the live list at
[github.com/sanskrit-lexicon/csl-ldev/issues](https://github.com/sanskrit-lexicon/csl-ldev/issues).

---

_Dr. Mārcis Gasūns_
