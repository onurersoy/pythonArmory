# We've seen that the cause of our problem was an invalid date ('09_dst_problem.py'). We produced that invalid date
# by adding a timedelta to a valid UK datetime. If performing arithmetic on local, aware times can cause problems; then
# it makes sense not to do that. Instead, convert your local time to UTC, before doing arithmetic, such as adding
# timedeltas. When you've finished performing the arithmetic, convert the UTC datetime back to the original timezone.

from datetime import datetime, timezone, timedelta

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

uk_tz = zoneinfo.ZoneInfo('Europe/London')
america_tz = zoneinfo.ZoneInfo('America/New_York')

year = 2022
month = 3
day = 27
hour = 0
minute = 25

td = timedelta(minutes=5)

uk_time = datetime(year, month, day, hour, minute, tzinfo=uk_tz)
utc_time = uk_time.astimezone(timezone.utc)  # UTC doesn't have daylight saving, so we can't get problems with creating
# invalid UTC times. We can add any values to a UTC time, and the new time will be valid.
utc_time = utc_time + td
uk_time = utc_time.astimezone(uk_tz)
uk_to_utc = uk_time.astimezone(timezone.utc)
# We haven't performed any arithmetic with our local time. We convert the UK time to UTC on line 25. Any arithmetic is
# performed using the UTC time. In this case, we add the timedelta, to increase the time by 5 minutes, on line 27.
# After we've done all the sums, we can convert the UTC time back to the original timezone, if that's what we want to
# display to the user. We do that on line 28.

uk_time = datetime(year, month, day, hour, minute, tzinfo=uk_tz)
uk_time = uk_time + td
uk_to_utc = uk_time.astimezone(timezone.utc)
print(f'Line 27 - utc_time:\t {utc_time}')
print(f'Line 28 - uk_time:\t {uk_time}')
print(f'Line 29 - uk --> utc:\t {uk_to_utc}')

ny1 = uk_time.astimezone(america_tz)
ny2 = utc_time.astimezone(america_tz)
print()
print(f'uk --> ny:\t {ny1}')
print(f'utc --> ny:\t {ny2}')
print(ny1 == ny2)

# <------------------------------------------->
print()
print('*' * 40)
print(f'Check: uk time equals UTC time: {uk_time == utc_time}')
print(f'Check: uk in UTC equals UTC time: {uk_to_utc == utc_time}')
print('-' * 40)

# If you're going to manipulate datetime objects – by adding to them, or subtracting two times – then a good
# guideline is to convert the times to UTC first. After manipulating the times, you can convert back to the original
# timezone, to display the result to your users.
