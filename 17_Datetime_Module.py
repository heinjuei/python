# Datetime Module
import datetime

dir(datetime)
help(datetime.date)

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

# Operations in Datetime

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100) #add 100 days to date mill
mill + dt

""" yyyy-mm-dd """

# Day-name, Month-name Day-#, Year

print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

dir(datetime)

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

# Current datetime

now = datetime.datetime.today()
print(now)
print(now.microsecond)

# Convert Strings to Datetimes

moon_landing = "7/20/1969"

""" module: datetime """
""" class: datetime """
""" method: strptime() """

moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
