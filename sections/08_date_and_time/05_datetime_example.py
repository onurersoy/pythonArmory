import datetime

today = datetime.datetime.today()
# 1st datetime is the module; the 2nd is the class
# There is no 'today' function in datetime module; so we would get an error with 'datetime.today()'; it's the 'today'
# method of datetime class.
print(today)


now = datetime.datetime.now()
# if we imported datetime module as 'import datetime as dt', we could have altered the code above with:
# now = dt.datetime.now
# if we imported datetime module as 'from datetime import datetime', we could have altered the code above with:
# now = datetime.now()
print(now)

# .today() and .now() basically give the same thing.
# You can get better precision with 'now'; it will be the same on Windows tho.
# 'now' can accept an optional tzinfo object. That lets you specify a different timezone, and get the current local
# time in that timezone. We will check that in the next module.

# The documentation also states that 'now' is preferred over the 'utcnow' method.
utc_now = datetime.datetime.utcnow()
print(utc_now)
# I wouldn't be surprised if the 'today' method and 'utc_now' method would be deprecated at some point, and removed
# entirely in a future version of Python. After all, the Zen of Python does state that "there should be one – and
# preferably only one – obvious way to do it".
