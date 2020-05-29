from tkinter import *
from PIL import ImageTk,Image

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import os
from subprocess import call

import sys

root=Tk()
root.title('Admin Space')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')
root.geometry("1000x600") 
root.configure(background="green")
mylabel=Label(root,text="Welcome admin! View and manage records from here.",font=("Arial Bold", 20), bg="orange", fg="white")
mylabel.pack(side=TOP,pady=80)

def click_details1():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/database.py"])
def click_details2():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/customer.py"])
def click_details3():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/category.py"])
def click_details4():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/supplier.py"])
def click_details5():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/orders.py"])

frame1=Frame(root)
frame1.pack(side=TOP,pady=30)

myButton1= Button(frame1,text="Plants", command=click_details1, fg="green", bg="white",font=('Times',20,'bold'))
myButton1.grid(row=1,column=1,pady=5)

myButton2= Button(frame1,text="Customers", command=click_details2, fg="green", bg="white",font=('Times',20,'bold'))
myButton2.grid(row=2,column=1,pady=5)

myButton3= Button(frame1,text="Categories", command=click_details3, fg="green", bg="white",font=('Times',20,'bold'))
myButton3.grid(row=3,column=1,pady=5)

myButton4= Button(frame1,text="Supplier", command=click_details4, fg="green", bg="white",font=('Times',20,'bold'))
myButton4.grid(row=4,column=1,pady=5)

myButton5= Button(frame1,text="Orders", command=click_details5, fg="green", bg="white",font=('Times',20,'bold'))
myButton5.grid(row=5,column=1,pady=5)

'''def Home():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/GUI.py"])'''

def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
def logout():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        root.destroy()
        call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/login.py"])
    	# wanted to destroy the window and then logout back to login page.....

'''frame_sticky1=Frame(root)
frame_sticky1.pack(side=LEFT,expand=YES,pady=30)
frame_sticky_btn1=Button(frame_sticky1,text="Home",command=Home,fg="blue",bg="white",font=('Times',20,'bold'))
frame_sticky_btn1.grid(row=0,column=0,padx=10)'''


frame_sticky2=Frame(root)
frame_sticky2.pack(side=LEFT,pady=30,expand=YES)
frame_sticky_btn2=Button(frame_sticky2,text="Logout",command=logout,fg="blue",bg="white",font=('Times',20,'bold'))
frame_sticky_btn2.grid(row=0,column=1,padx=10)

frame_sticky3=Frame(root)
frame_sticky3.pack(side=LEFT,pady=30,expand=YES)
frame_sticky_btn3=Button(frame_sticky3,text="Exit",command=Exit,fg="blue",bg="white",font=('Times',20,'bold'))
frame_sticky_btn3.grid(row=0,column=2,padx=10)



root.mainloop()
