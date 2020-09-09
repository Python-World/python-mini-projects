import os 
from PIL import Image


dir_path = os.path.dirname(os.path.realpath(__file__))

im1 = Image.open('input.jpeg')

im1.save('output.png')
