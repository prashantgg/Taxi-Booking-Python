from  tkinter import *
from  tkinter import ttk,messagebox
import Global
from databaseformakebooking import all2,all3
import mysql.connector

class WelcomeDriver():
    def __init__(self):

        window = Tk()
        window.title('Welcome Driver')
        window.resizable(False,False)
        window.geometry('800x460')

        mainframe = Frame(window, bg="gray", width=800, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        mainframe = Frame(window, bg="AntiqueWhite", width=800, height=420)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        frame = Frame(window)
        frame.configure(bg="light blue")
        frame.place(x=40, y=150)
        frame.configure(width=90, height=185)

        frame = Frame(window)
        frame.configure(bg="light blue")
        frame.place(x=660, y=150)
        frame.configure(width=90, height=185)

        def logout():
            window.destroy()
            from dashboard import FIRSTPAGE
            FIRSTPAGE.__init__(self)

        btnCompleted = Button(window, text="Completed", bg="lightgreen")
        btnCompleted.place(x=670, y=160)

        lblTitle = Label(window, text="Accept Ride", font=("Helvetica", 35,"bold"), fg='black', bg="grey")
        lblTitle.place(x=265, y=10)

        lblTaxi = Label(window, text="Taxi Booking System", font=("forte", 30), fg='black', bg="AntiqueWhite")
        lblTaxi.place(x=200, y=390)


        btnLogout = Button(window, text="LogOut", bg="firebrick1", width=10,command=logout)
        btnLogout.place(x=350, y=345)

        def change_status_to_completed(trip_id):
            connection = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='level4d'

            )
            cursor = connection.cursor()
            cursor.execute("UPDATE makebooking SET status='Completed' WHERE mid=%s", (trip_id,))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Trip Completed", f"Trip {trip_id} has been completed")
            table.delete(*table.get_children())
            driv = all3()
            for driv in driv:
                    table.insert(parent='', index='end', iid=driv[0],
                                 values=(driv[0], driv[1], driv[2], driv[3], driv[4]))
            table.pack()

        btnCompleted = Button(window, text="Completed", bg="lightgreen",
                              command=lambda: change_status_to_completed(tripnumber_entry.get()))
        btnCompleted.place(x=670, y=160)



        tripnumber = Label(window, text="TID: ", font=("Helvetica", 8,'bold' ), bg="AntiqueWhite")
        tripnumber.place(x=40, y=95)
        tripnumber_entry = Entry(window, width=3,bg='AntiqueWhite')
        tripnumber_entry.place(x=70, y=95)




        lblDesign = Label(window, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10),fg='black',bg="AntiqueWhite")
        lblDesign.place(x=-5, y=375)



        driv = all3()
        tableFrame = Frame(window)
        tableFrame.place(x=130, y=150)

        table = ttk.Treeview((tableFrame), height=8)
        table['columns'] = (('TripID', 'PickUpLocation', 'PickUpTime', 'DropOffLocation', 'Status'))

        table.column("#0", width=0, stretch=NO)
        table.column("TripID", width=70, anchor=CENTER)
        table.column("PickUpLocation", width=125, anchor=CENTER)
        table.column("PickUpTime", width=110, anchor=CENTER)
        table.column("DropOffLocation", width=135, anchor=CENTER)
        table.column("Status", width=90, anchor=CENTER)

        table.heading('#0', text='', anchor=CENTER)
        table.heading('TripID', text='TripID', anchor=CENTER)
        table.heading('PickUpLocation', text='PickUpLocation', anchor=CENTER)
        table.heading('PickUpTime', text='PickUpTime', anchor=CENTER)
        table.heading('DropOffLocation', text='DropOffLocation', anchor=CENTER)
        table.heading('Status', text='Status', anchor=CENTER)

        for driv in driv:
            table.insert(parent='', index='end', iid=driv[0], values=(driv[0], driv[1], driv[2], driv[3],driv[4]))
        table.pack()


        def selecteditems(a):
            tripnumber_entry.delete(0, END)
            selected = table.selection()
            if selected:
                selectedItem = selected[0]
                tripnumber_entry.insert(0, table.item(selectedItem)['values'][0])
        table.bind("<<TreeviewSelect>>", selecteditems)

        window.mainloop()











