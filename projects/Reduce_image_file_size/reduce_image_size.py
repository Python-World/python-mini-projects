# import openCV library for image handling
import cv2

# read image to be resized by imread() function of openCV library
img = cv2.imread('input.jpg')
print(img.shape)

# set the ratio of resized image
k = 5
width = int((img.shape[1])/k)
height = int((img.shape[0])/k)

# resize the image by resize() function of openCV library
scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
print(scaled.shape)

# show the resized image using imshow() function of openCV library
cv2.imshow("Output", scaled)
cv2.waitKey(500)
cv2.destroyAllWindows()

# get the resized image output by imwrite() function of openCV library
cv2.imwrite('resized_output_image.jpg', scaled)
