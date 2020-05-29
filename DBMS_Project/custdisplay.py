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
root.title('Customer Details')

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
filemenu.add_command(label='Back', command=btn3) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 

def connect():
    conn = sqlite3.connect("C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db")
    cur = conn.cursor()
    conn.close()
n_username = StringVar()



def View():
    conn = sqlite3.connect("C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db")
    cur = conn.cursor()
    cur.execute("SELECT username, password, name, phone, address FROM user")
    
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        #records=cur.fetchall()
        #tree.insert("", "end", values=records)
        tree.insert("","end", values=(row[0], row[1], row[2], row[3], row[4]))
    conn.close()

connect()

tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 10, padding = 3, show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="USERNAME")
tree.heading(2, text="PASSWORD")
tree.heading(3, text="NAME")
tree.heading(4, text="PHONE NO.")
tree.heading(5, text="ADDRESS")

tree.column(1, width = 210)
tree.column(2, width = 210)
tree.column(3, width = 210)
tree.column(4, width = 210)
tree.column(5, width = 210)

tree.pack()
b2 = ttk.Button(text="view data", command=View)
b2.pack()

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side = 'right', fill = 'y')

tree.configure(yscrollcommand=scroll.set)


root.mainloop()