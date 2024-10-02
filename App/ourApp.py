import database

# Create a customers table for testing if it doesn't already exist

database.create_table()

# Add some customers using add_one() function
database.add_one("Alice", "Smith", "alice.smith@example.com")
database.add_one("Bob", "Johnson", "bob.johnson@example.com")
database.add_one("Charlie", "Brown", "charlie.brown@example.com")

# Show all customers to verify the insertion
print("Customers before deletion:")
database.show_all()

# Delete the customer with rowid 2
database.delete_one(2)

# Show all customers to verify the deletion
print("\nCustomers after deletion of rowid 2:")
database.show_all()

customers_list = [
    ("Alice", "Smith", "alice.smith@example.com"),
    ("Bob", "Johnson", "bob.johnson@example.com"),
    ("Charlie", "Brown", "charlie.brown@example.com"),
    ("Daisy", "Miller", "daisy.miller@example.com")
]

# Add multiple records using add_many() function
database.add_many(customers_list)

# Show all customers to verify the insertion
print("Customers in the database after adding multiple records:")
database.show_all()

print("Looking up email \n")
database.email_lookup("alice.smith@example.com")
