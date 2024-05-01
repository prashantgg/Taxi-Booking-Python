from tkinter import *
from tkinter  import messagebox
from databasefordriver import searche
from welcomedriver import WelcomeDriver
import Global

class Driver():
    def __init__(self):
        def login():
            email = email_entry.get()
            password =password_entry.get()
            driver = searche(email,password)
            if driver != None:
                Global.driverlogin = driver
                messagebox.showinfo("Driver Login Sucessful","Welcome {}".format(email_entry.get()))
                window.destroy()
                WelcomeDriver()
                window.mainloop()

            else:
                messagebox.showerror("Title", "Incorrect Username or Password")


        window = Tk()
        window.title('Taxi Login Page for driver')
        window.resizable(False, False)
        window.geometry('500x350')

        mainframe = Frame(window, bg="gray", width=500, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        mainframe = Frame(window, bg="AntiqueWhite", width=500, height=290)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        def yes():
            if password_entry.cget('show') == "*":
                password_entry.config(show='')
            else:
                password_entry.config(show='*')


        lblCollege = Label(window, text="Log-In For Driver", font=("Arial Black", 20, "bold"),fg='black',bg="grey")
        lblCollege.place(x=110, y=20)

        lblCollege = Label(window, text="Taxi Booking System", font=("forte", 20,),fg='black',bg="AntiqueWhite")
        lblCollege.place(x=130, y=300)



        #Add Entry - text box - single line
        email = Label(window, text="Email: ", font=("Helvetica", 15, "bold"),bg="AntiqueWhite")
        email.place(x=80, y=100)
        email_entry = Entry(window, width=30)
        email_entry.place(x=200, y=105)

        def dest():
            window.destroy()
            from driverregister import DriverRegister
            DriverRegister.__init__(self)



        #Add password box
        password = Label(window, text="Password: ", font=("Helvetica", 15, "bold"),bg="AntiqueWhite")
        password.place(x=80, y=145)
        password_entry = Entry(window, width=30, show="*")
        password_entry.place(x=200, y=150)


        #Button
        btnLogIn = Button(window, text="Log-In",command=login, bg="firebrick1")
        btnLogIn.place(x=200, y=200)

        btnCancel = Button(window, text="Cancel", command=exit, bg="firebrick1")
        btnCancel.place(x=260, y=200)

        btnForgetPassword = Button(window, text="Sign-Up As Driver", command=dest, bg="firebrick1")
        btnForgetPassword.place(x=200, y=250)

        lblCollege = Label(window,text="---------------------------------------------------------------OR------------------------------------------------------------",font=("comicsansm", 10), fg='black', bg="AntiqueWhite")
        lblCollege.place(x=-10, y=225)

        lblCollege = Label(window,text="----------------------------------------------------------------------------------------------------------------------------------------------",font=("comicsansm", 10), fg='black', bg="AntiqueWhite")
        lblCollege.place(x=-5, y=275)

        ck1 = Checkbutton(window, text="SHOW", bg="Antique White", font=("Helvetica", 10, "bold"), command=yes)
        ck1.place(x=400, y=148)

        window.mainloop()