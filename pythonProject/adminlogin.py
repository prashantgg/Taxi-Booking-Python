from tkinter import *
from tkinter import messagebox
from databaseforadmin import searchee
from welcomeadmin import WelcomeAdmin

# This class creates a GUI for the Admin login page using tkinter library
class Admin():
    def __init__(self):
        # Function to validate login credentials
        def loginvalidate():
            email = username_entry.get()  #get email from email entry
            password = password_entry.get() #get password from password entry
            admin = searchee(email, password) #search for admin in the database
            if admin != None:
                messagebox.showinfo("Title", "Admin Login Sucessful")
                window.destroy()
                WelcomeAdmin()
                window.mainloop()
            else:
                messagebox.showerror("Title", "Incorrect Username or Password")

        # GUI window properties
        window = Tk()
        window.title('Taxi Login Page for admin')
        window.resizable(False, False)
        window.geometry('500x350')

        # Main frame properties
        mainframe = Frame(window, bg="gray", width=500, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        mainframe = Frame(window, bg="AntiqueWhite", width=500, height=290)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        # Function to show/hide password
        def show():
            if password_entry.cget('show') == "*":
                password_entry.config(show='')
            else:
                password_entry.config(show='*')

        # Labels and buttons for GUI
        lblTitle = Label(window, text="Log-In For Admin", font=("Arial Black", 20, "bold"),fg='black', bg='grey')
        lblTitle.place(x=110, y=20)

        lblTitle = Label(window, text="Taxi Booking System", font=("forte", 20,), fg='black', bg="AntiqueWhite")
        lblTitle.place(x=130, y=300)

        username = Label(window, text="Username: ", font=("Helvetica", 15, "bold"),bg="AntiqueWhite")
        username.place(x=80, y=115)
        username_entry = Entry(window, width=30)
        username_entry.place(x=200, y=120)

        password = Label(window, text="Password: ", font=("Helvetica", 15, "bold"),bg="AntiqueWhite")
        password.place(x=80, y=165)
        password_entry = Entry(window, width=30, show="*")
        password_entry.place(x=200, y=170)

        btnLogIn = Button(window, text="Log-In",command=loginvalidate,bg="firebrick1")
        btnLogIn.place(x=200, y=220)

        btnCancel = Button(window, text="Cancel", command=exit,bg="firebrick1")
        btnCancel.place(x=260, y=220)

        lblCollege = Label(window,
                                   text="----------------------------------------------------------------------------------------------------------------------------------------------",
                                   font=("comicsansm", 10), fg='black', bg="AntiqueWhite")
        lblCollege.place(x=-5, y=275)

        ck1 = Checkbutton(window, text="SHOW", bg="Antique White", font=("Helvetica", 10, "bold"), command=show)
        ck1.place(x=400, y=168)

        window.mainloop()




