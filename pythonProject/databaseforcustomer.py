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

def insert(customer1):
    conn = None
    sql = """INSERT INTO customers VALUES(%s,%s, %s, %s, %s,%s,%s)"""
    values = (customer1.getCID(),customer1.getNAME(),customer1.getADDRESS(),customer1.getEMAIL(),customer1.getPASSWORD(),customer1.getMOBILENO(),customer1.getCREDITCARD())
    # result = False
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
        print ("Customer Save")
        # result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        # return result


def search(email,password):
    sql = """SELECT * FROM customers WHERE email=%s AND password = %s"""
    values = (email,password)
    print("working")
    record = None
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
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def allexcract():
    sql = """SELECT * FROM customers"""
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
        records = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return records


def search_customers(name):
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='level4d'
    )
    cursor = connection.cursor()
    sql = "SELECT * FROM customers WHERE name LIKE '%{}%'".format(name)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results






