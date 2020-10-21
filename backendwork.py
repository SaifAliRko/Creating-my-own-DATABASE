import sqlite3

def connect():
    conn = sqlite3.connect('myDatabase.db')
    cur = conn.cursor()
    # actually as we created table there was an error being poped that table already created
    # to avoid that we deploy a if not exists statement
    cur.execute("CREATE TABLE IF NOT EXISTS myDatabase (Id INTEGER PRIMARY KEY , date text , earnings integer , exercise text , study text , diet text ,python text)")
    conn.commit()
    conn.close()

def insert(date , earnings , exercise , study , diet , python):
    conn = sqlite3.connect('myDatabase.db')
    cur = conn.cursor()
    # as we want our id to be empty since we will not use it.
    cur.execute("INSERT INTO myDatabase VALUES (NULL , ?,?,?,?,?,?)" , (date , earnings , exercise , study , diet , python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('myDatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM myDatabase")
    # since to view a database you need to get all data into rows
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows



# you'll delete things according to ID's
def delete(id):
    conn = sqlite3.connect('myDatabase.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM myDatabase WHERE id=? ", (id,))
    conn.commit()
    conn.close()


# what if a user clicks search without entering anything , so here we need to set the parameters as default
def search(date='' , earnings='' , exercise='' , study='' , diet='' , python=''):
    conn = sqlite3.connect('myDatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM myDatabase WHERE date=?  OR earnings=? OR exercise=? OR study=? OR diet=? OR python=?" , (date , earnings , exercise , study , diet , python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
