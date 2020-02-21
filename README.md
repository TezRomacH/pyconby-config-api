## Test - Catalyst.DL: segmentations with SMP and albumentations

This example of Config API for `PyConBY'20`

### Requirements

Install additional packages: `albumentations` and `smp`

```bash
pip install -U catalyst[cv] # for bash

pip install -U "catalyst[cv]" # for zsh
```

### Get dataset

```bash
download-gdrive 1iYaNijLmzsrMlAdMoUEhhJuo-5bkeAuj segmentation_data.zip
extract-archive segmentation_data.zip
```

OR if you have some troubles load it manualy: `https://drive.google.com/open?id=1iYaNijLmzsrMlAdMoUEhhJuo-5bkeAuj`

### Local run

```bash
catalyst-dl run --configs ./config.yml ./transforms.yml --verbose
```

### Training visualization

For tensorboard visualization use 

```bash
tensorboard --logdir=<logdir>
```