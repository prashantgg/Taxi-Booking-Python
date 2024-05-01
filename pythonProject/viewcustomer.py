from tkinter import *
from  tkinter import ttk
from databaseforcustomer import allexcract, search_customers




class ViewCustomer():
    def __init__(self):

        window = Tk()
        window.title('View Customer')
        window.resizable(False,False)
        window.geometry('800x460')

        mainframe = Frame(window, bg="gray", width=800, height=90)
        mainframe.pack()
        mainframe.place(x=1, y=1)

        mainframe = Frame(window, bg="AntiqueWhite", width=800, height=420)
        mainframe.pack()
        mainframe.place(x=0, y=90)

        def Wel():
            window.destroy()
            from welcomeadmin import WelcomeAdmin
            WelcomeAdmin.__init__(self)


        lblTitle = Label(window, text="View Customer", font=("Times New Roman", 35,"bold"), fg='black', bg="grey")
        lblTitle.place(x=215, y=20)

        lblTaxi = Label(window, text="Taxi Booking System", font=("forte", 30), fg='black', bg="AntiqueWhite")
        lblTaxi.place(x=200, y=390)


        def search():
            name = Name_entry.get()
            for item in table.get_children():
                table.delete(item)
            results = search_customers(name)
            for result in results:
                table.insert(parent='', index='end', iid=result[0],
                             values=(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))



        btnSearch = Button(window, text="Search", bg="skyblue", width=8, command=search)
        btnSearch.place(x=476, y=102)

        btnBack = Button(window, text="Back", bg="firebrick1", width=10,command=Wel)
        btnBack.place(x=350, y=345)

        Name = Label(window, text="Name: ", font=("Helvetica", 15, "bold"), bg="AntiqueWhite")
        Name.place(x=220, y=98)
        Name_entry = Entry(window, width=30)
        Name_entry.place(x=290, y=105)

        lblDesign = Label(window, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("comicsansm", 10),fg='black',bg="AntiqueWhite")
        lblDesign.place(x=-5, y=375)

        cust = allexcract()

        tableFrame = Frame(window)
        tableFrame.place(x=17, y=150)

        table = ttk.Treeview((tableFrame), height=8)
        table['columns'] = (('CID', 'Name', 'Address', 'Email', 'Password','MobileNumber','CreditCardNo'))

        table.column("#0", width=0, stretch=NO)
        table.column("CID", width=80, anchor=CENTER)
        table.column("Name", width=110, anchor=CENTER)
        table.column("Address", width=120, anchor=CENTER)
        table.column("Email", width=140, anchor=CENTER)
        table.column("Password", width=110, anchor=CENTER)
        table.column("MobileNumber", width=95, anchor=CENTER)
        table.column("CreditCardNo", width=110, anchor=CENTER)

        table.heading('#0', text='', anchor=CENTER)
        table.heading('CID', text='Customer Id', anchor=CENTER)
        table.heading('Name', text='Name', anchor=CENTER)
        table.heading('Address', text='Address', anchor=CENTER)
        table.heading('Email', text='Email', anchor=CENTER)
        table.heading('Password', text='Password', anchor=CENTER)
        table.heading('MobileNumber', text='MobileNumber', anchor=CENTER)
        table.heading('CreditCardNo', text='CreditCardNo', anchor=CENTER)

        for cust in cust:
            table.insert(parent='', index='end', iid=cust[0], values=(cust[0], cust[1], cust[2], cust[3],cust[4],cust[5],cust[6]))
        table.pack()


        window.mainloop()











