from tkinter import *
from PIL import ImageTk,Image

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import os
from subprocess import call

import sys

#import cv2 was trying to impleent background image but...OK....  :')

root=Tk()
root.title('Orders(As admin)')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

root.geometry("800x800")
root.configure(background="green")
#cv_img=cv2.imread("c:/Users/dell/Desktop/DBMS_Project/Images/pic1.png")
#height, width,no_channels=cv_img.shape
#canvas=Canvas(root,width=width,height=height)
#canvas.pack().....this was for background
conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')#database name inside quotes

#create cursor
c=conn.cursor()

def btn3():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/admin.py"])

menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
#filemenu.add_command(label='New') 
#filemenu.add_command(label='Open...') 
filemenu.add_command(label='Back', command=btn3) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit)

def update():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	c.execute("""UPDATE orders SET 
		oid= :oid,
		cid=:cid,
		pid=:pid,
		quantity=:quantity

		WHERE oid=:oid""",
		{
		'oid': oid_editor.get(),
		'cid':cid_editor.get(),
		'pid':pid_editor.get(),
		'quantity':quantity_editor.get(),
		'oid':record_id
		})

	conn.commit()
	conn.close()

	editor.destroy()


def submit():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	#insert into table
	c.execute("INSERT INTO orders VALUES(:oid,:cid,:pid,:quantity)",
			{
				'oid': oid.get(),
				'cid': cid.get(),
				'pid': pid.get(),
				'quantity': quantity.get()
			}
	)
	#commit changes
	conn.commit()

	#close connection
	conn.close()

	#clear the text boxes
	oid.delete(0,END)
	cid.delete(0,END)
	pid.delete(0,END)
	quantity.delete(0,END)
	

def edit():
	global editor
	editor=Tk()
	frame2=Frame(editor)
	frame2.pack(side=TOP,pady=80)
	editor.title('Edit a record')
	editor.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

	editor.geometry("400x400")
	editor.configure(background='green')
	#connecting saved record to database
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	# Query the  database
	c.execute("SELECT * FROM orders WHERE oid= "+ record_id)
	records=c.fetchall()
	#print(records)

	#create global variables for text box names
	global oid_editor
	global cid_editor
	global pid_editor
	global quantity_editor	

	#create text boxes
	oid_editor=Entry(frame2,width=30)
	oid_editor.grid(row=0,column=1,padx=20,pady= (10,0))
	cid_editor=Entry(frame2,width=30)
	cid_editor.grid(row=1,column=1,padx=20)
	pid_editor=Entry(frame2,width=30)
	pid_editor.grid(row=2,column=1,padx=20)
	quantity_editor=Entry(frame2,width=30)
	quantity_editor.grid(row=3,column=1,padx=20)
	
	#create text box labels
	oid_label=Label(frame2,text="Order ID",font=('comic sans',14))
	oid_label.grid(row=0,column=0, pady=(10,0))
	cid_label=Label(frame2,text="Customer ID",font=('comic sans',14))
	cid_label.grid(row=1,column=0)
	pid_label=Label(frame2,text="Plant id ordered",font=('comic sans',14))
	pid_label.grid(row=2,column=0)
	quantity_label=Label(frame2,text="Quantity ordered",font=('comic sans',14))
	quantity_label.grid(row=3,column=0)

	#loop through to get details
	for record in records:
		oid_editor.insert(0,record[0])
		cid_editor.insert(0,record[1])
		pid_editor.insert(0,record[2])
		quantity_editor.insert(0,record[3])
	#create a save button
	edit_btn=Button(frame2,text="Save record",command=update,fg='green',bg='white',font=('comic sans',14))
	edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)
	

def query():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	# Query the  database
	c.execute("SELECT *,oid FROM orders")
	records=c.fetchall()
	#print(records)

	#Loop through results
	print_records=''
	for record in records:
		print_records+= str(record[0]) + " \t"+ str(record[1]) + " \t" + str(record[3])+ " \n"
	#you can also use record[0] and record[1] for printing
	query_label=Label(frame1,text=print_records)
	query_label.grid(row=8,column=0,columnspan=2)
	#commit changes
	conn.commit()

	#close connection
	conn.close()

	print("record shown")
def delete():
	#Create a database or connect to one
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')
	#create cursor
	c=conn.cursor()

	#delete a record
	c.execute("DELETE from orders WHERE oid="+ select_box.get())

	conn.commit()
	conn.close()

global frame1
frame1=Frame(root)
frame1.pack(side=TOP,pady=80)


#create text boxes
oid=Entry(frame1,width=30)
oid.grid(row=0,column=1,padx=20,pady= (10,0))
cid=Entry(frame1,width=30)
cid.grid(row=1,column=1,padx=20)
pid=Entry(frame1,width=30)
pid.grid(row=2,column=1,padx=20)
quantity=Entry(frame1,width=30)
quantity.grid(row=3,column=1,padx=20)
#select box added
select_box=Entry(frame1,width=30)
select_box.grid(row=10,column=1,pady=5)

#create labels
oid_label=Label(frame1,text="Enter order id",font=('comic sans',14))
oid_label.grid(row=0,column=0, pady=(10,0))
cid_label=Label(frame1,text="Enter customer id",font=('comic sans',14))
cid_label.grid(row=1,column=0)
pid_label=Label(frame1,text="Enter plant id",font=('comic sans',14))
pid_label.grid(row=2,column=0)
quantity_label=Label(frame1,text="Enter quantity",font=('comic sans',14))
quantity_label.grid(row=3,column=0)

#select text box
select_box_label=Label(frame1,text="Select ID Number to delete/update",font=('comic sans',14,'bold'))
select_box_label.grid(row=10,column=0,pady=5)


submit_btn=Button(frame1,text="Add record to database",command=submit,fg='green',bg='white',font=('comic sans',14,'bold'))
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create query button
def btn1():
	root.destroy()
	call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/ordersdisplay.py"])
query_btn=Button(frame1,text="Show record of all orders",command=btn1,fg='green',bg='white',font=('comic sans',14,'bold'))
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create a delete button
delete_btn=Button(frame1,text="Delete record",command=delete,fg='green',bg='white',font=('comic sans',14,'bold'))
delete_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=135)



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

# updating records
#select_btn=Button(root,text="Select record",command=delete)
#select_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

edit_btn=Button(frame1,text="Update record",command=edit,fg='green',bg='white',font=('comic sans',14,'bold'))
edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)


conn.commit()
conn.close()
root.mainloop()

