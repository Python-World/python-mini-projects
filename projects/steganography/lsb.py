#!/usr/bin/env python3
#
# Copyright(C) 2021 wuyaoping
#
# LSB algorithm has a great capacity but fragile.

import cv2
import math
import os.path as osp
import numpy as np

# Insert data in the low bit.
# Lower make picture less loss but lower capacity.
BITS = 2

HIGH_BITS = 256 - (1 << BITS)
LOW_BITS = (1 << BITS) - 1
BYTES_PER_BYTE = math.ceil(8 / BITS)
FLAG = '%'


def insert(path, txt):
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    # Save origin shape to restore image
    ori_shape = img.shape
    max_bytes = ori_shape[0] * ori_shape[1] // BYTES_PER_BYTE
    # Encode message with length
    txt = '{}{}{}'.format(len(txt), FLAG, txt)
    assert max_bytes >= len(
        txt), "Message overflow the capacity:{}".format(max_bytes)
    data = np.reshape(img, -1)
    for (idx, val) in enumerate(txt):
        encode(data[idx*BYTES_PER_BYTE: (idx+1) * BYTES_PER_BYTE], val)

    img = np.reshape(data, ori_shape)
    filename, _ = osp.splitext(path)
    # png is lossless encode that can restore message correctly
    filename += '_lsb_embeded' + ".png"
    cv2.imwrite(filename, img)
    return filename


def extract(path):
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    data = np.reshape(img, -1)
    total = data.shape[0]
    res = ''
    idx = 0
    # Decode message length
    while idx < total // BYTES_PER_BYTE:
        ch = decode(data[idx*BYTES_PER_BYTE: (idx+1)*BYTES_PER_BYTE])
        idx += 1
        if ch == FLAG:
            break
        res += ch
    end = int(res) + idx
    assert end <= total // BYTES_PER_BYTE, "Input image isn't correct."

    res = ''
    while idx < end:
        res += decode(data[idx*BYTES_PER_BYTE: (idx+1)*BYTES_PER_BYTE])
        idx += 1
    return res


def encode(block, data):
    data = ord(data)
    for idx in range(len(block)):
        block[idx] &= HIGH_BITS
        block[idx] |= (data >> (BITS * idx)) & LOW_BITS


def decode(block):
    val = 0
    for idx in range(len(block)):
        val |= (block[idx] & LOW_BITS) << (idx * BITS)
    return chr(val)


if __name__ == '__main__':
    data = 'A collection of simple python mini projects to enhance your Python skills.'
    input_path = "./example.png"
    res_path = insert(input_path, data)
    res = extract(res_path)
    print(res)
