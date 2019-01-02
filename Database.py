import sqlite3

def ReadImage(filename):
    try:
        fin = open(filename, "rb")
        return fin.read() 
    except:
        print("Error")
    finally:
        if fin:
            fin.close()

def WriteImage(data, filename):
    try:
        fout = open(filename, "wb")
        fout.write(data)
    except:
        print("Error")
    finally:
        if fout:
            fout.close()
            
def Create_table(name_database, name_table, fields):
    try:
        conn = sqlite3.connect(name_database)
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS {name_table} ({fields})")
        conn.commit()
        print("Success")
    except:
        if conn:
            conn.rollback()
        print("Error")
    finally:
        if conn:
            conn.close()
            
def Add_values(name_database, name_table, field, filename):
    try:
        conn = sqlite3.connect(name_database)
        cur = conn.cursor()
        data = ReadImage(filename)
        binary = sqlite3.Binary(data)
        cur.execute(f"INSERT INTO {name_table}({field}) VALUES(?)", (binary,))
        conn.commit()
        print("Success")
    except:
        if conn:
            conn.rollback()
        print("Error")
    finally:
        if conn:
            conn.close()
            
            
def Get_values(name_database, name_table, field):
    try:
        conn = sqlite3.connect(name_database)
        cur = conn.cursor()
        cur.execute(f"SELECT {field} FROM {name_table}")
        values = cur.fetchone()[0]
        print("Success")
        return values
    except:
        if conn:
            conn.rollback()
        print("Error")
    finally:
        if conn:
            conn.close()