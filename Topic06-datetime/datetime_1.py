# Messing with datetime 
# Author: Andre

import datetime

# What is inside datetime?
print(dir(datetime))

# manipulating datetime.time to print the hour, minute and seconds
t = datetime.time(1, 2, 3)
print(t)
print(f'Hour: {t.hour}')
print(f'minute: {t.minute}')
print(f'second: {t.second}')
print(f'microsecond: {t.microsecond}')
print(f'tzinfo: {t.tzinfo}')

# get the valid range of times in a single day
print('Earliest: ', datetime.time.min)
print('Latest: ', datetime.time.max)
print('Resolution: ', datetime.time.resolution)

# Create a time object with 5 microseconds and 39 minutes
t1 = datetime.time(1,39,1,5)
print(t1)

# Dates (datetime.time)
today = datetime.date.today()
print(f'today: \n\t {today}')
print(f'ctime: \n\t {today.ctime()}')
print(f'tuple: \n\t {today.timetuple()}')
print(f'ordinal: \n\t {today.toordinal()}')
print(f'Year: \n\t {today.year}')
print(f'Month: \n\t {today.month}')
print(f'Day: \n\t {today.day}')

# There are also class methods for creating instances from integers 
import time

o = 733114
print(f'o = {o} and fromordinal(o) = {datetime.date.fromordinal(o)}')
t2 = time.time()
print(f't = {t2} and fromtimestamp(t2) = {datetime.date.fromtimestamp(t2)}')

# Also determine the range fo date values
print(f'Earliest: {datetime.date.min}')
print(f'Latest: {datetime.date.max}')
print(f'Resolution: {datetime.date.resolution}')

# Another way to create new date uses the replace()
d1 = datetime.date(2022, 7, 5)
print('d1: ', d1)
d2 = d1.replace(year=2023)
print('d2: ', d2)
help(d1.replace)

# Create a date object where year os 2023 and the day is 5
day3 = datetime.date(2025, 1, 9)
print('Day 3: ', day3)
day4 = day3.replace(year=2023, day=3)
print('Day 4 : ', day4)

# Timedeltas represents the duration
# datetime.timedelta(days=0, seconds=0, microsencods=0, milliseconds= 0,
#                    minutes=0, hours=0, weeks=0)
print(f'microsenconds: {datetime.timedelta(microseconds=1)}')
print(f'milliseconds: {datetime.timedelta(milliseconds=1)}')
print(f'seconds: {datetime.timedelta(seconds=1)}')
print(f'minutes: {datetime.timedelta(minutes=1)}')
print(f'hours: {datetime.timedelta(hours=1)}')
print(f'days: {datetime.timedelta(days=1)}')
print(f'weeks: {datetime.timedelta(weeks=1)}')
print()

# Date arithmetic
today = datetime.date.today()
print('Today:', today)
one_timedelta_day = datetime.timedelta(days=1)
print('One time delta: ', one_timedelta_day)
yesterday = today - one_timedelta_day
print('Yesterday: ', yesterday)
tomorrow = today + one_timedelta_day
print('Tomorrow: ', tomorrow)
print('tomorrow - yesterday: ', tomorrow - yesterday)
print('yesterday - tomorrow: ', yesterday - tomorrow)

# Create an arbritary date object and add five weeks
today2 = datetime.date.today()
print('Today: ', today2)
week_timedelta_day = datetime.timedelta(weeks=5)
add_5weeks = today2 + week_timedelta_day
print('5 weeks + today: ', add_5weeks)

# Comparing values 
print('Times: ')
t1 = datetime.time(12, 55, 0)
print('\tt1:', t1)
t2 = datetime.time(13, 5, 0)
print('\tt2: ', t2)
print('\tt1 < t2: ', t1 < t2)

print('Dates: ')
d1 = datetime.date.today()
print('\td1: ', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('\td2: ', d2)
print('\td1 > d2 ', d1 > d2)

# Combining Dates and Times: datetime class
# datetime.datetime(year, month, day, hour=0, minute=0, second=0,
#                   microsecond=0, tzinfo=None, *, fold=0)
print(f'Now: {datetime.datetime.now()}')
print(f'Today: {datetime.datetime.today()}')
print(f'UTC now: {datetime.datetime.utcnow()}')

d = datetime.datetime.now()
for attr in ['year', 'month', 'day', 'hour',
              'minute', 'second', 'microsecond']:
    print(f'{attr}: {getattr(d, attr)}')

NOW = datetime.datetime.now()
print(f'Current date & time = {NOW}')
print(f' Date and time in ISO format= {NOW.isoformat()}')
print(f'Current year = {NOW.year}')
print(f'Current month = {NOW.month}')
print(f'Current date (day) = {NOW.day}')
print(f'dd/mm/yyyy format = {NOW.day}/{NOW.month}/{NOW.year}')
print(f'Current hour = {NOW.hour}')
print(f'Current minute = {NOW.minute}')
print(f'Current second = {NOW.second}')
print(f'hh:mm:ss format = {NOW.hour}:{NOW.minute}:{NOW.second}')
print()

# Formatting date weekday month day hour:minute:second Year
format = "%a %d %b %H:%M:%S %Y"
today = datetime.datetime.today()
print(f'ISO: {today}')

s = today.strftime(format)
print(f'strftime: {s}')
print()

# Obtain the time in HH:MM:SS
print(today.strftime("%X"))
# Obtain the hour with 12 hours time
print(today.strftime("%I"))
# Obtain AM or PM
print(today.strftime('%p'))
# Obtain %c local date time, %x local's date, %X locals time
print(today.strftime('%c'))
print(today.strftime('%x'))
print(today.strftime('%X'))
print()

# Changing USA date to European date
datetime_str = 'Sep 19 2020 2:42PM'
datetime_fmt = "%b %d %Y %I:%M%p"
datetime_obj = datetime.datetime.strptime(datetime_str, datetime_fmt)
print('Date: ', datetime_obj.date())
print('Time: ', datetime_obj.time())
print('Date-time ', datetime_obj)
print('String date: ', datetime_obj.strftime(datetime_fmt))

# Write a function that takes 2 arguments(8 digits int YYYYMMDD) and
# returns the number of days between the two dates
def number_days_between(first_date,second_date):
    format =  '%Y%m%d'
    # convert intenger to strings, then to datetime objects
    actual_date = datetime.datetime.strptime(str(first_date), format)
    other_date = datetime.datetime.strptime(str(second_date), format)
    # Calculate the difference in days
    days_difference = abs((actual_date - other_date).days)
    
    return days_difference

print(number_days_between(20200617, 20200619))
print(number_days_between(20200619, 20100219))