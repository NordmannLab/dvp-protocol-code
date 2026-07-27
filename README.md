# dvp-protocol-code

[![Build](https://github.com/MannLabs/dvp-protocol-code/actions/workflows/build.yaml/badge.svg)](https://github.com/MannLabs/dvp-protocol-code/actions/workflows/build.yaml)

Code for protocol on Deep Visual Proteomics

## Setup

1. Clone this repository

```shell
git clone https://github.com/MannLabs/dvp-protocol-code.git
# go into the repository
cd dvp-protocol-code
```

2. Create a suitable python environment

```shell
conda create -n dvp python=3.13 -y

# For image analysis
pip install -r requirements/requirements_image.txt

# For proteomics data analysis
pip install -r requirements/requirements_proteomics.txt
```

3. Download the data

> [!Important]
> Careful! The utilized image is ~5GB large

```bash
cd data/
bash download.sh
```

## References

> Mund, A. et al. Deep Visual Proteomics defines single-cell identity and heterogeneity. Nat Biotechnol 40, 1231–1240 (2022).

> Nordmann, T. M. et al. Spatial proteomics identifies JAKi as treatment for a lethal skin disease. Nature 1–9 (2024) doi:10.1038/s41586-024-08061-0.

### Software

> **harpy** Benjamin Rombaut, Arne Defauw, Frank Vernaillen, Julien Mortier, Evelien Van Hamme, Sofie Van Gassen, Ruth Seurinck, Yvan Saeys. Scalable analysis of whole slide spatial proteomics with Harpy. Bioinformatics (2026), btag122. https://doi.org/10.1093/bioinformatics/btag122

> **spatialdata** Spatialdata: Marconato, L. et al. SpatialData: an open and universal data framework for spatial omics. Nat Methods 1–5 (2024) doi:10.1038/s41592-024-02212-x.
