from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Label, Entry, Button
from gettersetterforbooking import makebooking
from databaseformakebooking import  all, insertee, updateTrip, deletebooking,searchbyid
import re
import Global

class welcomecustomer():
    def __init__(self):

        def desroyWelcomeCust():
            window.destroy()
            from dashboard import FIRSTPAGE
            FIRSTPAGE


        def BOOKED():
            pickup = txtpickupaddress.get()
            time = txtpickuptime.get()
            dropoff = txtdropoffaddress.get()
            cid = Global.customerAccount[0]
            result = insertee(pickupaddress=pickup,pickuptime=time,dropoffaddress=dropoff,cid = cid)
            if (result == None):
                table.delete(*table.get_children())
                trips = all(cid)
                for trip in trips:
                    table.insert(parent='', index='end', iid=trip[0], values=((trip[0], trip[1], trip[2], trip[3], trip[4])))
                    table.pack()
                print("INSERT SUCCESSFULLY")
                messagebox.showinfo("Title", "Successfully Booked")
            else:
                messagebox.showinfo("Title", " Booking Failed")
                print("Error to insert")



        def Validate():
            validate_PickUpAddress = txtpickupaddress.get()
            pickupaddressRegex = re.compile(r'^[a-zA-Z0-9 ,]+$')
            validate_PickUpTime = txtpickuptime.get()
            pickuptimeRegex = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9] (AM|PM)$')
            validate_DropOffAddress = txtdropoffaddress.get()
            dropoffaddressRegex = re.compile(r'^[a-zA-Z0-9 ,]+$')
            if re.match(pickupaddressRegex, validate_PickUpAddress)and \
                    re.match(pickuptimeRegex, validate_PickUpTime)and re.match(dropoffaddressRegex, validate_DropOffAddress):
                BOOKED()
            else:
                messagebox.showwarning("Title", "Please enter the field correctly")


        def clear():
            txtpickupaddress.delete(0,END)
            txtpickuptime.delete(0,END)
            txtdropoffaddress.delete(0,END)

        def search():
            mid = BookingID_entry.get()
            for item in table.get_children():
                table.delete(item)
            results = searchbyid(mid)
            for result in results:
                table.insert(parent='', index='end', iid=result[0],
                             values=(result[0], result[1], result[2], result[3],result[4]))


        window = Tk()
        window.geometry("700x650")
        window.resizable(False, False)
        window.title("Insert New Trip")
        window.configure(bg='Antique White')


        mainframe = Frame(window, bg="lightblue", width=700, height=110)
        mainframe.pack()
        mainframe.place(x=1, y=1)



        lbltitle = Label(window, text='Book Your Cab Here', font=("forte", 35, ), fg='black', bg="lightblue")
        lbltitle.place(x=150, y=20)

        pickupaddress = Label(window, text="Pickup Address: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        pickupaddress.place(x=155, y=130)
        txtpickupaddress = Entry(window, width=30)
        txtpickupaddress.place(x=338, y=135)

        pickuptime = Label(window, text="Pick Up Time: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        pickuptime.place(x=155, y=180)
        txtpickuptime = Entry(window, width=30)
        txtpickuptime.place(x=338, y=185)

        dropoffaddress = Label(window, text="Drop Off Address: ", font=("Helvetica", 15, "bold"), bg="Antique White")
        dropoffaddress.place(x=155, y=230)
        txtdropoffaddress = Entry(window, width=30)
        txtdropoffaddress.place(x=338, y=235)

        btnBook = Button(window, text="Book", bg="lightgreen", command=Validate)
        btnBook.place(x=230, y=280)

        btnLogOut = Button(window, text="LogOut", font=("Times New Roman", 13, "bold"),command=desroyWelcomeCust, bg="firebrick1")
        btnLogOut.place(x=430, y=600)


        btnClear = Button(window, text="Clear", bg="lightgreen",command=clear)
        btnClear.place(x=490, y=280)

        lblLogOut = Label(window, text="Click Here To LogOut:", font=("Times New Roman", 20,'bold'), fg='black', bg="AntiqueWhite")
        lblLogOut.place(x=140, y=595)

        lblDesign = Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10,'bold'), fg='black', bg="AntiqueWhite")
        lblDesign.place(x=-5, y=310)

        lblDesign2 = Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10,'bold'), fg='black', bg="AntiqueWhite")
        lblDesign2.place(x=-5, y=570)

        btnSearch = Button(window, text="Search", bg="skyblue", width=8,command=search)
        btnSearch.place(x=476, y=343)

        BookingID = Label(window, text="Booking Id: ", font=("Helvetica", 15, ), bg="AntiqueWhite")
        BookingID.place(x=180, y=340)
        BookingID_entry = Entry(window, width=30)
        BookingID_entry.place(x=290, y=345)

        cid = Global.customerAccount[0]
        trips = all(cid)


        tableFrame = Frame(window)
        tableFrame.place(x=90, y=380)

        table = ttk.Treeview((tableFrame), height=8)
        table['columns'] = (('TripId', 'PickUpAddress', 'PickUpTime', 'DropOffAddress', 'Status'))

        table.column("#0", width=0, stretch=NO)
        table.column("TripId", width=85, anchor=CENTER)
        table.column("PickUpAddress", width=130, anchor=CENTER)
        table.column("PickUpTime", width=85, anchor=CENTER)
        table.column("DropOffAddress", width=120, anchor=CENTER)
        table.column("Status", width=100, anchor=CENTER)

        table.heading('#0', text='', anchor=CENTER)
        table.heading('TripId', text='TripId', anchor=CENTER)
        table.heading('PickUpAddress', text='PickUpAddress', anchor=CENTER)
        table.heading('PickUpTime', text='PickUpTime', anchor=CENTER)
        table.heading('DropOffAddress', text='DropOffAddress', anchor=CENTER)
        table.heading('Status', text='Status', anchor=CENTER)
        for trip in trips:
            table.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3],trip[4]))
        table.pack()



        def Update():
            pickup = txtpickupaddress.get()
            dropoff = txtdropoffaddress.get()
            time = txtpickuptime.get()
            mid = table.selection()[0]
            result =  updateTrip(pickup,dropoff,time,mid)
            if result == True:
                print("Record Edit")
                messagebox.showinfo("Title", "Successfully Edited")
                table.delete(*table.get_children())
                trips = all(cid)
                for trip in trips:
                    table.insert(parent='', index='end',iid=trip[0],values=((trip[0], trip[1], trip[2], trip[3],trip[4])))
                    table.pack()
            else:
                messagebox.showinfo("Title", "Edit Failed")
                print("Error to Edit")

        def cancelBooking():
            selected_row = table.selection()[0]
            trip_id = table.item(selected_row)['values'][0]
            result = deletebooking(trip_id)
            if result:
                table.delete(selected_row)
                messagebox.showinfo("Title", "Booking cancelled successfully")
            else:
                messagebox.showinfo("Title", "Error cancelling booking")


        def selecteditems(a):
            txtpickupaddress.delete(0, END)
            txtpickuptime.delete(0, END)
            txtdropoffaddress.delete(0, END)
            selected = table.selection()
            if selected:
                selectedItem = selected[0]
                txtpickupaddress.insert(0, table.item(selectedItem)['values'][1])
                txtpickuptime.insert(0, table.item(selectedItem)['values'][2])
                txtdropoffaddress.insert(0, table.item(selectedItem)['values'][3])
        table.bind("<<TreeviewSelect>>", selecteditems)

        btnUpdateBooking = Button(window, text="Update Booking", bg="lightgreen", command=Update)
        btnUpdateBooking.place(x=385, y=280)

        btnCancelBooking = Button(window, text="Cancel Booking", bg="lightgreen",command= cancelBooking)
        btnCancelBooking.place(x=280, y=280)

        window.mainloop()











