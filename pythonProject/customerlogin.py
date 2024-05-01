from tkinter import *
from customerregister import Register
from welcomecust import welcomecustomer
from tkinter import messagebox
from databaseforcustomer import search
from tkinter import Checkbutton
import Global


# Create the CustomerLogin class for the customer login page of the Taxi booking app
class CustomerLogin:
    def __init__(self):
        # Define the function for the "Sign Up" button
        def reg():
            # Close the current window and open the customer registration page
            window.destroy()
            Register()

        # Define the function for the "Log In" button
        def SearchUser():
            # Get the input from the email and password entries
            email = email_entry.get()
            password = password_entry.get()

            # Search the database to check if the entered email and password match an existing customer account
            customer = search(email, password)
            if customer != None:
                # Save the customer account in the Global variable
                Global.customerAccount = customer
                # Show a success message and open the welcome page for the customer
                messagebox.showinfo("Customer Login Sucessful", "Welcome {}".format(email_entry.get()))
                window.destroy()
                welcomecustomer()
                window.mainloop()
            # If the entered email and password do not match any customer account, show an error message
            else:
                messagebox.showerror("Title", "Incorrect Email or Password")

        # Create the main window for the customer login page
        window = Tk()
        window.title('Taxi Login Page for customer')
        window.resizable(False, False)
        window.geometry('500x350')

        mainframe = Frame(window, bg="gray", width=500, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        mainframe = Frame(window, bg="AntiqueWhite", width=500, height=290)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        # Show/hide password function
        def show_password():
            if password_entry.cget('show') == "*":
                password_entry.config(show='')
            else:
                password_entry.config(show='*')

        # Create a label for the login page title
        lbltitle = Label(window, text="Log-In For Customer", font=("Arial Black", 20, "bold"), fg='Black', bg="grey")
        lbltitle.place(x=110, y=20)

        # Create a label for the app name
        lblAppName = Label(window, text="Taxi Booking System", font=("forte", 20,), fg='black', bg="AntiqueWhite")
        lblAppName.place(x=130, y=300)

        # Create and position a label for the email input field
        email = Label(window, text="Email: ", font=("Helvetica", 15, "bold"), bg="AntiqueWhite")
        email.place(x=80, y=100)
        # Create and position an input field for the email
        email_entry = Entry(window, width=30, )
        email_entry.place(x=200, y=105)

        # Create and position a label for the password input field
        password = Label(window, text="Password: ", font=("Helvetica", 15, "bold"), bg="AntiqueWhite")
        password.place(x=80, y=145)
        # Create and position an input field for the password
        password_entry = Entry(window, width=30, show="*")
        password_entry.place(x=200, y=150)

        # Create and position a button for logging in
        btnLogIn = Button(window, text="Log-In", bg="firebrick1", command=SearchUser)
        btnLogIn.place(x=200, y=200)

        # Create and position a button for canceling
        btnCancel = Button(window, text="Cancel", bg="firebrick1", command=exit)
        btnCancel.place(x=260, y=200)

        # Create and position a label to separate the login and sign up options
        lblSeparate = Label(window,
                           text="---------------------------------------------------------------OR------------------------------------------------------------",
                           font=("comicsansm", 10), fg='black', bg="AntiqueWhite")
        lblSeparate.place(x=-10, y=225)

        # Create and position a button for signing up as a customer
        btnForgetPassword = Button(window, text="Sign-Up As Customer", bg="firebrick1", command=reg)
        btnForgetPassword.place(x=191, y=250)

        # Create and position a checkbox for showing the password
        ck1 = Checkbutton(window, text="SHOW", bg="Antique White", font=("Helvetica", 10, "bold"),
                          command=show_password)
        ck1.place(x=400, y=148)

        # Create and position a label to separate the options from the bottom of the window
        lblSeparate = Label(window,
                           text="----------------------------------------------------------------------------------------------------------------------------------------------",
                           font=("comicsansm", 10), fg='black', bg="AntiqueWhite")
        lblSeparate.place(x=-5, y=275)

        # Start the main event loop to display the window
        window.mainloop()





