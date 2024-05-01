from tkinter import *
from  tkinter import ttk
from databasefordriver import all,search_drivers


class ViewDriver():
    def __init__(self):


        def search():
            name = Name_entry.get()
            for item in table.get_children():
                table.delete(item)
            results = search_drivers(name)
            for result in results:
                table.insert(parent='', index='end', iid=result[0],
                             values=(result[0], result[1], result[2], result[3], result[4], result[5]))


        window = Tk()
        window.title('View Driver')
        window.resizable(False,False)
        window.geometry('800x460')

        mainframe = Frame(window, bg="gray", width=800, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        mainframe = Frame(window, bg="AntiqueWhite", width=800, height=420)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        def Back():
            window.destroy()
            from welcomeadmin import WelcomeAdmin
            WelcomeAdmin.__init__(self)


        lblTitle = Label(window, text="View Driver", font=("Times New Roman", 35,"bold"), fg='black', bg="grey")
        lblTitle.place(x=265, y=20)

        lblTaxi = Label(window, text="Taxi Booking System", font=("forte", 30), fg='black', bg="AntiqueWhite")
        lblTaxi.place(x=200, y=390)

        btnSearch = Button(window, text="Search", bg="skyblue", width=8,command=search)
        btnSearch.place(x=476, y=102)

        btnBack = Button(window, text="Back", bg="firebrick1", width=10,command=Back)
        btnBack.place(x=350, y=345)

        Name = Label(window, text="Name: ", font=("Helvetica", 15, "bold"), bg="AntiqueWhite")
        Name.place(x=220, y=98)
        Name_entry = Entry(window, width=30)
        Name_entry.place(x=290, y=105)

        lblDesign = Label(window, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10),fg='black',bg="AntiqueWhite")
        lblDesign.place(x=-5, y=375)

        driv = all()

        tableFrame = Frame(window)
        tableFrame.place(x=45, y=150)

        table = ttk.Treeview((tableFrame), height=8)
        table['columns'] = (('DID', 'Name', 'Address', 'Email', 'LicensePlate','Password'))

        table.column("#0", width=0, stretch=NO)
        table.column("DID", width=90, anchor=CENTER)
        table.column("Name", width=115, anchor=CENTER)
        table.column("Address", width=125, anchor=CENTER)
        table.column("Email", width=145, anchor=CENTER)
        table.column("LicensePlate", width=115, anchor=CENTER)
        table.column("Password", width=110, anchor=CENTER)


        table.heading('#0', text='', anchor=CENTER)
        table.heading('DID', text='Driver Id', anchor=CENTER)
        table.heading('Name', text='Name', anchor=CENTER)
        table.heading('Address', text='Address', anchor=CENTER)
        table.heading('Email', text='Email', anchor=CENTER)
        table.heading('LicensePlate', text='LicensePlate', anchor=CENTER)
        table.heading('Password', text='Password', anchor=CENTER)


        for driv in driv:
            table.insert(parent='', index='end', iid=driv[0], values=(driv[0], driv[1], driv[2], driv[3],driv[4],driv[5]))
        table.pack()

        window.mainloop()




