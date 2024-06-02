# Before 'zoneinfo' module, dealing with international times was a bit of a nightmare. There were a number of
# third-party libraries available, including pytz and dateutil. The dateutil module is a more accurate representation
# of Python's tzinfo class, but doesn't handle the situation when times are put back an hour.

from datetime import datetime, timezone
# Conditional importing:
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)

france_tz = zoneinfo.ZoneInfo('Europe/Paris')
france_now = utc_now.astimezone(france_tz)
print(france_now)

print()
print('Available timezone keys')
print('-----------------------')

for zone_key in sorted(zoneinfo.available_timezones()):
    print(zone_key)
