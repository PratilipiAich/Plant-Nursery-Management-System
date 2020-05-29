from tkinter import *
from PIL import ImageTk,Image

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import os
from subprocess import call

import sys


root=Tk()
root.title('Plants(As Admin)')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

root.geometry("1000x600")
root.configure(background="green")
#scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)


#databases

#create a database or connect to one
conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/garden.db')

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
	c.execute("""UPDATE plant SET
		pid= :pid,
		name=:name,
		season=:season,
		plant_category=:plant_category,
		description=:description,
		price=:price,
		sid=:sid

		WHERE pid=:pid""",
		{
		'pid': pid_editor.get(),
		'name':name_editor.get(),
		'season':season_editor.get(),
		'plant_category':category_editor.get(),
		'description':description_editor.get(),
		'price':price_editor.get(),	
		'sid':sid_editor.get(),	

		'pid':record_id
		})

	conn.commit()
	conn.close()

	editor.destroy()

def edit():
	global editor
	editor=Tk()
	editor.title('Edit a plant record')
	editor.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')
	global frame2
	frame2=Frame(editor)
	frame2.pack(side=TOP,pady=80)
	editor.geometry("600x600")
	editor.configure(background="green")
	#connecting saved record to database
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	# Query the  database
	c.execute("SELECT * FROM plant WHERE pid= "+ record_id)
	records=c.fetchall()
	#print(records)

	#create global variables for text box names
	global pid_editor
	global name_editor
	global season_editor	
	global category_editor
	global description_editor
	global price_editor
	global sid_editor
	#create text boxes
	pid_editor=Entry(frame2,width=30)
	pid_editor.grid(row=0,column=1,padx=20,pady= (10,0))
	name_editor=Entry(frame2,width=30)
	name_editor.grid(row=1,column=1,padx=20)
	season_editor=Entry(frame2,width=30)
	season_editor.grid(row=2,column=1,padx=20)
	category_editor=Entry(frame2,width=30)
	category_editor.grid(row=3,column=1,padx=20)
	description_editor=Entry(frame2,width=30)
	description_editor.grid(row=4,column=1,padx=20)
	price_editor=Entry(frame2,width=30)
	price_editor.grid(row=5,column=1,padx=20)
	sid_editor=Entry(frame2,width=30)
	sid_editor.grid(row=6,column=1,padx=20)

	#create text box labels
	pid_label=Label(frame2,text="Plant ID",font=('comic sans',14))
	pid_label.grid(row=0,column=0, pady=(10,0))
	name_label=Label(frame2,text="Name of plant",font=('comic sans',14))
	name_label.grid(row=1,column=0)
	season_label=Label(frame2,text="Season",font=('comic sans',14))
	season_label.grid(row=2,column=0)
	category_label=Label(frame2,text="Category of plant",font=('comic sans',14))
	category_label.grid(row=3,column=0)
	description_label=Label(frame2,text="Description about the plant",font=('comic sans',14))
	description_label.grid(row=4,column=0)
	price_label=Label(frame2,text="Price",font=('comic sans',14))
	price_label.grid(row=5,column=0)
	sid_label=Label(frame2,text="Supplier ID",font=('comic sans',14))
	sid_label.grid(row=6,column=0)


	#loop through to get details
	for record in records:
		pid_editor.insert(0,record[0])
		name_editor.insert(0,record[1])
		season_editor.insert(0,record[2])
		category_editor.insert(0,record[3])
		description_editor.insert(0,record[4])
		price_editor.insert(0,record[5])
		sid_editor.insert(0,record[6]) 
	#create a save button
	edit_btn=Button(frame2,text="Save record",command=update,fg="Green", bg="white",font=('Times',20,'bold'))
	edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)
	

#Create function to delete
def delete():
	#Create a database or connect to one
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')
	#create cursor
	c=conn.cursor()

	#delete a record
	c.execute("DELETE from plant WHERE pid="+ select_box.get())

	conn.commit()
	conn.close()


def submit():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	#insert into table
	c.execute("INSERT INTO plant VALUES(:pid,:name,:season,:plant_category,:description,:price,:sid)",
			{
				'pid': pid.get(),
				'name': name.get(),
				'season': season.get(),
				'plant_category': category.get(),
				'description': description.get(),
				'price': price.get(),
				'sid': sid.get()
			}
	)
	#commit changes
	conn.commit()

	#close connection
	conn.close()

	#clear the text boxes
	pid.delete(0,END)
	name.delete(0,END)
	season.delete(0,END)
	category.delete(0,END)
	description.delete(0,END)
	price.delete(0,END)
	sid.delete(0,END)

'''def query():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	# Query the  database
	c.execute("SELECT *,pid FROM PLANT")
	records=c.fetchall()
	#print(records)

	#Loop through results
	print_records=''
	for record in records:
		print_records+= str(record[0]) + " \t"+ str(record[1]) + " \t" + str(record[5])+ " \n"
	#you can also use record[0] and record[1] for printing
	query_label=Label(frame1,text=print_records,font=('comic sans',10))
	query_label.grid(row=9,column=0,columnspan=2)
	#commit changes
	conn.commit()

	#close connection
	conn.close()'''


global frame1
frame1=Frame(root)
frame1.pack(side=TOP,pady=5)


#create text boxes
pid=Entry(frame1,width=30)
pid.grid(row=0,column=1,padx=20,pady= (5,0))
name=Entry(frame1,width=30)
name.grid(row=1,column=1,padx=20)
season=Entry(frame1,width=30)
season.grid(row=2,column=1,padx=20)
category=Entry(frame1,width=30)
category.grid(row=3,column=1,padx=20)
description=Entry(frame1,width=30)
description.grid(row=4,column=1,padx=20)
price=Entry(frame1,width=30)
price.grid(row=5,column=1,padx=20)
sid=Entry(frame1,width=30)
sid.grid(row=6,column=1,padx=20)
#creating a delete box
#delete_box=Entry(frame1,width=30)
#delete_box.grid(row=9,column=1,pady=5)

#creating a select box
select_box=Entry(frame1,width=30)
select_box.grid(row=10,column=1,pady=5)

#create text box labels
pid_label=Label(frame1,text="Plant ID",font=('comic sans',14))
pid_label.grid(row=0,column=0, pady=(5,0))
name_label=Label(frame1,text="Name of plant",font=('comic sans',14))
name_label.grid(row=1,column=0)
season_label=Label(frame1,text="Season of growth",font=('comic sans',14))
season_label.grid(row=2,column=0)
category_label=Label(frame1,text="Category",font=('comic sans',14))
category_label.grid(row=3,column=0)
description_label=Label(frame1,text="Description",font=('comic sans',14))
description_label.grid(row=4,column=0)
price_label=Label(frame1,text="Price",font=('comic sans',14))
price_label.grid(row=5,column=0)
sid_label=Label(frame1,text="Supplier ID",font=('comic sans',14))
sid_label.grid(row=6,column=0)
#delete box label
#delete_box_label=Label(frame1,text="Delete ID Number to delete")
#delete_box_label.grid(row=9,column=0,pady=5)
#select box label
select_box_label=Label(frame1,text="Select ID Number to delete/update",font=('comic sans',14))
select_box_label.grid(row=10,column=0,pady=3)


def btn1():
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/plants.py"])
# create subit button
submit_btn=Button(frame1,text="Add record to database",command=submit,fg="Green", bg="white",font=('Times',12,'bold'))
submit_btn.grid(row=7,column=0,columnspan=2,pady=3,padx=10,ipadx=100)

#create query button
query_btn=Button(frame1,text="Show record of plants",command=btn1,fg="Green", bg="white",font=('Times',12,'bold'))
query_btn.grid(row=8,column=0,columnspan=2,pady=3,padx=10,ipadx=137)

#create a delete button
delete_btn=Button(frame1,text="Delete record",command=delete,fg="Green", bg="white",font=('Times',12,'bold'))
delete_btn.grid(row=11,column=0,columnspan=2,pady=3,padx=10,ipadx=135)

# updating records
#select_btn=Button(frame1,text="Select record",command=delete)
#select_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

edit_btn=Button(frame1,text="Update record",command=edit,fg="Green", bg="white",font=('Times',12,'bold'))
edit_btn.grid(row=12,column=0,columnspan=2,pady=3,padx=10,ipadx=145)



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
