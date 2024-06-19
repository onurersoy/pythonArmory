import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 1234567"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows updated.")
print('-' * 20)

print(f"Are connections same?: {update_cursor.connection == db}")
print('-' * 20)
update_cursor.connection.commit()  # ***It's also possible to commit by cursor, so you can have your connection alive
# while committing your transactions; even keeping alive your cursor. It might be what you need from time to time.***
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

# db.commit()
db.close()
