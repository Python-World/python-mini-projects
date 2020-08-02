#!/usr/bin/env python3

import cv2
import numpy as np

def print_out(array):
	'''prints the array line by line'''

	symbols = ['#','-','*','.','+','o']
	for row in array:
		for e in row:
			print(symbols[int(e)%len(symbols)], end='')
		print()

def img_to_ascii(image):
    """returns the numeric coded image"""
    
    width, height = image.shape
    width = int(width/18)
    height = int(height/10)
    # resize image to fit the printing screen
    resized_image = cv2.resize(
        image, (height, width),
    )  

    threshold_list = [0,50,100,150,200]
    thresh_image = np.zeros(resized_image.shape)
    
    for i, threshold in enumerate(threshold_list):
    	thresh_image[resized_image > threshold] = i
    return thresh_image

if __name__ == "__main__":
    image_path = '/home/akash/Downloads/2017505508.jpg' 
    image = cv2.imread(image_path, 0)

    ascii_art = img_to_ascii(image)
    print_out(ascii_art)
