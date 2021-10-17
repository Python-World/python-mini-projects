"""
Instructions
1. Install captcha: pip install captcha
2. download fonts and update the path in code
3. run the code
"""

from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['C:/Users/Administrator/Downloads/ChelseaMarketsr.ttf', 'C:/Users/Administrator/Downloads/DejaVuSanssr.ttf'])

random=str(randint(100000,999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random,'out.png')

def verify():
    global random
    x=t1.get("0.0",END)
    if (int(x)==int(random)):
        messagebox.showinfo("sucsess", "verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
        random=str(randint(100000,999999))
        data = image.generate(random)
        assert isinstance(data, BytesIO)
        image.write(random,'out.png')
        photo = PhotoImage(file="out.png")
        l1.config(image=photo,height=100,width=200)
        l1.update()
        UpdateLabel()
    
root=Tk()
photo = PhotoImage(file="out.png")

l1=Label(root,image=photo,height=100,width=200)
t1=Text(root,height=5,width=50)
b1=Button(root,text="submit",command=verify)
b2=Button(root,text="refresh",command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()



