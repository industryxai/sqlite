import sqlite3
# conn = sqlite3.connect(":memory:") ## this creates in-memory database
conn = sqlite3.connect("customer.db")
#Create Cursor
c  = conn.cursor()
#Create a Table 
c.execute("""CREATE TABLE customers (
          first_name text, 
          last_name text,
          email text
          )""")
## Commit our command
conn.commit()
## Close Our connection
conn.close()

##SQLITE has only five datatypes  NULL, INTEGER, REAL, TEXT , BLOB 
# one line is required if you were to use double quotations as oppossed to docstrings
# c.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")
