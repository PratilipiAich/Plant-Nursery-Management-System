#Python Tkinter and Sqlite3 Login Form
#Made By Namah Jain Form Youtube Channel All About Code
#Please Subscribe To Our Youtube Channel.
#https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber

#imports
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import os
from subprocess import call

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db') as db:
    c = db.cursor()

'''c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()'''

def btn3():
    root.destroy()
    call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/GUI.py"])



#main Class
class main:
    def __init__(self,master):
        root.configure(background="green3")
        root.iconbitmap('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/Images/nursery.ico')
        root.title('Login')
        menu = Menu(root) 
        root.config(menu=menu) 
        filemenu = Menu(menu) 
        menu.add_cascade(label='File', menu=filemenu) 
        #filemenu.add_command(label='New') 
        #filemenu.add_command(label='Open...') 
        filemenu.add_command(label='Back', command=btn3) 
        filemenu.add_separator() 
        filemenu.add_command(label='Exit', command=root.quit)

        root.geometry("1000x500") 
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_name = StringVar()
        self.n_phone = StringVar()
        self.n_address = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            print(self.username.get())
            if self.username.get()=="admin":
                root.destroy()
                call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/admin.py"])
            else:
                root.destroy()
                call(["python", "C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/custuser.py"])
                
            '''self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150'''
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('C:/Users/Dell/Desktop/Pratilipi/Plant-Nursery-Management-System/DBMS_Project/garden.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(name,phone,address,username,password) VALUES(?,?,?,?,?)'
        c.execute(insert,[(self.n_name.get()),(self.n_phone.get()),(self.n_address.get()),(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_name.set('')
        self.n_phone.set('')
        self.n_address.set('')
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('Arial bold',35), bg="green3",fg="white", pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Name: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_name,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Phone: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_phone,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.crf,text = 'Address: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_address,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=3,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=4,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=5,column=1)

    

#create window and application object
root = Tk()
#root.title("Login Form")
main(root)
root.mainloop()