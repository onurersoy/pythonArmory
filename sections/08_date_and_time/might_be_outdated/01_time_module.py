# Python standard library provides 3 modules to help us deal with dates and times, and that's the 'time',
# 'datetime' and 'calendar' modules.
# 'Time' documentation link: https://docs.python.org/3/library/time.html
import time

print(time.gmtime(0))  # gm time always works in UTC
print(time.localtime())
# GM time and local time convert the number of seconds into a struct_time and that's actually a 'named tuple' so we
# are going to be looking at how to create our owned named tuples later and this is a good opportunity to see how to
# use them:
# They just like order tuples that we've seen previously, but also they allow the individual items in a tuple to be
# accessed using a name and that can be a very useful way to make a code much more readable.

print(time.time())  # this is the epoch
print(time.localtime(time.time()))  # You can pass the epoch to localtime or gm time too
print("haha")

print('*' * 30)
# Let's try what we explained on the paragraph above:
time_here = time.localtime()
print(time_here)
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)
# So whenever you see a 'named tuple' mention in the documentation, you can treat it just like an ordinary tuple with
# the advantage of accessing the individual fields in the tuple by their names.
