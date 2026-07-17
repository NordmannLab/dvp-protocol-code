# Setup

Clone this repository

```shell
git clone https://github.com/MannLabs/dvp-protocol-code.git
# go into the repository
cd dvp-protocol-code
```

Create a suitable python environment

```shell
conda create -n dvp python=3.13 -y
pip install -r requirements.txt
```

Download the data

:::{important}
Careful! The utilized image is ~5GB large.
:::

```bash
cd data/
bash download.sh
```
