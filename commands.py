import sqlite3
# conn = sqlite3.connect(":memory:") ## this creates in-memory database
conn = sqlite3.connect("customer.db")
#Create Cursor
c  = conn.cursor()
#c.execute("INSERT INTO customers VALUES ('Ammar','Abdilghanie','aelghany@gmail.com')")
many_customers=[
('Ammar1','Abdilghanie1','aelghany1@gmail.com'),
('Amr','Abdilgh','aelgh@gmail.com'),
('Amor','Abd','aelg@gmail.com')
]
c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)
conn.commit()
conn.close()

print("Command Executed Successfully!")