import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
import time
'''
For running this game:
1)Run code 
2)open chrome type:chrome://dino
Note: After running code you should start dino game within 3 seconds
'''

def hit(key):
    pyautogui.keyDown(key)
    return

# This is going to make two triangles that detect black colour and then jumps or down
#  when it hits black colour like cactus and bird
def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):# change it according to your need
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
