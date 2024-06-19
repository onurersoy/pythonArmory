# This module is also about placeholders and parameter substitutions!

import sqlite3

db = sqlite3.connect("contacts.sqlite")

# Let's use f-string instead of hardcoded values (line 11):
new_email = "anotherupdate@update.com"
# phone = 1234567
phone = input("Please enter the phone number: ")
# update_sql = f"UPDATE contacts SET email = '{new_email}' WHERE contacts.phone = {phone}"
# This approach leaves you open for SQL injection attacks if you depend on a user input. Because someone can put this
# to input and harm your data integrity: "1234;drop table contacts".

# Let's comment out line 11 first. To avoid getting an SQL injection attack, you can use this kind of approach:
update_sql = f"UPDATE contacts SET email = ? WHERE contacts.phone = ?"  # << Placeholders
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))  # << Parameter substitutions
print(f"{update_cursor.rowcount} rows updated.")
print('-' * 20)

print(f"Are connections same?: {update_cursor.connection == db}")
print('-' * 20)
update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close()

# So never create a string to be run as an SQL script if any of the value are coming from an outside user's input.
# That's not a secure approach.
