#!/usr/bin/env python3
#
# Copyright(C) 2021 wuyaoping
#
# DCT algorithm has great a robust but lower capacity.

import numpy as np
import os.path as osp
import cv2

FLAG = '%'
# Select a part location from the middle frequency
LOC_MAX = (4, 1)
LOC_MIN = (3, 2)
# The difference between MAX and MIN,
# bigger to improve robust but make picture low quality.
ALPHA = 1

# Quantizer table
TABLE = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])


def insert(path, txt):
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    txt = "{}{}{}".format(len(txt), FLAG, txt)
    row, col = img.shape[:2]
    max_bytes = (row // 8) * (col // 8) // 8
    assert max_bytes >= len(
        txt), "Message overflow the capacity:{}".format(max_bytes)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # Just use the Y plane to store message, you can use all plane
    y, u, v = cv2.split(img)
    y = y.astype(np.float32)
    blocks = []
    # Quantize blocks
    for r_idx in range(0, 8 * (row // 8), 8):
        for c_idx in range(0, 8 * (col // 8), 8):
            quantized = cv2.dct(y[r_idx: r_idx+8, c_idx: c_idx+8]) / TABLE
            blocks.append(quantized)
    for idx in range(len(txt)):
        encode(blocks[idx*8: (idx+1)*8], txt[idx])

    idx = 0
    # Restore Y plane
    for r_idx in range(0, 8 * (row // 8), 8):
        for c_idx in range(0, 8 * (col // 8), 8):
            y[r_idx: r_idx+8, c_idx: c_idx+8] = cv2.idct(blocks[idx] * TABLE)
            idx += 1
    y = y.astype(np.uint8)
    img = cv2.cvtColor(cv2.merge((y, u, v)), cv2.COLOR_YUV2BGR)
    filename, _ = osp.splitext(path)
    # DCT algorithm can save message even if jpg
    filename += '_dct_embeded' + '.jpg'
    cv2.imwrite(filename, img)
    return filename


# Encode a char into the blocks
def encode(blocks, data):
    data = ord(data)
    for idx in range(len(blocks)):
        bit_val = (data >> idx) & 1
        max_val = max(blocks[idx][LOC_MAX], blocks[idx][LOC_MIN])
        min_val = min(blocks[idx][LOC_MAX], blocks[idx][LOC_MIN])
        if max_val - min_val <= ALPHA:
            max_val = min_val + ALPHA + 1e-3
        if bit_val == 1:
            blocks[idx][LOC_MAX] = max_val
            blocks[idx][LOC_MIN] = min_val
        else:
            blocks[idx][LOC_MAX] = min_val
            blocks[idx][LOC_MIN] = max_val


# Decode a char from the blocks
def decode(blocks):
    val = 0
    for idx in range(len(blocks)):
        if blocks[idx][LOC_MAX] > blocks[idx][LOC_MIN]:
            val |= 1 << idx
    return chr(val)


def extract(path):
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    row, col = img.shape[:2]
    max_bytes = (row // 8) * (col // 8) // 8
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(img)
    y = y.astype(np.float32)
    blocks = []
    for r_idx in range(0, 8 * (row // 8), 8):
        for c_idx in range(0, 8 * (col // 8), 8):
            quantized = cv2.dct(y[r_idx: r_idx+8, c_idx: c_idx+8]) / TABLE
            blocks.append(quantized)
    res = ''
    idx = 0
    # Extract the length of the message
    while idx < max_bytes:
        ch = decode(blocks[idx*8: (idx+1)*8])
        idx += 1
        if ch == FLAG:
            break
        res += ch
    end = int(res) + idx
    assert end <= max_bytes, "Input image isn't correct."
    res = ''
    while idx < end:
        res += decode(blocks[idx*8: (idx+1)*8])
        idx += 1
    return res


if __name__ == '__main__':
    data = 'A collection of simple python mini projects to enhance your Python skills.'
    res_path = insert('./example.png', data)
    res = extract(res_path)
    print(res)
