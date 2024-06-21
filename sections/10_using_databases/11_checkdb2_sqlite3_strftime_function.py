import sqlite3

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime') AS localtime, "
                      "transactions.account, transactions.amount FROM transactions ORDER BY transactions.time"):
    print(row)
    # We now used SQL to display the time field in our local time zone.
    # There is also 'datetime' function we can use on SQL instead of 'strftime', so there is not only a single approach
    # but many, feel free to explore.

db.close()
