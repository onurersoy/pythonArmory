import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to search for ")

for row in db.execute("SELECT * FROM contacts where name = ?", (name,)):
    # Notice the comma after 'name' parameter. # TODO: Needs to be further investigated
    print(row)

db.close()
