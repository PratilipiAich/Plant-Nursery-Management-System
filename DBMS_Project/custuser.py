from tkinter import *
from PIL import ImageTk,Image
import sqlite3

import os
from subprocess import call

root=Tk()
root.title('Your profile')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

root.geometry("1250x700") 
root.configure(background="green")

#conn=sqlite3.connect('')#database name inside quotes

#create cursor
#c=conn.cursor()


def btn3():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/login.py"])

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Exit', command=root.quit) 

myLabel1=Label(root,text="Welcome User! Explore the wide variety of plants that we offer...", font=("Arial Bold", 20), bg="orange", fg="white")
myLabel1.pack(pady=5)

def btn1():
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/plants.py"])
    

def btn2():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/custdisplay.py"])


username = StringVar()
username.__getattribute__
print(username)
orders_btn=Button(root,text='Explore', width=20, height=1, command=btn1, activebackground="lightblue", bg="AntiqueWhite", fg='green', font=("Arial", 15))
orders_btn.pack(padx=5,pady=3,expand=YES,side=LEFT)

edit_btn=Button(root,text='My Account', width=20, height=1, command=btn2 , activebackground="lightblue", bg="AntiqueWhite", fg='green', font=("Arial", 15))
edit_btn.pack(padx=5,pady=3,expand=YES,side=LEFT)

edit_btn=Button(root,text='Logout', width=20, height=1, command=btn3 , activebackground="lightblue", bg="AntiqueWhite", fg='green', font=("Arial", 15))
edit_btn.pack(padx=5,pady=3,expand=YES,side=LEFT)

#conn.commit()
#conn.close()
root.mainloop()
