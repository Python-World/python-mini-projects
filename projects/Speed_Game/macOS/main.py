import tkinter.font as tkFont
from tkinter import messagebox
import pandas as pd
import os
import random
from PIL import Image, ImageTk
import time
import threading
from tkinter import messagebox

try:
    import tkinter as tk
except:
    import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ImagePath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack(side='bottom')
        self.img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        canv.create_text((600 // 2), (500 // 2) - 40, fill="white", text="Speed Game", font=labelFont)

        startBtnFont = tkFont.Font(family="Consolas", size=20)
        startBtn = tk.Button(canv, text="START", font=startBtnFont, foreground="black", background="black",
                             relief="ridge", borderwidth=5, highlightbackground="yellow",
                             activebackground="yellow", activeforeground="black",
                             command=lambda: master.switch_frame(CategoryPage))
        canv.create_window((600 // 2), (500 // 2) + 100, window=startBtn)


class CategoryPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ImagePath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack(side='bottom')
        self.img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        canv.create_text((600 // 2), (500 // 2) - 190, fill="white", text="Speed Game", font=labelFont)

        btnFont = tkFont.Font(family="Consolas", size=20)
        countryBtn = tk.Button(self, text="country", foreground="black",
                               width=15, height=1,
                               background="yellow", font=btnFont, relief="ridge",
                               borderwidth=5, highlightbackground="yellow",
                               activebackground="yellow", activeforeground="yellow",
                               command=lambda: master.switch_frame(CountryPage))
        canv.create_window((600 // 2), (500 // 2) - 100, window=countryBtn)

        prevBtn = tk.Button(self, text="preve page", foreground="black",
                            width=15, height=1,
                            background="yellow", font=btnFont, relief="ridge",
                            borderwidth=5, highlightbackground="yellow",
                            activebackground="yellow", activeforeground="yellow",
                            command=lambda: master.switch_frame(StartPage))
        canv.create_window((600 // 2), (500 // 2) - 10, window=prevBtn)


class CountryPage(tk.Frame):
    def __init__(self, master):
        global pass_count, answer, country_img
        global df, pass_window
        tk.Frame.__init__(self, master)

        filename = random.choice(os.listdir("./images"))
        code = filename.split(".")[0]

        # data not in excel file 
        while code.upper() not in df.index:
            filename = random.choice(os.listdir("./images"))
            code = filename.split(".")[0]

        countryPath = "./images/" + filename

        print(countryPath)
        print(df["country"][code.upper()])
        print(filename)
        answer = df["country"][code.upper()]

        backgroundPath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack()
        self.img1 = ImageTk.PhotoImage(Image.open(backgroundPath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img1)

        titleFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        canv.create_text((600 // 2), (500 // 2) - 190, fill="white", text="Country", font=titleFont)

        self.img2 = ImageTk.PhotoImage(Image.open(countryPath).resize((180, 130), Image.ANTIALIAS))
        country_img = canv.create_image(210, 130, anchor="nw", image=self.img2)

        labelFont = tkFont.Font(family="Arial", size=17, slant="italic")
        BtnFont = tkFont.Font(family="Consolas", size=15)

        canv.create_text((600 // 2), (500 // 2) + 40, fill="white", text="answer", font=labelFont)

        input_text = tk.Entry(self, width=30)
        canv.create_window((600 // 2), (500 // 2) + 70, window=input_text)

        check_btn = tk.Button(self, text="check",
                              width=10, height=1, font=BtnFont, foreground="black",
                              background="yellow", relief="ridge",
                              activebackground="yellow", activeforeground="black",
                              command=lambda: self.checkBtn_click(master, input_text.get(), answer, canv,country_img))
        canv.create_window((600 // 2) - 80, (500 // 2) + 140, window=check_btn)

        pass_btn = tk.Button(self, text="pass: " + str(pass_count) + "/3",
                             width=10, height=1, font=BtnFont, foreground="black",
                             background="yellow", relief="ridge",
                             activebackground="yellow", activeforeground="black",
                             command=lambda: self.passBtn_click(tk, canv, country_img))
        pass_window = canv.create_window((600 // 2) + 80, (500 // 2) + 140, window=pass_btn)

        self.num = 180
        mins, secs = divmod(self.num, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        TimerFont = tkFont.Font(family="Arial", size=30, weight="bold", slant="italic")
        timer_text = canv.create_text(100, 100, fill="white", text=timeformat, font=TimerFont)
        canv.after(1, self.count, canv, timer_text)

    def count(self, canv, timer_text):
        mins, secs = divmod(self.num, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        canv.delete(timer_text)
        TimerFont = tkFont.Font(family="Arial", size=30, weight="bold", slant="italic")
        timer_text = canv.create_text(100, 100, fill="white", text=timeformat, font=TimerFont)
        self.num -= 1
        if self.num < 0:
            msgBox = tk.messagebox.askretrycancel('Exit App', 'Really Quit?')
            if msgBox == True:
                self.master.switch_frame(StartPage)
            else:
                self.master.switch_frame(FinishPage)
        else:
            canv.after(1000, self.count, canv, timer_text)

    # click check button
    def checkBtn_click(self, master, user_text, check_answer, canv, check_img):
        global answer, country_img
        global correct_count, problem_count
        problem_count -= 1

        user_text = user_text.upper().replace(" ", "")
        check_answer = check_answer.replace(" ", "")

        if (user_text == check_answer):
            # correct
            print('correct')
            ImagePath = 'correct.png'
            self.img3 = ImageTk.PhotoImage(Image.open(ImagePath).resize((100, 100), Image.ANTIALIAS))
            resultImage = canv.create_image(450, 30, anchor="nw", image=self.img3)
            correct_count += 1
        else:
            # wrong
            print('wrong')
            ImagePath = 'wrong.png'
            self.img4 = ImageTk.PhotoImage(Image.open(ImagePath).resize((100, 100), Image.ANTIALIAS))

            resultImage = canv.create_image(450, 30, anchor="nw", image=self.img4)

        # resolve 15 problems
        if problem_count <= 0:
            master.switch_frame(FinishPage)
        canv.after(1000, self.delete_img, canv, resultImage)
        filename = random.choice(os.listdir("./images"))
        code = filename.split(".")[0]

        # data not in excel file 
        while code.upper() not in df.index:
            filename = random.choice(os.listdir("./images"))
            code = filename.split(".")[0]

        countryPath = "./images/" + filename
        canv.after(1000,self.delete_img, canv, check_img)
        self.img2 = ImageTk.PhotoImage(Image.open(countryPath).resize((180, 130), Image.ANTIALIAS))
        country_img = canv.create_image(210, 130, anchor="nw", image=self.img2)
        answer = df["country"][code.upper()]

        print(answer)

    def passBtn_click(self, tk, canv, check_img):
        global pass_count, pass_window
        global country_img, answer
        pass_count = pass_count - 1
        if (pass_count < 0):
            print("패스 그만")
            pass_count = 0
            tk.messagebox.showerror('Pass', 'You Don\'t have pass ticket!')
        else:
            filename = random.choice(os.listdir("./images"))
            code = filename.split(".")[0]

            # data not in excel file 
            while code.upper() not in df.index:
                filename = random.choice(os.listdir("./images"))
                code = filename.split(".")[0]

            countryPath = "./images/" + filename
            canv.after(1000, self.delete_img, canv, check_img)
            self.img2 = ImageTk.PhotoImage(Image.open(countryPath).resize((180, 130), Image.ANTIALIAS))
            country_img = canv.create_image(210, 130, anchor="nw", image=self.img2)
            answer = df["country"][code.upper()]

        self.delete_img(canv, pass_window)
        BtnFont = tkFont.Font(family="Consolas", size=15)
        pass_btn = tk.Button(self, text="pass: " + str(pass_count) + "/3",
                             width=10, height=1, font=BtnFont, foreground="yellow",
                             background="black", relief="ridge",
                             activebackground="yellow", activeforeground="black",
                             command=lambda: self.passBtn_click(tk, canv, country_img))
        pass_window = canv.create_window((600 // 2) + 80, (500 // 2) + 140, window=pass_btn)

    def delete_img(self, canv, dele_img_name):
        canv.delete(dele_img_name)


class FinishPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ImagePath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack(side='bottom')
        self.img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold")
        canv.create_text((600 // 2), (500 // 2) - 50, fill="white", text="total score : " + str(correct_count)+ "/15", font=labelFont)
        canv.create_text((600 // 2), (500 // 2) + 50, fill="white", text="Good Job!", font=labelFont)


if __name__ == "__main__":
    #pygame.init()
    #mySound = pygame.mixer.Sound("SpeedGameBgm.mp3")
    #mySound.play(-1)
    pass_count = 3
    problem_count = 15
    correct_count = 0
    answer = 0
    country_img = 0
    pass_window = 0

    df = pd.read_excel("./CountryCodeData.xlsx", index_col=0, names=["code", "country"])
    print(df["country"]["KR"])

    app = SampleApp()
    app.title("Speed Game")

    app.geometry('600x500+100+100')
    app.mainloop()
