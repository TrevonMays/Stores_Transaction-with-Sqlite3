import sqlite3 

# define connection and cursor

connection = sqlite3.connect('stores_transaction.db')

cursor = connection.cursor()

# create store tables

command1 = """CREATE TABLE IF NOT EXISTS
stores(stores_id INTEGER PRIMARY KEY, LOCATION TEXT)"""

cursor.execute(command1)

# Create purchase table

command2 ="""CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# add to stores
cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis,MN')")
cursor.execute("INSERT INTO stores VALUES (85, 'Atlant,Ga')")
cursor.execute("INSERT INTO stores VALUES (83, 'Kaneohebay, HI')")


# add to purschase

cursor.execute("INSERT INTO purchases VALUES (60,21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23,64, 21.12)")

# get results

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()

print(results)

# Update
cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")

# Delete
# cursor.execute("Delete FROM purchases WHERE purchase_id = 54")