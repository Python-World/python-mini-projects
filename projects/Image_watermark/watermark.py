import os
from PIL import Image
from PIL import ImageFilter


def watermark_photo(input_image_path, output_image_path, watermark_image_path):

    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    # add watermark to your image
    position = base_image.size

    watermark.size

    newsize = int(position[0] * 8 / 100), int(position[0] * 8 / 100)

    watermark = watermark.resize(newsize)
    # Blur If Needed
    # watermark = watermark.filter(ImageFilter.BoxBlur(2))
    new_position = position[0] - newsize[0] - 20, position[1] - newsize[1] - 20

    transparent = Image.new(mode="RGBA", size=position, color=(0, 0, 0, 0))
    # Create a new transparent image
    transparent.paste(base_image, (0, 0))
    # paste the original image

    transparent.paste(watermark, new_position, mask=watermark)
    # paste the watermark image
    image_mode = base_image.mode
    if image_mode == "RGB":
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert("P")
    transparent.save(output_image_path, optimize=True, quality=100)
    print("Saving " + output_image_path + " ...")


folder = input("Enter Folder Path : ")

watermark = input("Enter Watermark Path : ")

os.chdir(folder)
files = os.listdir(os.getcwd())

if not os.path.isdir("output"):
    os.mkdir("output")

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png") or f.endswith(".jpg"):
            watermark_photo(f, "output/" + f, watermark)

