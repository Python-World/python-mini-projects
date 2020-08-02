#!/usr/bin/env python3

import cv2

def draw(image):
    '''prints the ascii art of the given image'''
    pass

if __name__ == '__main__':
    image_path = 'sample_image.png'
    image = cv2.imread(image_path)

    draw(image)
