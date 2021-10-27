from tkinter import *
from tkinter import messagebox
from typing import Counter


root = Tk()
root.title("My Tic Toc Toe")


my_menu = Menu(root)
root.config(menu=my_menu)
option_menu = Menu(my_menu, tearoff=FALSE)

my_menu.add_cascade(label="Options", menu=option_menu)


def whoseTurn():
    global clicked
    return "X" if clicked is True else "O"


def disable_all_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def is_win():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
    global clicked, count

    if(b1["text"] != " " and (b1["text"] == b4["text"] == b7["text"])):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b2["text"] != " " and (b2["text"] == b5["text"] == b8["text"])):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b3["text"] != " " and (b3["text"] == b6["text"] == b9["text"])):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b1["text"] != " " and (b1["text"] == b2["text"] == b3["text"])):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b4["text"] != " " and (b4["text"] == b5["text"] == b6["text"])):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b7["text"] != " " and (b7["text"] == b8["text"] == b9["text"])):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b1["text"] != " " and (b1["text"] == b5["text"] == b9["text"])):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif(b3["text"] != " " and (b3["text"] == b5["text"] == b7["text"])):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        b10["text"] = f"{whoseTurn()} Won"
        disable_all_button()

    elif (count == 9):
        b10["text"] = "Its tie, No one Won!!"
        disable_all_button()


def b_click(b):
    global clicked, count, b10

    if b["text"] == " ":
        b["text"] = whoseTurn()
        count += 1
        b10["text"] = "X Turn" if clicked is False else "O Turn"
        is_win()
        clicked = not clicked


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
    global clicked, count

    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica,20"), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b10 = Button(root, text=f'{whoseTurn()} Turn', font=(
        "Helvetica,20"), height=2, width=20, bg="Black", fg="white")

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    b10.grid(row=3, columnspan=3)


option_menu.add_command(label="Reset Game", command=reset)
reset()
root.mainloop()
