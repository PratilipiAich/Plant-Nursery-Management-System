from tkinter import *
from PIL import ImageTk,Image

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

import os
from subprocess import call

import sys


root=Tk()
root.title('Categories(As admin)')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')

root.geometry("1000x600")
root.configure(background="green2")
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

def submit():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	#insert into table
	c.execute("INSERT INTO category VALUES(:cat_id,:cat_name)",
			{
				'cat_id': cat_id.get(),
				'cat_name': cat_name.get()
			}
	)
	
	conn.commit()

	#close connection
	conn.close()

	#clear the text boxes
	cat_id.delete(0,END)
	cat_name.delete(0,END)
	print("submitted to database")

def update():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	record_id=select_box.get()
	c.execute("""UPDATE category SET
		cat_id= :cat_id,
		cat_name=:cat_name
		
		WHERE cat_id=:cat_id""",
		{
		'cat_id': cat_id_editor.get(),
		'cat_name':cat_name_editor.get(),
		
		'cat_id':record_id
		})

	conn.commit()
	conn.close()

	editor.destroy()


def edit():
	global editor
	editor=Tk()
	editor.title('Edit a plant record')
	editor.iconbitmap('C:/Users/Dell/Desktop/DBMS_Project/Pratilipi/Plant-Nursery-Management-System/Images/nursery.ico')

	editor.geometry("700x700")
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
	c.execute("SELECT * FROM category WHERE cat_id= "+ record_id)
	records=c.fetchall()
	#print(records)

	#create global variables for text box names
	global cat_id_editor
	global cat_name_editor
	#create text boxes
	cat_id_editor=Entry(frame2,width=30)
	cat_id_editor.grid(row=0,column=1,padx=20,pady= (10,0))
	cat_name_editor=Entry(frame2,width=30)
	cat_name_editor.grid(row=1,column=1,padx=20)

	#create text box labels
	cat_id_label=Label(frame2,text="Category ID",font=('comic sans',14))
	cat_id_label.grid(row=0,column=0, pady=(10,0))
	cat_name_label=Label(frame2,text="Name of category",font=('comic sans',14))
	cat_name_label.grid(row=1,column=0)

	#loop through to get details
	for record in records:
		cat_id_editor.insert(0,record[0])
		cat_name_editor.insert(0,record[1])
	#create a save button
	edit_btn=Button(frame2,text="Save record",command=update,fg='green',bg='white',font=('comic sans',14,'bold'))
	edit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=145)
	

#Create function to delete
def delete():
	#Create a database or connect to one
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')
	#create cursor
	c=conn.cursor()

	#delete a record
	c.execute("DELETE from category WHERE cat_id="+ select_box.get())

	conn.commit()
	conn.close()

def query():
	conn=sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db')

	#create cursor
	c=conn.cursor()

	# Query the  database
	c.execute("SELECT *,cat_id FROM category")
	records=c.fetchall()
	#print(records)

	#Loop through results
	print_records=''
	for record in records:
		print_records+= str(record[0]) + " \t"+ str(record[1]) + " \n"
	#you can also use record[0] and record[1] for printing
	query_label=Label(frame1,text=print_records)
	query_label.grid(row=8,column=0,columnspan=2)
	#commit changes
	conn.commit()

	#close connection
	conn.close()




global frame1
frame1=Frame(root)
frame1.pack(side=TOP,pady=30)
#create text boxes
cat_id=Entry(frame1,width=30)
cat_id.grid(row=0,column=1,padx=20,pady= (10,0))
cat_name=Entry(frame1,width=30)
cat_name.grid(row=1,column=1,padx=20)

#select box added
select_box=Entry(frame1,width=30)
select_box.grid(row=10,column=1,pady=5)

#create labels
cat_id_label=Label(frame1,text="Enter category id",font=('comic sans',14))
cat_id_label.grid(row=0,column=0, pady=(10,0))
cat_name_label=Label(frame1,text="Enter category name",font=('comic sans',14))
cat_name_label.grid(row=1,column=0)

#select text box
select_box_label=Label(frame1,text="Select ID Number to delete/update",font=('comic sans',14))
select_box_label.grid(row=10,column=0,pady=5)


submit_btn=Button(frame1,text="Add record to database",command=submit,fg='green',bg='white',font=('comic sans',14,'bold'))
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create query button
def btn1():
	root.destroy()
	call(["python","C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/categorydisplay.py"])
query_btn=Button(frame1,text="Show all records",command=btn1,fg='green',bg='white',font=('comic sans',14,'bold'))
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

