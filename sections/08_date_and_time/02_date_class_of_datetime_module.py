import datetime
import locale

# locale.setlocale(locale.LC_ALL, '')

# There are several ways to create a date object. We can pass the year, month, and day, to date, and we'll get back
# a date object representing that date.

start = datetime.date(2022, 2, 4)  # It's the default date format
print(start)

pretty_start = start.strftime('%A %d %B, %Y')  # Remember that it's case-sensitive
# %A : Name of the day of the week
# %d : Day of the month
# %B : Month name
# %Y : Year in 4 digits format
print(pretty_start)
# The 'strftime' options are aware of your computer's locale, and use that language for the names in the string that's
# created.

# You can find all the formatting codes that strftime supports, in the strftime and strptime documentation.
# The link: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# strftime: string-format-time
# strptime: string-parse-time

# Since we have a date object now, we can f.e. get the individual parts of the date.
year = start.year
month = start.month
day = start.day
# The above lines will give the results in a numeric format
print(f'The {year} winter olympics started on day {day} of month {month}')

today = datetime.date.today()
print(today)
print(today.strftime('%A'))
# The above will give the name of the day of the week in a string format

print(today.weekday())  # Remember that the 1st day is 0 which is monday
# If you want to use the locale settings for dates and times, call the setlocale function at the start of your program.
# That's in the locale module, so we'll need to import locale first.
