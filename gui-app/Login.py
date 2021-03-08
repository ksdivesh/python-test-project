from tkinter import *
from tkinter import messagebox
from Dashboard import Dashboard
from config.db import cursor, db

class Login:

    def __init__(self):
        self.window = Tk()
        self.window.title('Login')
        self.window.geometry('300x150')

        usernameLabel = Label(self.window, text='Username')
        usernameLabel.place(x=10, y=10)

        self.usernameText = Entry(self.window)
        self.usernameText.place(x=80, y=10)

        passwordLabel = Label(self.window, text='Password')
        passwordLabel.place(x=10, y=40)

        self.passwordText = Entry(self.window, show='*')
        self.passwordText.place(x=80, y=40)

        self.loginBtn = Button(self.window, text='Login', command=self.login)
        self.loginBtn.place(x=80, y=70)

        self.window.mainloop()


    def login(self):

        if(self.usernameText.get() == "" or self.passwordText.get() == ""):
            messagebox.showerror('Login Error', 'Please enter username and password')
            return None

        sql = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(self.usernameText.get(), self.passwordText.get())

        cursor.execute(sql)
        result = cursor.fetchall()

        if(len(result) == 0):
            messagebox.showerror('Wrong credentials','Wrong username or password')
            return None

        self.window.withdraw()
        dashboard = Dashboard(username= result[0]['username'],user_id= result[0]['user_id'])




