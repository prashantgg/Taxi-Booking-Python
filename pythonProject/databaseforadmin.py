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


def searchee(email,password):
    sql = """SELECT * FROM admin WHERE email=%s and password=%s"""
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





