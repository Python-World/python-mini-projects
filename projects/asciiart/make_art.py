#!/usr/bin/env python3

import cv2

def print_out(array):
	'''prints the array line by line'''
	for row in array:
		for e in row:
			if e:
				print('-', end='')
			else:
				print('|', end='')
		print()

def img_to_ascii(image):
    """converts the image to ascii art"""
    
    resized_image = cv2.resize(
        image, (50, 50)
    )  # resize image to fit the printing screen
    _, thresh = cv2.threshold(
        resized_image, 127, 1, 1
    )  # apply threshold to substitute different symbols

    return thresh

if __name__ == "__main__":
    image_path = "sample_image.png"
    image = cv2.imread(image_path, 0)

    ascii_art = img_to_ascii(image)
    print_out(ascii_art)
