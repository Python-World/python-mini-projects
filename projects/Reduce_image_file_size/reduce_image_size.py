import cv2

img = cv2.imread('input.jpg')

print(img.shape)

# rescalling image
width = int((img.shape[1])/5)
height = int((img.shape[0])/5)

scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

print(scaled.shape)

cv2.imshow("Output",scaled)
cv2.waitKey(500)
cv2.destroyAllWindows()

cv2.imwrite('resized_output_image.jpg',scaled)

