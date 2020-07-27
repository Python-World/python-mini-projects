from PIL import Image

im = Image.open("naruto_first.png").convert("RGB")
im.save("naruto.jpg", "jpeg")
