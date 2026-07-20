# Setup

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

:::{important}
Careful! The utilized image is ~5GB large.
:::

```bash
cd data/
bash download.sh
```
