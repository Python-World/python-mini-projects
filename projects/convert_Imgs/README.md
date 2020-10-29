# Convert Image Format

These scripts can change format of images from PNG to JPG and JPG to PNG

### Prerequisites

Required Modules
- PIL==1.1.6

To install:
```
$ pip install -r requirements.txt
```

### How to run the script

- Dynamic Change
    Copy the script `convertDynamic.py` into the directory where images
    are (PNG and/or JPG). And run:
    ``` bash
    $ python convertDynamic.py
    ```
    This will convert all JPG images to PNG and PNG images to JPG
	in the present directory tree recursively
	(i.e. will change format in images inside sub-directories too.)
- JPG to PNG (single image)
    1. Copy the JPG image to the directory where `JPGtoPNG.py` exists
    2. Replace file name `naruto_first.jpg` inside `JPGtoPNG.py`
	   (line 3) to input file name (JPG).
    3. Replace file name `naruto.png` inside `JPGtoPNG.py`(line 4) to
       output file name (PNG).
    4. Run following command:
      ```
      $ python JPGtoPNG.py
      ```
- PNG to JPG (single image)
    1. Copy the PNG image in directory where `PNGtoJPG.py` exists
    2. Replace file name `naruto_first.png` inside `PNGtoJPG.py`
	   (line 3) to input file name (PNG).
    3. Replace file name `naruto.jpg` inside `PNGtoJPG.py`
	   (line 4) to output file name (JPG).
    4. Run following command:
      ```
      $ python PNGtoJPG.py
      ```

## *Author Name*

[Ramon Ferreira](https://github.com/ramonfsk)
