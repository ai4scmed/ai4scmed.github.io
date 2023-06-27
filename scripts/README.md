# Scripts

This folder contains some utility scripts that might be useful on a day-to-day
basis to create elements for this website.

## Converting bibtex files to publication "formatted markdown" files

The script `convert_bibtex_to_md.py` takes as input a bibtex file and outputs
in a directory a markdown file per publication formatted as required by our
website.
It solely requires the python package `bibtextparser`, which can be installed via anaconda with `conda install -c conda-forge bibtexparser`.
You can then use this script as following:

```bash
python convert_bibtex_to_md.py filename.bib results/
```

Because I (Nelle…) is very lazy, I've added in my bibtex files a `note` entry
containing any additional information useful for the creation of the markdown
file that isn't typically in a bibtex file. In zotero, it consists in adding
the information in the extra entry of each citation.

A bibtex file of the format:

```
@article{cauer_inferring_2019,
        title = {Inferring {Diploid} {3D} {Chromatin} {Structures} from {Hi}-{C} {Data}},
        copyright = {Creative Commons Attribution 3.0 Unported license (CC-BY 3.0)},
        url = {http://drops.dagstuhl.de/opus/volltexte/2019/11041/},
        doi = {10.4230/LIPICS.WABI.2019.11},
        language = {en},
        urldate = {2021-10-19},
        author = {Cauer, Alexandra Gesine and Yardimci, Gürkan and Vert, Jean-Philippe and Varoquaux, Nelle and Noble, William Stafford},
        collaborator = {Wagner, Michael},
        year = {2019},
        note = {oa\_paperurl: 'http://doi.org/10.1101/2020.08.13.249110'
githuburl: 'https://tree-timc.github.io/circhic/'},
        keywords = {000 Computer science, knowledge, general works, Computer Science},
        pages = {13 pages},
}
```

will be written to a markdown file as follows:

```
---
title: "Inferring Diploid 3D Chromatin Structures from Hi-C Data"
collection: publications
permalink: /publication/2019-cauer_yardimci_vert_varoquaux
venue: ''
citation: '<a href="http://drops.dagstuhl.de/opus/volltexte/2019/11041/">A. G. Cauer, G. Yardimci, J.-P. Vert, N. Varoquaux <i>et al.</i>. <b>Inferring Diploid 3D Chromatin Structures from Hi-C Data</b>, <i></i> 2019</a>'
oa_paperurl: 'http://doi.org/10.1101/2020.08.13.249110'
githuburl: 'https://tree-timc.github.io/circhic/'
---
```

and the two icons for Open Access papers and github URL will be displayed
properly. Note that no check is currently done on what this `note` entry
contains. It could possible cause problems.

To only export the publications associated to one authors, use the following
command:

```python
python convert_bibtex_to_md.py test-data.bib results -f Varoquaux,\ Nelle
```
