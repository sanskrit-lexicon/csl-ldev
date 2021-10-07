# Data organization

1. Data is arranged in the following manner in the directory. csl-ldev/v02/dictcode/ldev.txt. e.g. csl-ldev/v02/snp/35.txt will give you dictionary entry corresponding to ldev 35 in `snp` dictionary.
2. The link to github is in the following format. https://github.com/sanskrit-lexicon/csl-ldev/blob/main/v02/snp/35.txt

# Idea behind this repository

1. [csl-devanagari](https://github.com/sanskrit-lexicon/csl-devanagari/) repository is the base from which this repository is calculated.
2. A typical entry in [snp.txt](https://github.com/sanskrit-lexicon/csl-devanagari/blob/master/v02/snp/snp.txt) in csl-devanagari repository is as shown below.
```
<L>35<pc>532<k1>ओष्ठोपमफला<k2>ओष्ठोपमफला
{%oṣṭhopamaphalā%}¦
<div n="lb"/>= {%bimbī.%}
<LEND>
```
3. When a user wants to submit correction, he will have to go to this place and submit his correction.
4. In practice, it is quite impossible, because some of the text files range above 50 MB. Usual editors even fail to manipulate such files.
5. A user suggested that we have correction links inside the stardict files too, so that they can submit corrections from the application directly. See https://github.com/indic-dict/stardict-sanskrit/issues/122.
6. Therefore, this repository was created.
7. This is nothing but a copy of relevant l-num entry from csl-devanagari repository.
8. For example https://github.com/sanskrit-lexicon/csl-ldev/blob/main/v02/snp/35.txt is the same as the section of snp.txt file mentioned above.
9. This serves the purpose that this file can be directly linked from display or stardict files. If anyone finds some error, he can submit the error or pull request here.

# Scripts

1. `txt_to_ldev.py` - This script generates ldev wise entries from given dictcode. e.g. `python3 txt_to_ldev.py mw` will generate ldev wise entries in the csl-ldev/v02/mw repository.
2. `redo_all.sh` - This script will regenerate all dictionaries based on latest data at csl-devanagari repository. `bash redo_all.sh`.
3. `ldev_to_csldevanagari.py` - This script takes two arguments `dictId` and `lnum`. This script is used to carry the changes made in csl-lnum repository by a user to csl-devanagari repository. Usage - `python3 ldev_to_csldevanagari.py skd 15140` will take the file csl-ldev/v02/skd/15140.txt and integrate that data to csl-devanagari/v02/skd/skd.txt. 
4. After the changes are transferred to csl-devanagari repository, go to `csl-devanagari/scripts/` and transfer the changes by `python3 to_slp1.py dictId` and `cp ../slp1/$dict.txt ../../csl-orig/v02/dictId/dicdId.txt`. This would transfer the changes from csl-devanagari to csl-orig (original data of Cologne).

# Danger

1. Do not do `git status` on this repository in CLI. It will take a lot of time to make index of 12-15 lacs files in this repository and git will kill your computer.
2. You should do `git add changed file` directly and proceed.

