# dvp-protocol-code

[![Build](https://github.com/MannLabs/dvp-protocol-code/actions/workflows/build.yaml/badge.svg)](https://github.com/MannLabs/dvp-protocol-code/actions/workflows/build.yaml)

Code for the protocol on **Deep Visual Proteomics** (DVP).

## Setup

Clone this repository:

```shell
git clone https://github.com/MannLabs/dvp-protocol-code.git
# go into the repository
cd dvp-protocol-code
```

Create a suitable Python environment:

```shell
conda create -n dvp python=3.13 -y
pip install -r requirements.txt
```

## Structure

```shell
├── README.md
├── LICENSE
├── requirements.txt
├── data
│   └── download.sh
├── notebooks
│   ├── image-analysis
│   │   ├── harpy.ipynb
│   │   └── src
│   └── proteomics-analysis
└── results
```

## Tutorials

The analysis workflows are documented as executable notebooks:

- [Image analysis](tutorials/image-analysis.ipynb) — cell segmentation, feature extraction, quality control, and cell classification of DVP imaging data.
- [Proteomics analysis](tutorials/proteomics-analysis.ipynb) — pseudobulk reanalysis of the proteomics data.

```{toctree}
:hidden:
:maxdepth: 2

tutorials/index
```

## References
