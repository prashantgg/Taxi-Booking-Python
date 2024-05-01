from tkinter import *


class WelcomeAdmin():
    def __init__(self):
        # Function to close the current window and open the AssignDriver window
        def destroy1():
            window.destroy()
            from assigndriver import AssignDriver
            AssignDriver.__init__(self)

        # Function to close the current window and open the ViewCustomer window
        def destroy2():
            window.destroy()
            from viewcustomer import ViewCustomer
            ViewCustomer.__init__(self)

        # Function to close the current window and open the ViewDriver window
        def destroy3():
            window.destroy()
            from viewdriver import ViewDriver
            ViewDriver.__init__(self)

        # Function to close the current window and open the Dashboard window
        def dashboard():
            window.destroy()
            from dashboard import FIRSTPAGE
            FIRSTPAGE.__init__(self)

        # Create the main window
        window = Tk()
        window.title('Welcome Customer')
        window.resizable(True, True)
        window.geometry('500x350')

        # Create a frame for the top portion of the window
        mainframe = Frame(window, bg="gray", width=500, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        # Create a frame for the bottom portion of the window
        mainframe = Frame(window, bg="AntiqueWhite", width=500, height=290)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        # Create a label for the title of the window
        lblCollege = Label(window, text="Wecome To Taxi Booking App", font=("forte", 20, "bold"), fg='firebrick1',
                           bg="black")
        lblCollege.place(x=80, y=30)

        lblCollege = Label(window, text="Your Very Own Taxi Company", font=("Times New Roman", 16), fg='black',
                           bg="Yellow")
        lblCollege.place(x=120, y=95)

        # Create a label for the "Assign Driver" button
        lblCollege = Label(window, text="Click Here To Assign Driver :", font=("Times New Roman", 15), fg='black',
                           bg="Antique White")
        lblCollege.place(x=30, y=135)

        lblCollege = Label(window, text="Taxi Booking System", font=("forte", 20,), fg='black', bg="AntiqueWhite")
        lblCollege.place(x=130, y=300)

        lblCollege = Label(window,
                           text="----------------------------------------------------------------------------------------------------------------------------------------------",
                           font=("comicsansm", 10), fg='blue', bg="AntiqueWhite")
        lblCollege.place(x=-5, y=275)

        # Create a label for the "View Customer" button
        lblCollege = Label(window, text="Click Here To View Customer :", font=("Times New Roman", 15), fg='black',
                           bg="Antique White")
        lblCollege.place(x=30, y=175)

        # Create a label for the "View Driver" button

        lblCollege = Label(window, text="Click Here To View Driver :", font=("Times New Roman", 15), fg='black',
                           bg="Antique White")
        lblCollege.place(x=30, y=215)

        # Create "Assign Driver" button and link it to the destroy1 function
        btnLogIn = Button(window, text="Assign Driver", font=("Times New Roman", 10, "bold"), bg="lightblue",
                          command=destroy1)
        btnLogIn.place(x=305, y=135)

        # Create "View Customer" button and link it to the destroy2 function
        btnLogIn = Button(window, text="View Customer", font=("Times New Roman", 10, "bold"), bg="lightblue",
                          command=destroy2)
        btnLogIn.place(x=305, y=175)

        # Create "View Driver" button and link it to the destroy3 function
        btnLogIn = Button(window, text="View Driver", font=("Times New Roman", 10, "bold"), bg="lightblue",
                          command=destroy3)
        btnLogIn.place(x=305, y=215)

        # Create "LogOut" button and link it to the dashboard function
        btnLogIn = Button(window, text="LogOut", font=("Times New Roman", 13, "bold"), bg="lightgreen", command=dashboard)
        btnLogIn.place(x=195, y=248)

        # Start the main event loop
        window.mainloop()
