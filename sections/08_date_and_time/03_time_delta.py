import datetime

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')
print(pretty_start)

duration = datetime.timedelta(days=15)
duration_old = datetime.timedelta(days=15, hours=4)  # We lost our 4 hours because dates don't have a time part.
end = start + duration
print(end)
print(duration)
print(duration_old)

duration2 = datetime.timedelta(days=15, hours=48)
# The duration of 15 days and 48 hours has been normalized to 17 days – which we can confirm by printing out duration:
# Run the program again and notice that the duration is 17 days, as we expected. That's all normalization means. If
# you provide any units that timedelta doesn't store, they get converted to the units that it does store. That means
# you can specify a duration in one set of units, and it will compare equal to the same duration specified in different
# units.
# Two hours are 120 minutes, which is 7,200 seconds. The timedelta class will store the seconds, converting the other
# units to their corresponding number of seconds. So each of these objects will be equal. Run the program to check.
# Each of the values, in the last line of the output, represents 2 hours.
end2 = start + duration2
print(end2)
print(duration2)

d1 = datetime.timedelta(hours=2)
d2 = datetime.timedelta(minutes=120)
d3 = datetime.timedelta(seconds=7200)
print(d1, d2, d3, sep=', ')
print(repr(d1), repr(d2), repr(d3), sep=', ')
# Run the program, to confirm that each of those delta objects represent exactly the same duration. The timedeltas are
# all storing 7,200 seconds. The hours and minutes that we provided, on lines 17 and 18, have been "normalized" to
# seconds. OK, you can add or subtract a timedelta to a date, and you can also add and subtract them to or from each
# other. You can also subtract 2 dates to get a timedelta.

difference = end - start
print(repr(difference))  # Let's use 'repr' again so that we can see that the above result is a timedelta, and not a
# time.
print(difference == duration)

# Although you can subtract dates, to get the difference between them, you can't add dates together. That's reasonable
# – the sum of 2 dates doesn't mean anything. So you'll get an error if you try.
