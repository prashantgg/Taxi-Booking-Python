from tkinter import *
from PIL import Image, ImageTk


class FIRSTPAGE():
    def __init__(self):
        # Create the main window
        window = Tk()
        window.title('Dashboard')
        window.resizable(False, False)
        window.geometry('500x350')

        # Open the background image file and display it in the window
        tmpImage = Image.open('taxi.png')
        imgFile = ImageTk.PhotoImage(tmpImage)
        imgFile_lbl = Label(window, image=imgFile)
        imgFile_lbl.image = imgFile
        imgFile_lbl.place(x=1, y=-30)

        # Create a label for the title of the app
        lblTitle = Label(window, text="Taxi Booking App", font=("forte", 20,), fg='black', bg="grey")
        lblTitle.place(x=130, y=0)

        # Define functions to be called when the user clicks the "Customer", "Driver", or "Admin" buttons
        def destroycustomer():
            window.destroy()
            from customerlogin import CustomerLogin
            CustomerLogin.__init__(self)

        def destroydriver():
            window.destroy()
            from driverlogin import Driver
            Driver.__init__(self)

        def destroyadmin():
            window.destroy()
            from adminlogin import Admin
            Admin.__init__(self)

        # Create a label to display a quote on the app
        lblQuote = Label(window,
                         text="-Book a ride with just a simple tap\n\n-Ride with best and high-rated drivers\n\n-Licensed and fully insured drivers",
                         font=("Time New Roman", 10, "bold"), fg='firebrick1', bg="black")
        lblQuote.place(x=120, y=50)

        # Create a label for the "Log-In As:" text
        lblLogInAs = Label(window, text="Log-In As:", font=("Arial Black", 12, "bold"), fg='black')
        lblLogInAs.place(x=10, y=300)

        # Create buttons for the user to log in as a customer, driver, or admin
        btnCustomer = Button(window, text="Customer", command=destroycustomer, bg="Antique White")
        btnCustomer.place(x=130, y=300)

        btnDriver = Button(window, text="Driver", command=destroydriver, bg="firebrick1")
        btnDriver.place(x=260, y=300)

        btnAdmin = Button(window, text="Admin", command=destroyadmin, bg="yellow")
        btnAdmin.place(x=380, y=300)

        # Start the main event loop of the app
        window.mainloop()


# Create an instance of the FIRSTPAGE class to display the app
FIRSTPAGE()
