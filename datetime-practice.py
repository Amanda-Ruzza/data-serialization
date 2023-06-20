import datetime
import pytz

# The 'now' method works better with the pytz package and using UTC timezones
date_time_now = datetime.datetime.now(tz=pytz.UTC)
# converting current time into different timezones:
date_time_now_mtn_time = date_time_now.astimezone(pytz.timezone('US/Mountain'))
mtn_iso_format = date_time_now_mtn_time.isoformat()
print(f"This is MTN Time in ISO Format:\t{mtn_iso_format}")


print(date_time_now_mtn_time.strftime("%B %d, %Y"))
    
# for tz in pytz.all_timezones:
#     print(tz)

us_eastern_timezone = pytz.timezone('US/Eastern')

# The 'utcnow' method is too complicated to use with the pytz package
date_time_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

# print(date_time_now, "\n")
print(f"Using the 'now' method and pytz to convert the current time into US MTN time:\n{date_time_now_mtn_time}\n")

# print(date_time_utc, "\n")

# converting 'EPOCH TIME' into a readable format of: 2021-08-31 00:00:00
timestamp = datetime.datetime.now().timestamp()
print(f"\nThis is the current time in epoch format:\t{timestamp}")

# the 'fromtimestamp' method converts EPOCH TIME in a regular date/time format:
date_time_object = datetime.datetime.fromtimestamp(timestamp)
print(f"\nThis is the current time in readable format:\t{date_time_object}")


# converting a STRING into a Date Time using the strptime method:
date_time_string = "June 22, 1971"
date_integer = datetime.datetime.strptime(date_time_string, "%B %d, %Y")
print(f"\nThis is the conversion result from string to integer:\t {date_integer}")