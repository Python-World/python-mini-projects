
# NETWORK USAGE TRACKER

# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from pil import ImageTk, Image
import time
import psutil
import socket

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Network Usage Tracker") # title given is "DICTIONARY"
window1.geometry('1000x700')

# top label
start1 = tk.Label(text = "NETWORK USAGE\nTRACKER", font=("Arial", 55,"underline"), fg="magenta") # same way bg
start1.place(x = 150, y = 10)

def start_fun():
    window1.destroy()

# start button created
startb = Button(window1, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =130 , y =590 )

# image on the main window
path = "Images/front.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window1, image = img1)
panel.place(x = 320, y = 200)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# exit button created
exitb = Button(window1, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 590 )
window1.protocol("WM_DELETE_WINDOW", exit_win)
window1.mainloop()

# main window created
window = Tk()
window.title("Network Usage Tracker")
window.geometry("1000x700")

# top label
top1 = Label(window, text="NETWORK USAGE\nTRACKER", font=("Arial", 50,'underline'), fg="magenta")
top1.place(x = 190, y = 10)

top1 = Label(window, text="MAX LIMIT  :  1 MB/sec", font=("Arial", 50), fg="green")
top1.place(x = 130, y = 180)

# text area
path_text = Text(window, height=1, width=24, font=("Arial", 50), bg="white", fg="blue",borderwidth=2, relief="solid")
path_text.place(x=50, y = 300)

# l1 = Label(window, fg='blue', font=("Arial", 50))
# l1.place(x = 80, y = 300)

top1 = Label(window, text="Connection Status :", font=("Arial", 50), fg="green")
top1.place(x = 200, y = 450)

l2 = Label(window, fg='blue', font=("Arial", 30))
l2.place(x = 200, y = 530)

def convert_to_gbit(value):
    return value/1024./1024./1024.*8

# function defined to update the usage instantly
old_value = 0
def update_label():
    global old_value
    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    # if old_value:
    # send_stat(new_value - old_value)
    x = "{0:.3f}".format(new_value - old_value)
    # l1.configure(text="")
    # l1.configure(text= "Usage : " + str(x) + " bytes/sec")
    path_text.delete("1.0", "end")
    path_text.insert(END, "Usage : " + str(x) + " bytes/sec")

    # for updating connection status
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        l2.configure(text="No internet, your localhost is\n" + IPaddress)
    else:
        l2.configure(text="Connected, with the IP address\n" + IPaddress)

    # for checking max limit exceeded
    if(new_value - old_value>1000000):
        mbox.showinfo("Exceed Status", "Max Limit Usage Exceeded.")

    old_value = new_value

    time.sleep(0.5)
    window.after(1, update_label)

update_label()


# function for exiting window
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()