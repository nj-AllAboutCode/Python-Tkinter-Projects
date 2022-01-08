# Python Tkinter and Sqlite3 Login Form
# Made By Namah Jain Form Youtube Channel All About Code
# Please Subscribe To Our Youtube Channel.
# https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber

# imports
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);')
db.commit()
db.close()


# main Class
class Main:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Useful variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.head = None
        self.logf = None
        self.crf = None
        # Create Widgets
        self.widgets()
        # Sets up the database
        self.db2 = None
        # Holds database information
        self.db = None
        self.db_connection()

    # Open Database connection
    def db_connection(self):
        with sqlite3.connect('quit.db') as self.db2:
            self.db = self.db2.cursor()

    # Close Database connection
    def db_close_connection(self):
        self.db.close()

    # Login Function
    def login(self):
        # Establish Connection
        # Moved to db_connection()
        # Find user If there is any take proper action
        find_user = 'SELECT * FROM user WHERE username = ? and password = ?'
        self.db.execute(find_user, [(self.username.get()), (self.password.get())])
        result = self.db.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        # Moved to db_connection()

        # Find Existing username if any take proper action
        find_user = 'SELECT username FROM user WHERE username = ?'
        self.db.execute(find_user, [(self.n_username.get())])
        if self.db.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Different One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        self.db.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        self.db2.commit()

        # Frame Packing Methods

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Login Form')
    # root.geometry('400x350+300+300')
    running = Main(root)
    root.mainloop()
    running.db_close_connection()
