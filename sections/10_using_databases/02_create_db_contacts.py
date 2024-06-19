import sqlite3

db = sqlite3.connect("contacts.sqlite")  # << A connection statement. It will also create the db while trying to connect
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@email.com')")

# Now you can use a cursor to query the data in 'contacts' table:
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# Each row is printed as a tuple containing a value for each of the columns in the database.
# A db cursor is an iterable, so we can just use a for loop to iterate over the cursor and print each row.

# for row in cursor:
#     print(row)

# And what we could also do, if we wanted to, we can unpack the tuples as we go, so we could slightly change the syntax
# like:
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('*' * 20)
# Okay, so our cursor code uses the cursor's execute method to execute the SQL against the database and return something
# that behaves very much like a list. So we can iterate over it to process each row, but it's really not a list. And if
# you think about it, a database table could contain; you know, literally billions of rows. So if the cursor tried to
# load them all into a list in memory, it's highly likely we'd run out of memory. So a cursor is what's called a
# generator.

# A generator is basically an iterable that works by generating the next value each time it's used in Python. You can
# create an iterable object that will return every single possible integer number. So you could count to infinity
# without running out of memory. Time may be against you, of course, but memory wouldn't be a problem.

# So when our code iterates over the cursor, it returns the next row from the database but doesn't actually keep track
# of previous rows. Now because it's not really a list, there's no way to go back to previous records, and that explains
# why if you try to print out the same cursor without re-executing the select statement, it wouldn't print at all.
# Because all the rows are already printed once and there is no way to retrieve the previous records now.

cursor.close()
db.close()

# A note about using semicolon:
# Notice that we did not use semicolon ';' on the above queries! While keeping with the Python philosophy, you'll find
# they're generally not used. In fact, they can often get in the way if you store a select statement in a string, and
# later concatenate a where clause at the end. You don't wanna have to search for and remove a trailing semicolon at the
# end of the select statement. So my recommendation is generally, don't use semicolons when using SQL in Python.
