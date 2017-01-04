# Cityscapes Dataset Labeling Tool

Tested on Ubuntu 14.04 LTS

## Usage:

**This will create gtFine & gtCoarse folders if they do not exist. Existing files won't be affected.**

1. Get images ready. The file structure should be like that given by CityScapes:
    * /home/image/path/leftImg8bit/[train, val, test]/[cities]/id_leftImg8bit.png
2. Write configuration file `annotaion/cityscapesLabelTool.conf`, specify:
    * csPath: /home/image/path
    * imgsize: [imgHeight, imgWidth]

2. Initialize `id_polygon.json`:

    ```bash
    python initialization/initializer.py
    ```

3. Start Label tool:

    ```bash
    python annotation/cityscapesLabelTool.py
    ```

## Label Guide:
