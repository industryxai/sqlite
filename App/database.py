import sqlite3

import sqlite3

def create_table():
    # Connect to the database
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    # Drop the customers table if it already exists
    c.execute("DROP TABLE IF EXISTS customers")
    
    # Create the customers table
    c.execute('''CREATE TABLE customers (
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT
                )''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()



def show_all():
    
    conn = sqlite3.connect("customer.db")
    c  = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers")
    items= c.fetchall()
    
    for item in items:
        print(item) 

    conn.commit()
    conn.close()
    
def add_one(first, last, email):
    # Connect to the database
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    # Insert a new record into the customers table
    c.execute("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", (first, last, email))
    
    conn.commit()
    conn.close()


def delete_one(id):
    # Connect to the database
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    # Delete the record with the specified rowid
    c.execute("DELETE FROM customers WHERE rowid = ?", (id,))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def add_many(records):
    # Connect to the database
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    # Insert multiple records into the customers table
    c.executemany("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", records)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def email_lookup(email):
    # Connect to the database
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    # Execute a query to find the customer by email
    c.execute("SELECT rowid, * FROM customers WHERE email = ?", (email,))
    customers = c.fetchall()
    # Loop through and print each customer record
    for customer in customers:
        print(customer)
    
    # Close the connection
    conn.close()
    
    # Return the customer information
    return customer
