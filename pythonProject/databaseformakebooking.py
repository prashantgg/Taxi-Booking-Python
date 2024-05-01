import sys
import mysql.connector

def connectdatabase(self):
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4d'
        )
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn


def insertee(pickupaddress,pickuptime,dropoffaddress,cid):
    conn = None
    sql = """INSERT INTO makebooking(pickupaddress,pickuptime,dropoffaddress,status,cid) VALUES(%s,%s, %s,'Pending',%s)"""
    values = (pickupaddress,pickuptime,dropoffaddress,cid)
    result = False
    try:
        conn = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print ("Booking Saved")
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn





def deletebooking (mid):
    conn = None
    sql = "DELETE FROM makebooking WHERE mid=%s"
    values = (mid,)
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def updateTrip(pickup,dropoff,time,mid):
    conn = None
    sql = "UPDATE makebooking SET pickupaddress= %s,dropoffaddress= %s, pickuptime= %s WHERE mid =%s"
    values = (pickup,dropoff,time,mid)
    result = False
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4d'
        )

        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        result = True
        print("Customer Updated")
    except:
        print("Error: ",sys.exc_info() )
    finally:
        del values
        del sql
        del conn
        return result





def all(cid):
    sql = """SELECT * FROM makebooking WHERE cid = %s"""
    records = None
    values = (cid,)
    try:
        conn = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql,values)
        print("working")
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return records

def all2():
    sql = """SELECT * FROM makebooking """
    records = None
    try:
        conn = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql)
        print("working")
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return records

def all3():
    sql = """SELECT * FROM makebooking """
    records = None
    try:
        conn = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql,)
        print("working")
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return records

def searchbyid(mid):
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='level4d'
    )
    cursor = connection.cursor()
    sql = "SELECT * FROM makebooking WHERE mid LIKE '%{}%'".format(mid)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def get_driver_names():
    driver_names = []
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='level4d'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM driver")
    for row in cursor:
        driver_names.append(row[0])
    cursor.close()
    conn.close()
    return driver_names



def updatebookingstatus(mid):
    conn = None
    sql = "UPDATE makebooking SET status = 'Cancelled' WHERE mid = %s"
    values = (mid,)
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result








