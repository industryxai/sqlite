import sqlite3
# conn = sqlite3.connect(":memory:") ## this creates in-memory database
conn = sqlite3.connect("customer.db")
#Create Cursor
c  = conn.cursor()

# c.execute("""UPDATE customers SET first_name = 'Amoose' 
#           WHERE first_name='Bob'
#           """)

# c.execute("UPDATE customers SET first_name = ? WHERE rowid = ?", ("Holger", 2))
# c.execute("DELETE FROM customers WHERE rowid = ?", (2,))
# c.execute("DELETE FROM customers WHERE rowid = 6")

# Commit the changes
conn.commit()


#c.execute("UPDATE customers SET first_name = ? WHERE last_name = ?", ("Bob", "Elder"))

conn.commit()
c.execute("SELECT * FROM customers")
items= c.fetchall()
for item in items:
    print(item) 


c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
rows = c.fetchall()

for row in rows:
    print(row)

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'abd%' OR rowid = 3 ORDER BY rowid LIMIT 2")
rows = c.fetchall()
print("*"*100)
for row in rows:
    print(row)


# c.execute("DROP TABLE customers")

# # Commit the changes
# conn.commit()
