import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Alice', 6545678123, 'alice@email.com')")
db.execute("INSERT INTO contacts VALUES ('Ace', 1234567, 'ace@email.com')")
# Be noticed that these changes are not permanent until you commit these changes. If you don't, you would lose your
# changes once this session is closed. In other words, all these transactions are rollbacked once the connection is
# closed (check line 31).

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# Now, sometimes, you may actually want the entire dataset in a single list, and rather than using a for loop to build
# up your own list, you can actually use the fetchall method:
print(cursor.fetchall())
# You can see that the fetchall has returned a list containing a tuple for each row in the database. So it is possible
# to get all the rows from a database into a list, and then you can actually move backwards and forwards through the
# items in the list. Because all the data's being retrieved from the cursor by the fetchall method, our for loop,
# though, in this particular case, on line 16, hasn't got anything to print.
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('*' * 20)

# Now, there's also a fetchone method that returns the next row in the cursor:
print(cursor.fetchone())  # But it would return 'None' in this case because of the same reason we mentioned on line 16.

cursor.close()
db.commit()
db.close()
