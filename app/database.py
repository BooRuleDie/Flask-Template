import sqlite3
import datetime

def runSQL(SQL, data = (), fetch = False):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()        
        cursor.execute(SQL, data)
        conn.commit()

        if fetch:
            result = cursor.fetchall()
            return result

    except sqlite3.Error as e:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("errors.log", "a") as f:
            f.write(now + ": " + str(e) + "\n\n")
            
    finally:
        cursor.close()
        conn.close()