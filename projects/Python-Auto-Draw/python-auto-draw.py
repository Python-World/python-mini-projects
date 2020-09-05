import pyautogui
import time

# time to change tabs from editor to paint;
time.sleep(10)

# it will remain clicked till program ends;
pyautogui.click()

# can be varied according to convininence
distance = 250

while distance > 0:
    # right
    pyautogui.dragRel(distance, 0, duration = 0.1)
    
    distance -= 5

    # down
    pyautogui.dragRel(0, distance, duration = 0.1)

    # left
    pyautogui.dragRel(-distance, 0, duration = 0.1)

    distance -= 5

    #up
    pyautogui.dragRel(0, -distance, duration = 0.1)

