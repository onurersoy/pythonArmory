import sqlite3

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM transactions"):
    # print(row)
    time_field = row[0]  # It would normally return as a string value but 'detect_types=sqlite3.PARSE_DECLTYPES' makes
    # it recognizable for its original type by Python and automatically converts it to the respected type. We needed it
    # to be able to convert it to different kinds of time fields, like local time zone etc. We couldn't use the related
    # functions while it was a string.
    # You can now use builtin functions to display 'time_field' in your local timezone etc. (datetime module)
    # Always work in UTC, then convert when you need to display or print the local times!
    print(f"{time_field}\t{type(time_field)}")

db.close()

# Also check 'dateutil' module, which is an extension to the standard Python datetime module.
