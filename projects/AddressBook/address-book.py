from shutil import copyfile
from tkinter import ttk
#import tkinter as tk
from tkinter import *
from tkinter import filedialog 
import os
#from PIL import Image, ImageTk
import sqlite3  

def add_customer():
    
    name = entryName.get()
    phone = entryPhone.get()
    more = entryMore.get()
    
    # Create connection
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    #Insert data
    cur.execute("INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)", (name , phone, more))
    # commit connection
    conn.commit()
    conn.close()
    
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("SELECT*FROM customers order by id desc")
    select = list(select)
    tree.insert('' , END , values = select[0] )
    conn.close()                                     
   
root = Tk()
root.title("Address Book")
root.geometry("550x480")
#root.configure(bg = "#eaeaea")

# Add Title
lblTitle = Label(root , text = "Address Book" , font = ("Arial" , 21) , bg="darkblue" , fg = "white" )
lblTitle.place(x=0 , y=0 , width=250)

# Search area
lbSearchByName = Label(root , text = "Search by name :"  , bg="darkblue" , fg = "white" )
lbSearchByName.place(x=250 , y=0 , width=120)
entrySearchByName = Entry(root)
entrySearchByName.place(x=380 , y=0 , width=160)

lbSearchByPhone = Label(root , text = "Search by name :"  , bg="darkblue" , fg = "white" )
lbSearchByPhone.place(x=250 , y=20 , width=120)
entrySearchByPhone = Entry(root)
entrySearchByPhone.place(x=380 , y=20 , width=160)

# Label & Entry name
lblName = Label(root , text = "Name & surname:" ,  bg="black" , fg = "yellow")
lblName.place(x=5 , y = 50 , width = 125)

entryName = Entry(root)
entryName.place(x = 140,  y =50 , width=400)


# Label & Entry Phone
lblPhone = Label(root , text = "Phone Number:" , bg="black" , fg = "yellow")
lblPhone.place(x=5 , y=80 ,  width = 125 )
entryPhone = Entry(root)
entryPhone.place(x = 140,  y =80 , width=400)


# Label & Entry Photo
lblPhoto = Label(root , text = "Photo:" , bg="black" , fg = "yellow")
lblPhoto.place(x=5 , y=110 ,  width = 125 )
bPhoto = Button(root , text = "Browse" , bg="darkblue" , fg = "yellow" )
bPhoto.place(x= 480 ,  y = 110 , height = 25)
entryPhoto = Entry(root)
entryPhoto.place(x = 140,  y =110 , width=320)

# More Info
lblMore = Label(root , text = "More Info:" , bg="black" , fg = "yellow")
lblMore.place(x=5 , y=140 ,  width = 125 )
entryMore = Entry(root)
entryMore.place(x = 140,  y =140 , width=400)

# Command Button
bAdd = Button(root , text = "Add Customer" , bg="darkblue" , fg = "yellow" , command = add_customer)
bAdd.place(x= 5 ,  y = 170 , width = 255)

bDelete = Button(root , text = "Delete Selected" , bg="darkblue" , fg = "yellow" )
bDelete.place(x= 5 ,  y = 205 , width = 255)

bEdit = Button(root , text = "Edit Selected" , bg="darkblue" , fg = "yellow" )
bEdit.place(x= 5 ,  y = 240 , width = 255)

bSort= Button(root , text = "Sort by name" , bg="darkblue" , fg = "yellow" )
bSort.place(x= 5 ,  y = 275 , width = 255)

bExit= Button(root , text = "Exit App" , bg="darkblue" , fg = "yellow" , command = quit)
bExit.place(x= 5 ,  y = 310 , width = 255)

# Load Image

# Add Treeview
tree = ttk.Treeview(root, columns =(1,2,3), height = 5 , show ="headings")
tree.place(x=265, y=170, width = 290, height = 175)
# Add headings
tree.heading(1, text ="ID")
tree.heading(2, text = "name")
tree.heading(3, text = "Phone")
#Define column width
tree.column(1, width=50)
tree.column(2, width=100)
tree.column(3, width=100)
# Display data in treeview object
conn = sqlite3.connect('database.db')
cur = conn.cursor()
select = cur.execute("select*from customers")
for row in select:
    tree.insert('' , END , values = row)



root.mainloop()