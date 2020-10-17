import cv2                             #importing Opencv2
import matplotlib.pyplot as plt        #importing the matplotlib
import cvlib as cv                     #importing the opencv library for object detection.
from cvlib.object_detection import draw_bbox          #importing draw_bbox(for drawing the box around detected object)
im = cv2.imread('img1.jpg')                           #input image(you can replace 'img1.jpg' with your image)
bbox, label, conf = cv.detect_common_objects(im)      #code for the detection of objects
output_image = draw_bbox(im, bbox, label, conf)       #code for pre-presenting the image
plt.imshow(output_image)                              #to plot the output image
plt.show()                                            #output
