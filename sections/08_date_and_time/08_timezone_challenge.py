from datetime import datetime, timezone
import zoneinfo

# Timezone keys for creating the ZoneInfo objects.
zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi',
)

# Get the current time, in UTC
# utc_now = datetime.now(tz=timezone.utc)
local_now = datetime.now()
# local_now = local_now.replace(microsecond=0)  # It gets rid of microseconds. But note that we've modified the times
# above, and those micro-seconds are now lost. If we want to display the times without micro-seconds, but need to
# keep the original accuracy for our calculations, then we can use the strftime method. That will let us display the
# times in exactly the format we want.

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)
    # required_time = datetime.now(tz=tz)
    required_time = local_now.astimezone(tz)
    # The city is the last item, after splitting the zone at the /
    city = zone.split('/')[-1]
    # print(f'The time in {city} is {required_time}')
    print(f'The time in {city} is {required_time.strftime("%m/%d/%Y %H:%M:%S %z %Z")}')
    # Now we've lost the microseconds from the above output but the datetime objects still contain the micro-seconds,
    # so this approach would be useful if you needed to retain that level of accuracy. The strftime method is more
    # flexible, and doesn't modify the actual values that you're displaying, so you should certainly become familiar
    # with those format codes, if you'll be working with dates and times often.

    # If we're not going to use strftime, we can call the tzname method of our datetimes. tzname returns the timezone
    # name as a string:
    print(f'The time in {city} is {required_time} {required_time.tzname()}')
