import sqlite3

db = sqlite3.connect("contacts.sqlite")
# Now sometimes cursors are useful, but in the scenario where you just want to iterate over the resulting data set,
# Python allows you to execute queries using the connection without having to create a cursor.

# for row in db.execute("SELECT * FROM contacts"):
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)
    # So this is actually an alternative way to do; without explicitly creating the cursor. So actually, the connection
    # execute method does return a cursor when you execute a select statement. But you don't have to worry about
    # explicitly defining one. And we can actually unpack the cursor's tuples, just like we did in the previous module
    # and just we did above.

db.close()
