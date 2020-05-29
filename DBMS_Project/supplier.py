from tkinter import *
from PIL import ImageTk,Image

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import os
from subprocess import call

import sys

root=Tk()
root.title('Supplier Details(As Admin)')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

root.geometry("600x600")
root.configure(background='green')

#databases

#create a database or connect to one
conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

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

#create table
'''
c.execute("""CREATE TABLE plant(
		pid integer,
		name text,
		price integer,
		about text,
		season text,
		catid integer 
		)""")
'''

#create function to update a record
def update():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	c.execute("""UPDATE supplier SET
		sid= :sid,
		sup_name=:sup_name,
		sup_phone=:sup_phone,
		sup_address=:sup_address

		WHERE sid=:sid""",
		{
		'sid': sid_editor.get(),
		'sup_name':sup_name_editor.get(),
		'sup_phone':sup_phone_editor.get(),
		'sup_address':sup_address_editor.get(),
		'sid':record_id
		})

	conn.commit()
	conn.close()

	editor.destroy()

def edit():
	global editor
	editor=Tk()
	editor.title('Edit a supplier record')
	editor.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

	editor.geometry("600x600")
	editor.configure(background="green")
	global frame2
	frame2=Frame(editor)
	frame2.pack(side=TOP,pady=80)
	#connecting saved record to database
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	# Query the  database
	c.execute("SELECT * FROM supplier WHERE sid= "+ record_id)
	records=c.fetchall()
	#print(records)

	#create global variables for text box names
	global sid_editor
	global sup_name_editor
	global sup_phone_editor
	global sup_address_editor	

	#create text boxes
	sid_editor=Entry(frame2,width=30)
	sid_editor.grid(row=0,column=1,padx=20,pady= (10,0))
	sup_name_editor=Entry(frame2,width=30)
	sup_name_editor.grid(row=1,column=1,padx=20)
	sup_phone_editor=Entry(frame2,width=30)
	sup_phone_editor.grid(row=2,column=1,padx=20)
	sup_address_editor=Entry(frame2,width=30)
	sup_address_editor.grid(row=3,column=1,padx=20)
	
	#create text box labels
	sid_label=Label(frame2,text="Supplier ID",font=('comic sans',14))
	sid_label.grid(row=0,column=0, pady=(10,0))
	sup_name_label=Label(frame2,text="Name of supplier",font=('comic sans',14))
	sup_name_label.grid(row=1,column=0)
	sup_phone_label=Label(frame2,text="Phone number of supplier",font=('comic sans',14))
	sup_phone_label.grid(row=2,column=0)
	sup_address_label=Label(frame2,text="Supplier address",font=('comic sans',14))
	sup_address_label.grid(row=3,column=0)

	#loop through to get details
	for record in records:
		sid_editor.insert(0,record[0])
		sup_name_editor.insert(0,record[1])
		sup_phone_editor.insert(0,record[2])
		sup_address_editor.insert(0,record[3])
	#create a save button
	edit_btn=Button(frame2,text="Save record",command=update,fg='green',bg='white',font=('comic sans',14,'bold'))
	edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)
	

#Create function to delete
def delete():
	#Create a database or connect to one
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')
	#create cursor
	c=conn.cursor()

	#delete a record
	c.execute("DELETE from supplier WHERE sid="+ select_box.get())

	conn.commit()
	conn.close()


def submit():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	#insert into table
	c.execute("INSERT INTO supplier VALUES(:sid,:sup_name,:sup_phone,:sup_address)",
			{
				'sid': sid.get(),
				'sup_name': sup_name.get(),
				'sup_phone': sup_phone.get(),
				'sup_address': sup_address.get()
			}
	)
	#commit changes
	conn.commit()

	#close connection
	conn.close()

	#clear the text boxes
	sid.delete(0,END)
	sup_name.delete(0,END)
	sup_phone.delete(0,END)
	sup_address.delete(0,END)
	
def query():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	# Query the  database
	c.execute("SELECT *,sid FROM supplier")
	records=c.fetchall()
	#print(records)

	#Loop through results
	print_records=''
	for record in records:
		print_records+= str(record[0]) + " \t"+ str(record[1]) + " \t" + str(record[2])+ " \n"
	#you can also use record[0] and record[1] for printing
	query_label=Label(frame1,text=print_records,font=('comic sans',14))
	query_label.grid(row=8,column=0,columnspan=2)
	#commit changes
	conn.commit()

	#close connection
	conn.close()



#create text boxes

frame1=Frame(root)
frame1.pack(side=TOP,pady=80)
sid=Entry(frame1,width=30)
sid.grid(row=0,column=1,padx=20,pady= (10,0))
sup_name=Entry(frame1,width=30)
sup_name.grid(row=1,column=1,padx=20)
sup_phone=Entry(frame1,width=30)
sup_phone.grid(row=2,column=1,padx=20)
sup_address=Entry(frame1,width=30)
sup_address.grid(row=3,column=1,padx=20)

#creating a delete box
#delete_box=Entry(root,width=30)
#delete_box.grid(row=9,column=1,pady=5)

#creating a select box
select_box=Entry(frame1,width=30)
select_box.grid(row=10,column=1,pady=5)

#create text box labels
sid_label=Label(frame1,text="Supplier ID",font=('comic sans',14))
sid_label.grid(row=0,column=0, pady=(10,0))
sup_name_label=Label(frame1,text="Name of supplier",font=('comic sans',14))
sup_name_label.grid(row=1,column=0)
sup_phone_label=Label(frame1,text="Phone number of supplier",font=('comic sans',14))
sup_phone_label.grid(row=2,column=0)
sup_address_label=Label(frame1,text="Address of supplier",font=('comic sans',14))
sup_address_label.grid(row=3,column=0)

#delete box label
#delete_box_label=Label(root,text="Delete ID Number to delete")
#delete_box_label.grid(row=9,column=0,pady=5)
#select box label
select_box_label=Label(frame1,text="Select ID Number to delete/update",font=('comic sans',14))
select_box_label.grid(row=10,column=0,pady=5)

# create subit button
submit_btn=Button(frame1,text="Add record to database",command=submit,fg='green',bg='white',font=('comic sans',14,'bold'))
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create query button
def btn1():
	root.destroy()
	call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/supdisplay.py"])
query_btn=Button(frame1,text="Show record of suppliers",command=btn1,fg='green',bg='white',font=('comic sans',14,'bold'))
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create a delete button
delete_btn=Button(frame1,text="Delete record",command=delete,fg='green',bg='white',font=('comic sans',14,'bold'))
delete_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=135)

# updating records
#select_btn=Button(root,text="Select record",command=delete)
#select_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

edit_btn=Button(frame1,text="Update record",command=edit,fg='green',bg='white',font=('comic sans',14,'bold'))
edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)


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
