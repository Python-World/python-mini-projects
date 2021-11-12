import os
import os.path as osp
import math
import time
from util import wgs84_to_baidu, get_rectangle, get_baidu_poi
import argparse


def run(args):
    baidu_web_ak = args.ak
    wgs_l_x, wgs_l_y, wgs_r_x, wgs_r_y = args.range
    kernel_x, kernel_y = args.ksize
    rec_index = args.idx
    roi_key = args.poi
    output = args.save
    if not osp.exists(output):
        os.makedirs(output)
    rec_index -= 1
    l_x, l_y = wgs84_to_baidu(wgs_l_x, wgs_l_y, baidu_web_ak)
    r_x, r_y = wgs84_to_baidu(wgs_r_x, wgs_r_y, baidu_web_ak)
    print("lonlat of the upper right point: ", l_x, l_y)
    print("lonlat of the lower left point: ", r_x, r_y)
    num_x = math.ceil((r_x - l_x) / kernel_x)
    num_y = math.ceil((r_y - l_y) / kernel_y)
    num_rec = num_x * num_y
    print("number of grids: ", num_rec)
    for idx in range(rec_index, num_rec):
        rec_str = get_rectangle(l_x, l_y, r_x, r_y, kernel_x, kernel_y, idx)
        print("No ", (idx+1), ", current area coordinates: ", rec_str)
        get_baidu_poi(roi_key, rec_str, baidu_web_ak, idx, output)
        print("current area completed")
        time.sleep(1)


parser = argparse.ArgumentParser(description="input parameters")
parser.add_argument("--ak", type=str, required=True, help="Baidu web ak")
parser.add_argument("--range", type=float,nargs='+', required=True, help="Latlon of the lower left point and latlon of the upper right point")
parser.add_argument("--poi", type=str, required=True, help="POI key")
parser.add_argument("--save", type=str, default="output", help="Save path")
parser.add_argument("--ksize", type=float, nargs='+', default=[0.5, 0.5])
parser.add_argument("--idx", type=int, default=1)


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)