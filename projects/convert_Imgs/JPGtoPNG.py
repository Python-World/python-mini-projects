from PIL import Image

im = Image.open("naruto_first.jpg").convert("RGB")
im.save("naruto.png", "png")
