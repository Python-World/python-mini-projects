import pyautogui
import time

print("""
╔═══╗─────────╔══╗───╔╗
║╔═╗║─────────║╔╗║──╔╝╚╗
║╚══╦══╦══╦╗╔╗║╚╝╚╦═╩╗╔╝
╚══╗║╔╗║╔╗║╚╝║║╔═╗║╔╗║║
║╚═╝║╚╝║╔╗║║║║║╚═╝║╚╝║╚╗
╚═══╣╔═╩╝╚╩╩╩╝╚═══╩══╩═╝
────║║
────╚╝
""")

msg = input("Message : ")
msg_count = int(input("Message Count : "))

print("Starting in 5...")
time.sleep(1)
print("Starting in 4...")
time.sleep(1)
print("Starting in 3...")
time.sleep(1)
print("Starting in 2...")
time.sleep(1)
print("Starting in 1...")
time.sleep(1)
print("Boom!")

for _ in range(0, int(msg_count)):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
