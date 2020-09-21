from PIL import Image
# Take input image from present folder
img = Image.open('input.png')
# Generate and save output image to present folder
img.save('output.ico') 