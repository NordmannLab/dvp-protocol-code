# Setup

1. Clone this repository

```shell
git clone https://github.com/MannLabs/dvp-protocol-code.git
# go into the repository
cd dvp-protocol-code
```

2. Create a suitable python environment

For image analysis

```shell
conda create -n dvp python=3.13 -y

pip install -r requirements/requirements_image.txt
```

For the proteomics data analysis section

```shell
conda create -n dvp python=3.13 -y

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
