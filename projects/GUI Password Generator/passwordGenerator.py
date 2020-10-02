from tkinter import *
import string
import random

root = Tk()
root.title("Password Generator - By Rohit")
root.geometry("1000x700")
root.wm_iconbitmap("pass.ico")
# Function to generate a password
def generate():
    if passLen.get() == 0:
        TextArea.insert(1.0, "Please Enter password length.")
    else:
        TextArea.delete(1.0, END)
        if passType.get() == 1:
            s1 = string.digits
            s = []
            s.extend(s1)
            random.shuffle(s)
            password = "".join(s[0:passLen.get()])
            TextArea.insert(1.0, f"Your password is : {password}")
        elif passType.get() == 2:
            s1 = string.ascii_lowercase
            s2 = string.digits
            s = []
            s.extend(s1)
            s.extend(s2)
            random.shuffle(s)
            password = "".join(s[0:passLen.get()])
            TextArea.insert(1.0, f"Your password is : {password}")
        elif passType.get() == 3:
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            s = []
            s.extend(s1)
            s.extend(s2)
            s.extend(s3)
            s.extend(s4)
            random.shuffle(s)
            password = "".join(s[0:passLen.get()])
            TextArea.insert(1.0, f"Your password is : {password}")

        else:
            TextArea.insert(1.0, "Invalid Password Type\n")

# Length of password
passLen = IntVar()
passLen.set(0)
passType = IntVar()

Label(root, text="Welcome to Password Generator", font="lucida 20 bold").pack(pady=10)
f1 = Frame(root)
# Label for Enter Password length
l1 = Label(f1, text="Enter password length", font="lucida 10 bold")
l1.grid(row=1, column=3, pady=20)

# Entry widget
e1 = Entry(f1, textvariable=passLen)
e1.grid(row=1, column=5)

# Radiobuttons for password type
r1 = Radiobutton(f1, text="PIN", value=1, variable=passType, padx=10, font="lucida 12").grid(row=2, column=4, )
r2 = Radiobutton(f1, text="AlphaNumeric", value=2, variable=passType, padx=10, font="lucida 12").grid(row=3, column=4)
r3 = Radiobutton(f1, text="Extreme Secure", value=3, variable=passType, padx=10, font="lucida 12").grid(row=4, column=4)

# Submit Button
b1 = Button(f1, text="Submit", command=generate, font="lucida 12")
b1.grid(row=5, column=4, pady=10)

# Textarea to show generated password
TextArea = Text(f1)
TextArea.grid(row=6, column=4)

f1.pack()


root.mainloop()