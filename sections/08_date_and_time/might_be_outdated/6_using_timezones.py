import pytz  # We are using it to convert UTC to the local time zone
import datetime

# Immediately convert a time you're going to use locally to UTC so only work in UTC, then you convert them back to
# the local time when you want to display them to the users of your program.
# By doing this, you can get rid of almost all time related problems.

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.all_timezones):
    print(x + ": " + pytz.country_names[x])

for x in sorted(pytz.all_timezones):
    # print("{}: {}: {}".format(x, pytz.country_names[x], pytz.county_timezones[x]))
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.county_timezones.get(x)))

for x in sorted(pytz.all_timezones):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.county_timezones:
        for zone in sorted(pytz.coutry_timezones[x]):
            tz_to_display = pytz.timezone(country)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
