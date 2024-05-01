# Importing necessary libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Label, Entry, Button
from databaseformakebooking import  all2, updatebookingstatus,get_driver_names
import mysql.connector


 # Class for the Assign Driver feature
class AssignDriver():
    # Initializing the class
    def __init__(self):
        def clear():
            txttripnumber.delete(0,END)
            txtpickupaddress.delete(0,END)
            txtpickuptime.delete(0,END)
            txtdropoffaddress.delete(0,END)
            driver_combobox.delete(0,END)

        window = Tk()
        window.geometry("700x650")
        window.resizable(False, False)
        window.title("Insert New Trip")
        window.configure(bg='Antique White')

        # Function to go back to the Welcome Admin page
        def destroyassigndriver():
            window.destroy()
            from welcomeadmin import WelcomeAdmin
            WelcomeAdmin.__init__(self)

        frame = Frame(window)
        frame.configure(bg="lightgreen")
        frame.place(x=130, y=95)
        frame.configure(width=420, height=250)

        mainframe = Frame(window, bg="lightblue", width=700, height=85)
        mainframe.pack()
        mainframe.place(x=1, y=1)



        lbltitle = Label(window, text='Assign Driver', font=("forte", 40, ), fg='black', bg="lightblue")
        lbltitle.place(x=200, y=5)

        tripnumber = Label(window, text="Trip Number: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
        tripnumber.place(x=155, y=95)
        txttripnumber = Entry(window, width=3)
        txttripnumber.place(x=338, y=100)
        txttripnumber.place_forget()
        txttripnumber.place(x=338, y=100)

        pickupaddress = Label(window, text="Pickup Address: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
        pickupaddress.place(x=155, y=135)
        txtpickupaddress = Entry(window, width=30)
        txtpickupaddress.place(x=338, y=140)

        pickuptime = Label(window, text="Pick Up Time: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
        pickuptime.place(x=155, y=175)
        txtpickuptime = Entry(window, width=30)
        txtpickuptime.place(x=338, y=180)

        dropoffaddress = Label(window, text="Drop Off Address: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
        dropoffaddress.place(x=155, y=215)
        txtdropoffaddress = Entry(window, width=30)
        txtdropoffaddress.place(x=338, y=220)

        btnBack = Button(window, text="Back", font=("Times New Roman", 13, "bold"),width=7, bg="firebrick1",command=destroyassigndriver)
        btnBack.place(x=440, y=596)

        btnClear = Button(window, text="Clear", bg="yellow",command=clear)
        btnClear.place(x=490, y=295)

        lblBack = Label(window, text="Click Here To Go Back:", font=("Times New Roman", 20,'bold'), fg='black', bg="AntiqueWhite")
        lblBack.place(x=140, y=595)

        lblDesign = Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10,'bold'), fg='black', bg="AntiqueWhite")
        lblDesign.place(x=-5, y=350)

        lblDesign2 = Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10,'bold'), fg='black', bg="AntiqueWhite")
        lblDesign2.place(x=-5, y=570)

        driver = Label(window, text="Driver: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
        driver.place(x=155, y=255)
        driver_names = get_driver_names()
        driver_combobox = ttk.Combobox(window, values=driver_names)
        driver_combobox.place(x=338, y=255)



        def assign():
            selected_driver = driver_combobox.get()
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='level4d'
            )
            cursor = connection.cursor()
            query = "SELECT name, licenseplate FROM driver WHERE name = %s"
            cursor.execute(query, (selected_driver,))
            result = cursor.fetchone()
            if result:
                Name, Licenseplate = result
                update_query = "UPDATE makebooking SET status='Booked', DriverName=%s, LicensePlate=%s WHERE mid=%s"
                cursor.execute(update_query, (Name, Licenseplate, txttripnumber.get()))
                connection.commit()
                messagebox.showinfo("Title", "Driver Assigned Successfully")
                table.delete(*table.get_children())
                trips = all2()
                for trip in trips:
                    table.insert(parent='', index='end', iid=trip[0],
                                 values=((trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6],trip[7])))
                    table.pack()
            else:
                print("Driver not found in the database")

        trips = all2()

        tableFrame = Frame(window)
        tableFrame.place(x=15, y=380)

        table = ttk.Treeview((tableFrame), height=8)
        table['columns'] = (
        ('TripId', 'PickUpAddress', 'PickUpTime', 'DropOffAddress', 'Status', 'DriverName', 'LicensePlate','CustomerID'))

        table.column("#0", width=0, stretch=NO)
        table.column("TripId", width=50, anchor=CENTER)
        table.column("PickUpAddress", width=120, anchor=CENTER)
        table.column("PickUpTime", width=83, anchor=CENTER)
        table.column("DropOffAddress", width=120, anchor=CENTER)
        table.column("Status", width=70, anchor=CENTER)
        table.column("DriverName", width=100, anchor=CENTER)
        table.column("LicensePlate", width=73, anchor=CENTER)
        table.column("CustomerID", width=50, anchor=CENTER)

        table.heading('#0', text='', anchor=CENTER)
        table.heading('TripId', text='TID', anchor=CENTER)
        table.heading('PickUpAddress', text='PickUpAddress', anchor=CENTER)
        table.heading('PickUpTime', text='PickUpTime', anchor=CENTER)
        table.heading('DropOffAddress', text='DropOffAddress', anchor=CENTER)
        table.heading('Status', text='Status', anchor=CENTER)
        table.heading('DriverName', text='DriverName', anchor=CENTER)
        table.heading('LicensePlate', text='LicensePlate', anchor=CENTER)
        table.heading('CustomerID', text='CID', anchor=CENTER)
        for trip in trips:
            if len(trip) < 6:
                continue
            table.insert(parent='', index='end', iid=trip[0],
                         values=(trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6],trip[7]))

        table.pack()


        def cancelBooking():
            selected_row = table.selection()[0]
            trip_id = table.item(selected_row)['values'][0]
            result = updatebookingstatus(trip_id)
            if result:
                table.item(selected_row)['values'][3] = "cancelled"
                messagebox.showinfo("Title", "Booking cancelled successfully")
                table.delete(*table.get_children())
                trips = all2()
                for trip in trips:
                    table.insert(parent='', index='end', iid=trip[0], values=((trip[0], trip[1], trip[2], trip[3], trip[4],trip[5],trip[6],trip[7])))
                    table.pack()
            else:
                messagebox.showinfo("Title", "Error cancelling booking")

        def selecteditems(a):
            txttripnumber.delete(0, END)
            txtpickupaddress.delete(0, END)
            txtpickuptime.delete(0, END)
            txtdropoffaddress.delete(0, END)
            selected = table.selection()
            if selected:
                selectedItem = selected[0]
                values = table.item(selectedItem)['values']
                if values:
                    txttripnumber.insert(0, values[0])
                    txtpickupaddress.insert(0, values[1])
                    txtpickuptime.insert(0, values[2])
                    txtdropoffaddress.insert(0, values[3])

        table.bind("<<TreeviewSelect>>", selecteditems)

        btnAssignDriver = Button(window, text="Assign Driver", bg="yellow",command=assign)
        btnAssignDriver.place(x=335, y=295)

        btnCancelBooking = Button(window, text="Cancel", bg="yellow",command= cancelBooking)
        btnCancelBooking.place(x=200,y=295)

        window.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# from tkinter import Tk, Label, Entry, Button
# from databaseformakebooking import  all2, updatebookingstatus,get_driver_names
# import mysql.connector
#
# # Class for the Assign Driver feature
# class AssignDriver():
#     # Initializing the class
#     def __init__(self):
#         # Function to clear all the fields
#         def clear():
#             txttripnumber.delete(0,END)
#             txtpickupaddress.delete(0,END)
#             txtpickuptime.delete(0,END)
#             txtdropoffaddress.delete(0,END)
#             driver_combobox.delete(0,END)
#
#         # Creating the main window
#         window = Tk()
#         window.geometry("700x650")
#         window.resizable(False, False)
#         window.title("Insert New Trip")
#         window.configure(bg='Antique White')
#
#         # Function to go back to the Welcome Admin page
#         def destroyassigndriver():
#             window.destroy()
#             from welcomeadmin import WelcomeAdmin
#             WelcomeAdmin.__init__(self)
#
#         # Creating a frame for the widgets
#         frame = Frame(window)
#         frame.configure(bg="lightgreen")
#         frame.place(x=130, y=95)
#         frame.configure(width=420, height=250)
#
#         # Creating a main frame for the title
#         mainframe = Frame(window, bg="lightblue", width=700, height=85)
#         mainframe.pack()
#         mainframe.place(x=1, y=1)
#
#         # Title label
#         lbltitle = Label(window, text='Assign Driver', font=("forte", 40, ), fg='black', bg="lightblue")
#         lbltitle.place(x=200, y=5)
#
#         # Trip number label and entry
#         tripnumber = Label(window, text="Trip Number: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
#         tripnumber.place(x=155, y=95)
#         txttripnumber = Entry(window, width=3)
#         txttripnumber.place(x=338, y=100)
#         txttripnumber.place_forget()
#         txttripnumber.place(x=338, y=100)
#
#         # Pickup address label and entry
#         pickupaddress = Label(window, text="Pickup Address: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
#         pickupaddress.place(x=155, y=135)
#         txtpickupaddress = Entry(window, width=30)
#         txtpickupaddress.place(x=338, y=140)
#
#
#         # Creating a label for the pick-up time
#         pickuptime = Label(window, text="Pick Up Time: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
#         # Placing the label on the window
#         pickuptime.place(x=155, y=175)
#         # Creating an entry field for the pick-up time
#         txtpickuptime = Entry(window, width=30)
#         # Placing the entry field on the window
#         txtpickuptime.place(x=338, y=180)
#
#         # Creating a label for the drop-off address
#         dropoffaddress = Label(window, text="Drop Off Address: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
#         # Placing the label on the window
#         dropoffaddress.place(x=155, y=215)
#         # Creating an entry field for the drop-off address
#         txtdropoffaddress = Entry(window, width=30)
#         # Placing the entry field on the window
#         txtdropoffaddress.place(x=338, y=220)
#
#         # Creating a button for going back to the previous window
#         btnBack = Button(window, text="Back", font=("Times New Roman", 13, "bold"), width=7, bg="firebrick1",
#                          command=destroyassigndriver)
#         # Placing the button on the window
#         btnBack.place(x=440, y=596)
#
#         # Creating a button for clearing the input fields
#         btnClear = Button(window, text="Clear", bg="yellow", command=clear)
#         # Placing the button on the window
#         btnClear.place(x=490, y=295)
#
#         # Creating a label for the "Click Here To Go Back:" text
#         lblBack = Label(window, text="Click Here To Go Back:", font=("Times New Roman", 20, 'bold'), fg='black',
#                         bg="AntiqueWhite")
#         # Placing the label on the window
#         lblBack.place(x=140, y=595)
#
#         # Creating a label for the design line
#         lblDesign = Label(window,
#                           text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
#                           font=("comicsansm", 10, 'bold'), fg='black', bg="AntiqueWhite")
#         # Placing the label on the window
#         lblDesign.place(x=-5, y=350)
#
#         # Creating another label for the design line
#         lblDesign2 = Label(window,
#                            text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
#                            font=("comicsansm", 10, 'bold'), fg='black', bg="AntiqueWhite")
#         # Placing the label on the window
#         lblDesign2.place(x=-5, y=570)
#
#         # Creating a label for the driver
#         driver = Label(window, text="Driver: ", font=("Helvetica", 15, "bold"), bg="lightgreen")
#         # Placing the label on the window
#         driver.place(x=155, y=255)
#
#         # Getting a list of driver names from the database
#         driver_names = get_driver_names()
#         # Creating a combobox for selecting a driver
#         driver_combobox = ttk.Combobox(window, values=driver_names)
#         # place the combobox on the window
#         driver_combobox.place(x=338, y=255)
#
#         # function to assign a driver to a trip
#         def assign():
#             # get the selected driver from the combobox
#             selected_driver = driver_combobox.get()
#             # connect to the database
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 port='3306',
#                 user='root',
#                 password='',
#                 database='level4d'
#             )
#             cursor = connection.cursor()
#             # retrieve the driver's name and license plate from the database
#             query = "SELECT name, licenseplate FROM driver WHERE name = %s"
#             cursor.execute(query, (selected_driver,))
#             result = cursor.fetchone()
#             # check if the driver was found in the database
#             if result:
#                 Name, Licenseplate = result
#                 # update the trip's status, driver's name, and license plate in the database
#                 update_query = "UPDATE makebooking SET status='Booked', DriverName=%s, LicensePlate=%s WHERE mid=%s"
#                 cursor.execute(update_query, (Name, Licenseplate, txttripnumber.get()))
#                 connection.commit()
#                 # show a message box indicating the driver was assigned successfully
#                 messagebox.showinfo("Title", "Driver Assigned Successfully")
#                 # update the table to reflect the changes in the database
#                 table.delete(*table.get_children())
#                 trips = all2()
#                 for trip in trips:
#                     table.insert(parent='', index='end', iid=trip[0],
#                                  values=((trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6], trip[7])))
#                     table.pack()
#             else:
#                 print("Driver not found in the database")
#
#         # retrieve all trips from the database
#         trips = all2()
#
#         # create a frame for the table
#         tableFrame = Frame(window)
#         tableFrame.place(x=15, y=380)
#
#         # create the table
#         table = ttk.Treeview((tableFrame), height=8)
#         table['columns'] = (
#             ('TripId', 'PickUpAddress', 'PickUpTime', 'DropOffAddress', 'Status', 'DriverName', 'LicensePlate',
#              'CustomerID'))
#
#         # set the width of each column
#         table.column("#0", width=0, stretch=NO)
#         table.column("TripId", width=50, anchor=CENTER)
#         table.column("PickUpAddress", width=120, anchor=CENTER)
#         table.column("PickUpTime", width=83, anchor=CENTER)
#         table.column("DropOffAddress", width=120, anchor=CENTER)
#         table.column("Status", width=70, anchor=CENTER)
#         table.column("DriverName", width=100, anchor=CENTER)
#         table.column("LicensePlate", width=73, anchor=CENTER)
#         table.column("CustomerID", width=50, anchor=CENTER)
#
#         # set the headings for each column
#         table.heading('#0', text='', anchor=CENTER)
#         table.heading('TripId', text='TID', anchor=CENTER)
#         table.heading('PickUpAddress', text='PickUpAddress', anchor=CENTER)
#         table.heading('PickUpTime', text='PickUpTime', anchor=CENTER)
#         table.heading('DropOffAddress', text='DropOffAddress', anchor=CENTER)
#         table.heading('Status', text='Status', anchor=CENTER)
#         table.heading('DriverName', text='DriverName', anchor=CENTER)
#         table.heading('LicensePlate', text='LicensePlate', anchor=CENTER)
#         table.heading('CustomerID', text='CID', anchor=CENTER)
#
#         # insert the retrieved trips into the table
#         for trip in trips:
#             if len(trip) < 6:
#                 continue
#             table.insert(parent='', index='end', iid=trip[0],
#                          values=(trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6], trip[7]))
#
#         # display the table
#         table.pack()
#
#         # function to cancel a booking
#         def cancelBooking():
#             # get the selected row
#             selected_row = table.selection()[0]
#             # get the trip id from the selected row
#             trip_id = table.item(selected_row)['values'][0]
#             # update the trip's status in the database
#             result = updatebookingstatus(trip_id)
#             if result:
#                 # update the table to reflect the changes in the database
#                 table.item(selected_row)['values'][3] = "cancelled"
#                 # show a message box indicating the booking was cancelled successfully
#                 messagebox.showinfo("Title", "Booking cancelled successfully")
#                 # Delete any existing entries in the table
#                 table.delete(*table.get_children())
#
#                 # Get all trips and add them to the table
#                 trips = all2()
#                 for trip in trips:
#                     table.insert(parent='', index='end', iid=trip[0],
#                                  values=((trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6], trip[7])))
#                     table.pack()
#                 else:
#                     # Show an error message if there is a problem cancelling the booking
#                     messagebox.showinfo("Title", "Error cancelling booking")
#
#                 # Function to handle when an item in the table is selected
#                 def selecteditems(a):
#                     # Clear the input fields
#                     txttripnumber.delete(0, END)
#                     txtpickupaddress.delete(0, END)
#                     txtpickuptime.delete(0, END)
#                     txtdropoffaddress.delete(0, END)
#                     # Get the selected item
#                     selected = table.selection()
#                     if selected:
#                         selectedItem = selected[0]
#                         values = table.item(selectedItem)['values']
#                         if values:
#                             # Insert the values of the selected item into the input fields
#                             txttripnumber.insert(0, values[0])
#                             txtpickupaddress.insert(0, values[1])
#                             txtpickuptime.insert(0, values[2])
#                             txtdropoffaddress.insert(0, values[3])
#
#                 # Bind the selecteditems function to the "TreeviewSelect" event of the table
#                 table.bind("<<TreeviewSelect>>", selecteditems)
#
#                 # Create buttons for assigning a driver and cancelling a booking
#                 btnAssignDriver = Button(window, text="Assign Driver", bg="yellow", command=assign)
#                 btnAssignDriver.place(x=335, y=295)
#                 btnCancelBooking = Button(window, text="Cancel", bg="yellow", command=cancelBooking)
#                 btnCancelBooking.place(x=200, y=295)
#
#                 # Start the main loop of the application
#                 window.mainloop()












