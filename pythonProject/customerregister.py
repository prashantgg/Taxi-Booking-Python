from tkinter import *
from databaseforcustomer import insert
from tkinter import messagebox
from tkinter import Checkbutton
import re
from gettersetterforcustomer import customer1
class Register():
    def __init__(self):

        # Function to save the registration information
        def saveregister():
            # Get the values from the input fields
            name = txtname.get()
            address = txtaddress.get()
            email = txtemail.get()
            password = txtpassword.get()
            mobileno= txttelephone.get()
            creditcard=txtcreditcard.get()
            # Create a customer1 object with the input values
            cu= customer1(cid=' ',name=name,address=address,email=email,password=password,mobileno=mobileno,creditcard=creditcard)
            # Insert the customer object into the database
            result = insert(cu)
            if(result == None):
                # Show a message if the insertion is successful
                print ("INSERT SUCCESSFULLY")
                messagebox.showinfo("Title", "User registered")
            else:
                # Show a message if the insertion is not successful
                messagebox.showinfo("Title", "Invalid id")
                print ("Error to insert")


        # Create the main window for the application
        window = Tk()
        window.title('Taxi Registration Page')
        window.resizable(False, False)
        window.geometry('500x350')

        # Create a frame for the top of the window
        mainframe = Frame(window, bg="gray", width=500, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=-30)

        # Create a frame for the middle of the window
        mainframe = Frame(window, bg="AntiqueWhite", width=500, height=500)
        mainframe.pack()
        mainframe.place(x=0, y=60)

        # Function to toggle the visibility of the password input field
        def ShowPass():
            if txtpassword.cget('show') == "*":
                txtpassword.config(show='')
            else:
                txtpassword.config(show='*')

        # Create a label for the top of the window
        lblCollege = Label(window, text="Create New Account", font=("Arial Black", 20, "bold"), fg='black', bg="grey")
        lblCollege.place(x=110, y=10)

        # Create labels and input fields for name, address, email, password, mobile number and credit card
        name = Label(window, text="Name: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        name.place(x=80, y=65)
        txtname = Entry(window, width=30)
        txtname.place(x=230, y=70)

        address = Label(window, text="Address: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        address.place(x=80, y=95)
        txtaddress = Entry(window, width=30)
        txtaddress.place(x=230, y=100)

        email = Label(window, text="Email: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        email.place(x=80, y=125)
        txtemail = Entry(window, width=30)
        txtemail.place(x=230, y=130)

        password = Label(window, text="Password: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        password.place(x=80, y=155)
        txtpassword = Entry(window, width=30, show="*")
        txtpassword.place(x=230, y=160)

        telephone = Label(window, text="Mobile No: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        telephone.place(x=80, y=185)
        txttelephone = Entry(window, width=30)
        txttelephone.place(x=230, y=190)

        creditcard = Label(window, text="Credit Card: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        creditcard.place(x=80, y=215)
        txtcreditcard = Entry(window, width=30)
        txtcreditcard.place(x=230, y=220)

        def Validate():
            # Use regular expressions to check the validity of input fields
            validate_Address = txtaddress.get()
            addressRegex = re.compile(r'^[a-zA-Z0-9 ,]+$')
            validate_Name=txtname.get()
            nameRegex = re.compile(r'^[a-zA-Z0-9 ]+$')
            validate_Email = txtemail.get()
            emailRegex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            validate_Mobile = txttelephone.get()
            mobileRegex = re.compile(r'^9\d{9}$')
            validate_creditcard = txtcreditcard.get()
            creditcardRegex = re.compile(r'^4\d{11}$')
            validate_password = txtpassword.get()
            passwordRegex = re.compile("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")

            # Check if all input fields match the regular expressions
            if re.match(addressRegex, validate_Address)and re.match(nameRegex, validate_Name)and \
            re.match(emailRegex, validate_Email)and re.match(mobileRegex, validate_Mobile)and \
            re.match(creditcardRegex, validate_creditcard)and re.match(passwordRegex, validate_password):
                saveregister()
            else:
                messagebox.showwarning("Title", "Please enter the field correctly")

        # Function to open the login page and close the registration page
        def dashboard():
            window.destroy()
            from customerlogin import CustomerLogin
            CustomerLogin.__init__(self)

        # Create a register button that runs the validate function
        btnRegister = Button(window, text="Register", command=Validate,bg="firebrick1")
        btnRegister.place(x=230, y=260)

        # Create a back button that opens the login page
        btnRegister = Button(window, text="Back", command=dashboard, bg="firebrick1")
        btnRegister.place(x=310, y=260)

        # Create additional labels for the bottom of the window
        lblCollege = Label(window, text="Taxi Booking System", font=("forte", 20,),fg='black',bg="AntiqueWhite")
        lblCollege.place(x=130, y=300)

        lblCollege = Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------------",bg="Antique White")
        lblCollege.place(x=-5, y=285)

        # Create a checkbox to toggle password visibility
        ck1 = Checkbutton(window, text="SHOW",bg="Antique White", font=("Helvetica", 10, "bold"),command=ShowPass)
        ck1.place(x=420, y=158)

        window.mainloop()








