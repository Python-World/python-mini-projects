from PIL import Image
import sys
import os

try:
  im = None
  for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith('.jpg'):
          im = Image.open(filename).convert("RGB")
          im.save(filename.replace('jpg', 'png'), "png")
        elif filename.endswith('.png'):
          im = Image.open(filename).convert("RGB")
          im.save(filename.replace('png', 'jpg'), "jpeg")
        else:
          print('dont have image to convert')
except IOError:
  print('directory empty!')
  sys.exit()
