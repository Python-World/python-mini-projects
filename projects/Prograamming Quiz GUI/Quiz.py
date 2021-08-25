from tkinter import *
from tkinter import messagebox
from questions import *

class Project:
    def __init__(self):
        self.que=None
        self.ans=None
        self.correct=0
        self.count=-1
        self.__correct_answer=None
        self.__answer=None
        self.__question=None

    def course(self):
        self.correct=0
        self.count=-1
        B.config(text="Start")
        if s.get()=="Python":
            self.que=python_que
            self.ans=python_ans
        elif s.get()=="C":
            self.que=c_que
            self.ans=c_ans
        elif s.get()=="Java":
            self.que=java_que
            self.ans=java_ans

    def set_(self):
        if self.que==None:
            messagebox.showinfo("Error","Please select course first...")
            return
        self.count+=1

        if self.count==len(self.que):
            messagebox.showinfo("Result","You have answered {0} out of {1} questions correctly".format(self.correct,self.count))
            exit()

        if(self.count==len(self.que)-1):
            B.config(text="Finish")
        else:
            B.config(text="Next")

        self.__question=self.que[self.count]
        self.__answer=self.ans[self.__question]
        l.config(text=self.__question)
        for i in range(0,4):
            v[i].set(self.__answer[i])
        self.__correct_answer=self.__answer[4]
    
    def fun(self,y,n):
        if y==self.__correct_answer:
            self.correct+=1
            n.config(activebackground="green")
        else:
            n.config(activebackground="red")
        self.set_()

        
   
obj=Project()
scr=Tk(className="quiz")
s=StringVar()
main_menu=Menu(scr)
file_menu=Menu(main_menu,tearoff=0)

course_menu=Menu(file_menu,tearoff=0)
course_menu.add_radiobutton(label="Python",value="Python",variable=s,command=obj.course)
course_menu.add_radiobutton(label="C",value="C",variable=s,command=obj.course)
course_menu.add_radiobutton(label="Java",value="Java",variable=s,command=obj.course)

file_menu.add_cascade(label="Course",menu=course_menu)
file_menu.add_command(label="Exit",command=exit)
main_menu.add_cascade(label="file",menu=file_menu)
scr.config(menu=main_menu)

l=Label(scr,font=("consolas",20),relief="groove",width=40,height=2,wraplength=600,bg="steel blue")
l.grid(row=0,column=0,columnspan=20,sticky="news")

b=[]
for i in range(0,4):
    b.append(Button())
v=[]
for i in range(0,4):
    v.append(StringVar())

   
b[0]=Button(scr,textvariable=v[0],font=("consolas",20),anchor="w",width=20,activebackground="light blue",command=lambda :obj.fun(v[0].get(),b[0]))
b[0].grid(row=2,column=0,sticky=W)

b[1]=Button(scr,textvariable=v[1],font=("consolas",20),anchor="w",width=20,command=lambda :obj.fun(v[1].get(),b[1]))
b[1].grid(row=2,column=1,sticky=S)

b[2]=Button(scr,textvariable=v[2],font=("consolas",20),anchor="w",width=20,command=lambda :obj.fun(v[2].get(),b[2]))
b[2].grid(row=3,column=0,sticky=W)

b[3]=Button(scr,textvariable=v[3],font=("consolas",20),anchor="w",width=20,command=lambda :obj.fun(v[3].get(),b[3]))
b[3].grid(row=3,column=1,sticky=S)

B=Button(scr,text="Start",font=("consolas",20),width=40,height=1,bg="black",fg="white",command=obj.set_)
B.grid(row=10,column=0,columnspan=2,sticky="news")
#B.geometry('{0}x{1}+0+0'.format(scr.winfo_screenwidth(),200))

scr.mainloop()
