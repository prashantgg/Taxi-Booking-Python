import sys
import mysql.connector

#class driver:
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

def insert(driver):
    conn = None
    sql = """INSERT INTO driver VALUES(%s,%s, %s, %s, %s, %s,%s)"""
    values = (driver.getDID(),driver.getNAME(),driver.getADDRESS(),driver.getEMAIL(),driver.getLICENSEPLATE(),driver.getPASSWORD(), ' ')
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
        print ("Customer Save")
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn





def searche(email,password):
    sql = """SELECT * FROM driver WHERE email=%s and password=%s"""
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



def all():
    sql = """SELECT * FROM driver"""
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

def search_drivers(name):
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='level4d'
    )
    cursor = connection.cursor()
    sql = "SELECT * FROM driver WHERE name LIKE '%{}%'".format(name)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results







