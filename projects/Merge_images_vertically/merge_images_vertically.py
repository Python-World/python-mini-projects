import numpy as np
import PIL
from PIL import Image
import os
from os import listdir
from os.path import isfile, join

def merge_pics_vertically(images_list, name):
    imgs = [Image.open(i) for i in images_list]
    min_img_width = min(i.width for i in imgs)

    total_height = 0
    for i, img in enumerate(imgs):
        if img.width > min_img_width:
            imgs[i] = img.resize((min_img_width, int(img.height / img.width * min_img_width)), Image.ANTIALIAS)
        total_height += imgs[i].height

    img_merge = Image.new(imgs[0].mode, (min_img_width, total_height))
    y = 0
    for img in imgs:
        img_merge.paste(img, (0, y))
        y += img.height
    img_merge.save(name + '.jpg')

def get_files(directory, ext = [".jpg"]):
    files = []
    for f in os.scandir(directory):
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)
    return files

name = input("Sub-folder with images to be merged: ")
path = os.getcwd() + "/" + name
pictures = get_files(path)
merge_pics_vertically(pictures, path)



