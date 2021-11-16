# Image steganography

This project contains two algorithm (LSB and DCT), which can insert some secret but invisible.

**LSB** insert message into Least Significant Bit of each pixels.

**DCT** insert message into Middle Frequency.

## Requirement

Installation:

```shell
$ pip install -r requirements.txt
```

## Usage

Run LSB algorithm

```shell
$ python3 lsb.py
```

Run DCT algorithm

```shell
$ python3 dct.py
```