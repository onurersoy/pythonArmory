# Time class stores times independent of any particular day. Because of that, you probably won't use this class.
# You'll use the datetime class when you want to work with real dates and times, rather than this time class.
# A datetime object is a single object containing all the information from a date object and a time object. Notice that
# this module is added just to know what a time object is, and also know that it's probably not what you want to use.

# UTC = Coordinated Universal Time (It's not CUT but UTC because it's actually in French; Temps Universel Coordonne -
# or TUC)
# UTC is a time standard, not a timezone. Think of it as the time that all the timezones are measured against. It's
# measured using very accurate atomic clocks.

# the tz database, aka the IANA or Olson database:
# We need a database, to keep track of which timezones are in use, and where. Such a database was created, in around
# 1986, by Arthur David Olson. That's why it's sometimes called the Olson database. The database is maintained by IANA
# – the Internet Assigned Numbers Authority. That's the same organization that oversees IP addresses worldwide
# amongst other internet-related things. The database is kept up to date, which usually involves several updates each
# year.
# The tz database also tracks the dates when daylight savings time is in effect, for each of the timezones. That data
# is historical, so you can get the correct local time for times in the past.
# DST = Daylight Savings Time
from datetime import time, date

meeting = time(hour=11, minute= 15, second=0)
print(meeting)

end_time = time(hour=12, minute=30)
print(end_time)
# OK, to find out how long the meeting lasted, we want to subtract the start time from the end time. Unfortunately,
# we can't do that. Subtraction isn't supported for these datetime.time objects. You also can't use a timedelta to
# get a time before or after another time.
# There's a good reason for that – if the timedelta would take the time into the next day, or into the previous day
# when subtracting, the new time couldn't reflect that. There's no way of tracking the date when using a time object.

# Fortunately, the datetime module provides another class that we can use, and we'll look at that in the next module.

# Let's check another way to create time objects. We can provide a time as a string, in ISO 8601 format:
iso_time = '11:15:00'
_time = time.fromisoformat(iso_time)
print(_time)

# We can actually do the same thing with dates:
iso_date = '2022-05-10'
_date = date.fromisoformat(iso_date)
print(_date)
# We get the date as a datetime.date object. That can be a useful way to get dates from an external source – such as
# when reading them from a text file. That's the reason for the ISO standard – it exists to allow the exchange of date
# and time-related data.
