from tkinter import *
class medium:
    def user(self,color): # takes user' choice
        self.color=color
    def __init__(self): # generates random palette
        a=['#270101', '#F08B33', '#776B04', '#F1B848', '#8F715B', '#0486DB', '#C1403D', '#F3D4A0']
        import random
        self.b=[];n=4;
        while n!=0: 
            p=random.choice(a)
            if p not in self.b:
                self.b.append(p)
                n-=1
    def compare(self,g,l1):
        l=[] # hints           
        for x in range(4):
            if l1[x]==g[x]:
                l.append('red')
            elif l1[x]in g:
                l.append('gray')
        return l
class MasterMind():
    def __init__(self, root):
        obj=medium()
        self.gen=obj.b  # generated color combo
        self.colors = ['#270101', '#F08B33', '#776B04', '#F1B848', '#8F715B', '#0486DB', '#C1403D', '#F3D4A0']
        root.geometry('390x600')
        for y in range(20):
            Grid.rowconfigure(root, y, weight=1)
        for x in range(8):
            Grid.columnconfigure(root, x, weight=1)
        self.palette = [] # display of palette
        n,c=0,0
        for i in self.colors:
            self.palette.append(Button(root, bg=i, height=1, width=5, relief=SUNKEN))
            self.palette[n].grid(row=20, column=c)
            n+=1;c+=1;
        self.palette[0].config(command=lambda: self.guess(root, self.palette[0]['bg'],obj))         # binding function to palette
        self.palette[1].config(command=lambda: self.guess(root, self.palette[1]['bg'],obj))
        self.palette[2].config(command=lambda: self.guess(root, self.palette[2]['bg'],obj))
        self.palette[3].config(command=lambda: self.guess(root, self.palette[3]['bg'],obj))
        self.palette[4].config(command=lambda: self.guess(root, self.palette[4]['bg'],obj))
        self.palette[5].config(command=lambda: self.guess(root, self.palette[5]['bg'],obj))
        self.palette[6].config(command=lambda: self.guess(root, self.palette[6]['bg'],obj))
        self.palette[7].config(command=lambda: self.guess(root, self.palette[7]['bg'],obj))
        self.user_choice = []  # stores the widget
        self.code = []  # stores the colors
        self.key = []  # stores the hints
        global ccol, cro
        ccol,cro = 2,19
    def guess(self, root, choice,obj):
            global ccol
            global cro
            f=True  # boolean flag
            if cro != 1:
                self.user_choice.append(Button(root, bg=choice, height=1, width=5, relief=RAISED))
                if len(self.user_choice) < 4:
                    self.user_choice[-1].grid(row=cro, column=ccol)
                    self.code.append(self.user_choice[-1]['bg'])
                    ccol += 1
                elif len(self.user_choice) == 4:
                    self.user_choice[-1].grid(row=cro, column=ccol)
                    self.code.append(self.user_choice[-1]['bg'])
                    ccol += 1
                    ccol = 2
                    cro = cro-1
                    obj.user(self.code) # send the user's choice
                    self.key=obj.compare(self.code,self.gen) #get the hints
                    if self.key==['red','red','red','red']:
                        f=False
                        self.hint(root, self.key)
                        l=Label(root,text="CONGRATULATIONS!!!")
                        l.grid(row=0,columnspan=8)
                    else:
                        self.hint(root, self.key)
                        self.code = []
                        self.user_choice = []
            else:
                if f:
                    l=Label(root,text="You are a LOSER!!!!        ANSWER:")
                    l.grid(row=0,columnspan=4)
                    c=5
                    for i in self.gen:                        
                        b=Button(root,bg=i,height=1, width=5, relief=SUNKEN)
                        b.grid(row=0,column=c)
                        c+=1
    global hcol, hro
    hcol,hro = 8,19
    def hint(self, root, key):
        global hcol, hro
        a = []
        for i in key:
            a.append(Label(root, bg=i,relief=SUNKEN))
            a[-1].grid(row=hro, column=hcol, sticky=E)
            hcol += 1
        hro -= 1;hcol = 8;
master = Tk()
M = MasterMind(master)
master.mainloop()
