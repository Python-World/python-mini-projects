from PIL import Image
from PIL.ExifTags import TAGS
from author_utils import get_file_security, get_author
from gps_utils import get_location
import os
import sys
from datetime import datetime

def get_exif(image):
    image.verify()
    return image._getexif()


def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

im = Image.open(sys.argv[1])

# get the image name
name = im.filename

# get the image size
w, h = im.size

# get the image file extension
_, file_extension = os.path.splitext(sys.argv[1])

# get the exif information
exif = get_exif(im)
labeled = get_labeled_exif(exif)

# get the file creation time
ctime = os.path.getctime(sys.argv[1])

# output information
print("ImageName: %s" %(name))
print("size: %sx%s" % (w, h))
print("FileExtension: %s" %(file_extension))
if ('ExifImageWidth' in labeled.keys()):
    print("ImageWidth: %s" % (labeled['ExifImageWidth']))
else:
    print("No ImageWidth")

if ('ExifImageHeight' in labeled.keys()):
    print("ImageHeight: %s" % (labeled['ExifImageHeight']))
else:
    print("No ImageHeight")

if ('DateTimeOriginal' in labeled.keys()):
    print("DateTimeOriginal: %s" % (labeled['DateTimeOriginal']))
else:
    print("No DateTimeOriginal")

print("CreateDate: %s" % (datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')))
print("Author: %s" % (get_author(sys.argv[1])))
print("Location: %s" % (get_location(sys.argv[1])))
