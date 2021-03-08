from tkinter import *

class Dashboard:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.dashboardWindow = Tk()
        self.dashboardWindow.title("Cafe Dashboard")
        self.dashboardWindow.geometry('500x500')

        label = Label(self.dashboardWindow, text='Dashboard', font=('Arial', 20))
        label.place(x=50, y=0)

        userNameLabel = Label(self.dashboardWindow, text='{} {}'.format(self.username, self.user_id))
        userNameLabel.place(x=40, y=50)

        self.dashboardWindow.mainloop()



