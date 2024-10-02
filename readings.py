import sqlite3
# conn = sqlite3.connect(":memory:") ## this creates in-memory database
conn = sqlite3.connect("customer.db")
#Create Cursor
c  = conn.cursor()

#c.execute("SELECT rowid, * FROM customers")
#c.fetchone()
#c.fetchmany(3)
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Abd%' ")
items= c.fetchall()
for item in items:
    print(item) 