from tkinter import *
from tkinter import ttk
import sqlite3

import os.path
import os
from subprocess import call

root = Tk()
root.geometry("1250x700") 
root.configure(background="green3")
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')
root.title('Plants')

#data = [ ["val1", "val2", "val3"],
         #["asd1", "asd2", "asd3"],
         #["bbb1", "bbb3", "bbb4"],
         #["ccc1", "ccc3", "ccc4"],
         #["ddd1", "ddd3", "ddd4"],
         #["eee1", "eee3", "eee4"] ]



frame = Frame(root)
frame.pack()

def btn3():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/custuser.py"])

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
#filemenu.add_command(label='New') 
#filemenu.add_command(label='Open...') 
#filemenu.add_command(label='Back', command=btn3) 
#filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 

def connect():
    conn = sqlite3.connect("C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db")
    cur = conn.cursor()
    conn.close()


def View():
    conn = sqlite3.connect("C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db")
    cur = conn.cursor()
    cur.execute("SELECT pid, name, season, plant_category, description, price FROM plant")
    rows = cur.fetchall()
    for row in rows:
       # print(row) # it print all records in the database
        records=cur.fetchall()
        tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    conn.close()


connect()



tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6), height = 20, padding = 3, show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="ID")
tree.heading(2, text="NAME")
tree.heading(3, text="SEASON")
tree.heading(4, text="CATEGORY")
tree.heading(5, text="DESCRIPTION")
tree.heading(6, text="PRICE")


tree.column(1, width = 100)
tree.column(2, width = 100)
tree.column(3, width = 100)
tree.column(4, width = 100)
tree.column(5, width = 800)
tree.column(6, width = 100)

tree.pack()
b2 = ttk.Button(text="view data", command=View)
b2.pack()

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side = 'right', fill = 'y')

tree.configure(yscrollcommand=scroll.set)


root.mainloop()