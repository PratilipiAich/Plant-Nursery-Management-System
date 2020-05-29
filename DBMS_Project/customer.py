from tkinter import *
from PIL import ImageTk,Image

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import os
from subprocess import call

import sys


root=Tk()
root.title('Customer Details(As Admin)')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')
root.configure(background="green")

root.geometry("1000x500")

conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')#database name inside quotes

#create cursor
c=conn.cursor()

'''def update():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	c.execute("""UPDATE customer SET 
		cid=:cid,
		name=:name,
		phone=:phone,
		address=:address,
		ussername=:ussername,
		password=:password

		WHERE uid=:uid""",
		{
		'uid': cid_editor.get(),
		'name':name_editor.get(),
		'phone':phone_editor.get(),
		'address':address_editor.get()
		})

	conn.commit()
	conn.close()

	editor.destroy()'''


'''def submit():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	#insert into table
	c.execute("INSERT INTO customer VALUES(:uid,:name,:phone,:address,:ussername,:password)",
			{
				'uid': cid.get(),
				'name': name.get(),
				'phone': phone.get(),
				'address': address.get()
				
			}
	)
	#commit changes
	conn.commit()

	#close connection
	conn.close()

	#clear the text boxes
	
	name.delete(0,END)
	phone.delete(0,END)
	address.delete(0,END)'''
	
	
'''def edit():
	global editor
	editor=Tk()
	global frame2
	
	frame2=Frame(editor)
	frame2.pack(side=TOP, pady=30)

	editor.title('Edit a record')
	editor.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

	editor.geometry("1250x700")
	#connecting saved record to database
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	# Query the  database
	c.execute("SELECT * FROM customer WHERE uid= "+ record_id)
	records=c.fetchall()
	#print(records)

	#create global variables for text box names
	global cid_editor
	global name_editor
	global phone_editor
	global address_editor	
	global ussername_editor	
	global password_editor	
	#create text boxes
	cid_editor=Entry(frame2,width=30)
	cid_editor.grid(row=0,column=1,padx=20,pady= (10,0))
	name_editor=Entry(frame2,width=30)
	name_editor.grid(row=1,column=1,padx=20)
	phone_editor=Entry(frame2,width=30)
	phone_editor.grid(row=2,column=1,padx=20)
	address_editor=Entry(frame2,width=30)
	address_editor.grid(row=3,column=1,padx=20)

	#create text box labels
	cid_label=Label(frame2,text="Customer ID",font=('comic sans',14))
	cid_label.grid(row=0,column=0, pady=(10,0))
	name_label=Label(frame2,text="Customer Name",font=('comic sans',14))
	name_label.grid(row=1,column=0)
	phone_label=Label(frame2,text="Phone number",font=('comic sans',14))
	phone_label.grid(row=2,column=0)
	address_label=Label(frame2,text="Address",font=('comic sans',14))
	address_label.grid(row=3,column=0)

	#loop through to get details
	for record in records:
		cid_editor.insert(0,record[0])
		name_editor.insert(0,record[1])
		phone_editor.insert(0,record[2])
		address_editor.insert(0,record[3])
		
	#create a save button
	edit_btn=Button(frame2,text="Save record",font=('comic sans',14),command=update)
	edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)'''
	
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

def delete():
	#Create a database or connect to one
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')
	#create cursor
	c=conn.cursor()

	#delete a record
	c.execute("DELETE from user WHERE cid="+select_box.get())

	conn.commit()
	conn.close()

global frame1
frame1=Frame(root)
frame1.pack(side=TOP, pady=30)
#create text boxes
'''cid=Entry(frame1,width=30)
cid.grid(row=0,column=1,padx=20,pady= (10,0))
name=Entry(frame1,width=30)
name.grid(row=1,column=1,padx=20)
phone=Entry(frame1,width=30)
phone.grid(row=2,column=1,padx=20)
address=Entry(frame1,width=30)
address.grid(row=3,column=1,padx=20)'''

#select box added
select_box=Entry(frame1,width=30)
select_box.grid(row=10,column=1,pady=5)


#create labels
'''cid_label=Label(frame1,text="Enter customer id",font=('comic sans',14))
cid_label.grid(row=0,column=0, pady=(10,0))
name_label=Label(frame1,text="Enter name",font=('comic sans',14))
name_label.grid(row=1,column=0)
phone_label=Label(frame1,text="Enter phone",font=('comic sans',14))
phone_label.grid(row=2,column=0)
address_label=Label(frame1,text="Enter address",font=('comic sans',14))
address_label.grid(row=3,column=0)'''

#select text box
select_box_label=Label(frame1,text="Select ID Number to delete/",font=('comic sans',14))
select_box_label.grid(row=10,column=0,pady=5)


'''submit_btn=Button(frame1,text="Add record to database",font=('comic sans',14),command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)'''

#create query button

def btn1():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/admincust.py"])
query_btn=Button(frame1,text="Show record of all customers",font=('comic sans',14),command=btn1)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create a delete button
delete_btn=Button(frame1,text="Delete record",font=('comic sans',14),command=delete)
delete_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=135)

# updating records
#select_btn=Button(root,text="Select record",command=delete)
#select_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

'''edit_btn=Button(frame1,text="Update record",font=('comic sans',14),command=edit)
edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)'''

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



conn.commit()
conn.close()
root.mainloop()

