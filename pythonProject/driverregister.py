from tkinter import *
from tkinter import ttk, messagebox
from databasefordriver import insert
from tkinter import Checkbutton
from gettersetterfordriver import driver
import re


class DriverRegister():
    def __init__(self):

        def doneregister():
            name = txtname.get()
            address = txtaddress.get()
            email = txtemail.get()
            licenseplate = txtlicenseplate.get()
            password = txtpassword.get()


            dr = driver(did=' ',name=name, address=address, email=email, licenseplate=licenseplate, password=password)
            result = insert(dr)
            if(result == None):
                print ("INSERT SUCCESSFULLY")
                messagebox.showinfo("Title", "User registered")
            else:
                messagebox.showinfo("Title", "Invalid id")
                print ("Error to insert")



        window = Tk()
        window.title('Taxi Registration Page')
        window.resizable(False, False)
        window.geometry('500x350')

        mainframe = Frame(window, bg="gray", width=500, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=-30)

        mainframe = Frame(window, bg="AntiqueWhite", width=500, height=500)
        mainframe.pack()
        mainframe.place(x=0, y=60)


        def bka():
            if txtpassword.cget('show') == "*":
                txtpassword.config(show='')
            else:
                txtpassword.config(show='*')

        #label
        lblCollege = Label(window, text="Create New Account", font=("Arial Black", 20, "bold"),fg='black',bg="grey")
        lblCollege.place(x=110, y=5)




        #Add Entry - text box - single line
        name = Label(window, text="Name: ", font=("Helvetica", 15, "bold"),bg="Antique White")
        name.place(x=80, y=70)
        txtname = Entry(window, width=30)
        txtname.place(x=230, y=75)

        address = Label(window, text="Address: ", font=("Helvetica", 15, "bold"),bg="Antique White")
        address.place(x=80, y=105)
        txtaddress = Entry(window, width=30)
        txtaddress.place(x=230, y=110)

        email = Label(window, text="Email: ", font=("Helvetica", 15, "bold"),bg="Antique White")
        email.place(x=80, y=143)
        txtemail = Entry(window, width=30)
        txtemail.place(x=230, y=148)

        license = Label(window, text="License Plate: ", font=("Helvetica", 15, "bold"),bg="Antique White")
        license.place(x=80, y=180)
        txtlicenseplate = Entry(window, width=30)
        txtlicenseplate.place(x=230, y=185)


        # #Add password box
        password = Label(window, text="Password: ", font=("Helvetica", 15, "bold"),bg="Antique White")
        password.place(x=80, y=220)
        txtpassword = Entry(window, width=30, show="*")
        txtpassword.place(x=230, y=225)

        def Val():
            validate_Address = txtaddress.get()
            addressRegex = re.compile(r'^[a-zA-Z0-9 ,]+$')
            validate_Name=txtname.get()
            nameRegex = re.compile(r'^[a-zA-Z0-9 ]+$')
            validate_Email = txtemail.get()
            emailRegex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            validate_password = txtpassword.get()
            passwordRegex = re.compile("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")
            validate_licese = txtlicenseplate.get()
            licenseRegex = re.compile('[0-9]{4}$')

            if re.match(addressRegex, validate_Address)and re.match(nameRegex, validate_Name)and \
                    re.match(emailRegex, validate_Email)and re.match(passwordRegex, validate_password)and \
                    re.match(licenseRegex, validate_licese):
                doneregister()
            else:
                messagebox.showwarning("Title", "Please enter the field correctly")



        def drive():
            window.destroy()
            from driverlogin import Driver
            Driver.__init__(self)



        #Button
        btnRegister = Button(window, text="Register", command=Val,bg="firebrick1")
        btnRegister.place(x=230, y=255)


        btnRegister = Button(window, text="Back", bg="firebrick1",command=drive)
        btnRegister.place(x=310, y=255)


        lblCollege = Label(window, text="Taxi Booking System", font=("forte", 20,),fg='black',bg="AntiqueWhite")
        lblCollege.place(x=130, y=300)

        lblCollege = Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------------",bg="Antique White")
        lblCollege.place(x=-5, y=280)

        ck1 = Checkbutton(window, text="SHOW", bg="Antique White", font=("Helvetica", 10, "bold"), command=bka)
        ck1.place(x=420, y=221)

        window.mainloop()


