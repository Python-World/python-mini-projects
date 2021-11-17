import os
import os.path as osp
from util import get_baidu_poi
import argparse


def run(args):
    baidu_web_ak = args.ak
    city_str = args.city
    roi_key = args.poi
    output = args.save
    if not osp.exists(output):
        os.makedirs(output)
    get_baidu_poi(roi_key, city_str, baidu_web_ak, output)
    print("current area completed")


parser = argparse.ArgumentParser(description="input parameters")
parser.add_argument("--ak", type=str, required=True, help="Baidu web ak")
parser.add_argument("--city", type=str, required=True, help="City name")
parser.add_argument("--poi", type=str, required=True, help="POI key")
parser.add_argument("--save", type=str, default="output", help="Save path")


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)