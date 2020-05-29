from tkinter import *
from PIL import ImageTk,Image

import os
from subprocess import call

import sys

root=Tk()
root.title('Welcome to HeavenlyPlantNursery.com')
root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')
root.geometry("1000x600") 
root.configure(background="green")
#creating a label
#myLabel=Label(root,  text="Plants")
#myLabel1=Label(root, text="PID")
#myLabel2=Label(root, text="Name")
#shoving label to screen
#myLabel.grid()
#myLabel1.grid(row=1,column=0)
#myLabel2.grid(row=2,column=0)

canvas=Canvas(root,bg="blue",width=250,height=300)
my_img= ImageTk.PhotoImage(Image.open("C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/pic1.png"))
myLabel5=Label(image=my_img)
myLabel5.pack()

#e= Entry(root, width=50, borderwidth=5)#fg,bg
#e.pack()
#e.insert(0,"Enter the plant id")#dislays text inside the box in entry button--the default text

#def click_details():
#	myLabel3=Label(root, text="The details will arrive shortly")
#	myLabel3.pack()

#myButton= Button(root,text="Get details", command=click_details, fg="Green", bg="white")
#myButton.pack()
# below is an entry button
#you can use a variable to print the text e.g. t1="This is for pid:"+e.get()
'''
def click_details1():
	global login
	login=Tk()
	login.title('Login To Your Account')
	login.iconbitmap('c:/Users/dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_SENT/DBMS_SENT/Images/nursery.ico')

	login.geometry("400x400")
	#connecting saved record to database
	#conn=sqlite3.connect('plant_nursery.db')

	#create cursor
	#c=conn.cursor()

	myLabel4=Label(login, text="You have logged in succesfully")
	myLabel4.grid(row=2,column=0,padx=3,pady=3)


	#conn.commit()
	#conn.close()
'''
'''
class Buttons:
	
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.b2 = Button(self.master, text="Button2", command=self.new_window)
		#self.b1.pack()
		self.b2.pack()
		self.frame.pack()

	def new_window(self):
		self.master.withdraw()
		self.newWindow = Toplevel(self.master)

		bb = Buttons1(self.newWindow)
'''

def click_details1():
	root.destroy()
	call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/login.py"])

def click_details2():
	root.destroy()
	call(["python","C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/login.py"])


'''def click_details3():
	root.destroy()
    call(["python", "register.py"])'''


myLabel5=Label(root,text="Welcome to HeavenlyPlantNursery", font=("Arial Bold", 20), bg="orange", fg="white")
myLabel5.pack(pady=5)
myLabel6=Label(root,text="Planning to build a garden? Decorating your house? Or just some flowers to beautify your backyard?", font=("Arial Bold", 17), bg="green", fg="AntiqueWhite")
myLabel6.pack(pady=5)
myLabel7=Label(root,text="You've come to the right place!", font=("Arial Bold", 17), bg="green", fg="AntiqueWhite")
myLabel7.pack(pady=5)
myLabel8=Label(root,text="Register or Log in for more details.", font=("Arial Bold", 17), bg="green", fg="AntiqueWhite")
myLabel8.pack(pady=5)

myButton1= Button(root,text="Login/Register", command=click_details1, fg="Green", bg="white",font=('Times',20,'bold'))
myButton1.pack(padx=5,pady=3,expand=YES,side=LEFT)

'''myButton2= Button(root,text="Register", command=click_details3, fg="Green", bg="white",font=('Times',20,'bold'))
myButton2.pack(padx=5,pady=5,expand=YES,side=LEFT)'''

'''myButton2= Button(root,text="Admin Login", command=click_details2, fg="Green", bg="white",font=('Times',20,'bold'))
myButton2.pack(padx=5,pady=5,expand=YES,side=LEFT)'''

button_quit=Button(root,text="Exit Program",command=root.quit,fg='Green',bg='white',font=('Times',20,'bold'))
button_quit.pack(padx=5,pady=5,expand=YES,side=LEFT)
root.mainloop()

'''
class Buttons1:
	
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
	#	self.b3 = Button(self.master, text="Button3", command=self.display3)
	#	self.b3.pack()
		self.frame.pack()
		

	#def display3(self):
	#	print ('hello button3')


if __name__ == '__main__':
	root = Tk()
	b = Buttons(root)
	root.mainloop()
'''
