import datetime
from datetime import date as dt
from datetime import timedelta as td
from datetime import time as tm
from datetime import datetime as dtm
import time


print(dir(datetime))
print('MINYEAR =', datetime.MINYEAR, 'MAXYEAR =', datetime.MAXYEAR)
print()


# timedelta objects
print(dir(td))
print('timedelta: min =', td.min, 'max =', td.max, 'resolution =',
      td.resolution)
td_days1 = td(99)
print(td_days1)
print('td_days1.days, td_days1.seconds, td_days1.microseconds =', td_days1.days, td_days1.seconds,
      td_days1.microseconds)
td_days2 = td(1)
print(td_days2)
print('td_days1, td_days2, td_days1 + td_days2 =', td_days1, '|', td_days2, '|',
      td_days1 + td_days2)
td_secs = td(seconds=60)
print('num minutes in a day =', td_days2 / td_secs)
print('ten days =', td_days2 * 10)
td_days3 = td_days2 * 9.99
print('approximately ten days =', td_days3)
td_days4 = td(days=1, hours=1)
print('td_days4 =', td_days4)
print('(td_days2 * 10) % td_days4 =', (td_days2 * 10) % td_days4)
print('divmod((td_days2 * 10), td_days4) =', divmod((td_days2 * 10), td_days4))
td_millisecs = td(milliseconds=-999)
print('td_millisecs, -td_millisecs, abs(td_millisecs) =', td_millisecs, -td_millisecs,
      abs(td_millisecs))
print('td_secs + td_millisecs =', td_secs + td_millisecs)
print('td_days2.total_seconds() =', td_days2.total_seconds())
try:
    tde = td(days=1000000000)
except OverflowError as e:
    print(e)
print()


# date objects
today = dt.today()
print('Today is', today)
print('today.year, today.month, today.day =', today.year, today.month, today.day)
print('Last day of 2020 was', dt(2020, 12, 31))
print('dt.min, dt.max =', dt.min, dt.max)
tomorrow = dt.today() + td(days=1)
yesterday = dt.today() + td(days=-1)
print('Tomorrow:', tomorrow, 'Yesterday:', yesterday)
print('tomorrow - yesterday =', tomorrow - yesterday)
print('tomorrow > yesterday :', tomorrow > yesterday)
print('yesterday > today :', yesterday > today)
print('today >= today :', today >= today)
print('one year from now =', today.replace(year=2022))
print('today weekday =', today.weekday())
print('yesterday weekday =', yesterday.weekday())
print('day before yesterday weekday =', (yesterday - td_days2).weekday())
print()


# time objects
print(dir(tm))
print('tm.min, tm.max =', tm.min, tm.max)
t1 = tm(11, 29, 56)
print('t1 =', t1)
print('t1.hour, t1.min, t1.second =', t1.hour, t1.min, t1.second)
print('t1.resolution, t1.tzinfo =', t1.resolution, t1.tzinfo)
print('new t1 =', t1.replace(hour=16))
print('t1.utcoffset(), t1.dst(), t1.tzname() =', t1.utcoffset(), t1.dst(), t1.tzname())
print()


# timezone
print(dir(datetime.timezone))
print('timezone min:', datetime.timezone.min, 'max:', datetime.timezone.max)
print('datetime.timezone.utc =', datetime.timezone.utc)
india_time = datetime.timezone(td(hours=5, minutes=30))
print('India time:', india_time)
print('india_time.utcoffset(None) =', india_time.utcoffset(None))
print('india_time.tzname(None) =', india_time.tzname(None))
print()


# datetime objects
print(dir(dtm))
right_now = dtm.now(india_time)
print('Right now:', right_now)
print('Right now:', right_now.year, right_now.month, right_now.day, right_now.hour,
      right_now.minute, right_now.second, right_now.microsecond, right_now.tzinfo,
      right_now.fold)
# Operations similar to date object are also supported
print('Same time tomorrow:', right_now + td(days=1))

print('UTC now:', dtm.utcnow())
print('From timestamp India time:', dtm.fromtimestamp(time.time(), tz=india_time))
print('From timestamp UTC:', dtm.fromtimestamp(time.time(), tz=datetime.timezone.utc),
      '|', dtm.utcfromtimestamp(time.time()))
print('Combine:', dtm.combine(today, t1))
print('Combine with timezone:', dtm.combine(today, t1, india_time))
try:
    print('Diff from UTC:', right_now - dtm.utcnow())
except TypeError as e:
    print(e)
print('Diff from UTC:', right_now - dtm.fromtimestamp(time.time(), tz=datetime.timezone.utc))

print('Right now date:', right_now.date(), ' time:', right_now.time(), ' tz:', right_now.timetz(),
      ' utc offset:', right_now.utcoffset(), ' dst:', right_now.dst(),
      ' tzname:', right_now.tzname(), ' weekday:', right_now.weekday())
replaced_right_now = right_now.replace(hour=10)
print('Replaced right now:', replaced_right_now)
print('Replaced right now as UTC:', replaced_right_now.astimezone(datetime.timezone.utc))

print(right_now.strftime('%a, %d %B %Y %I:%M:%S %p %Z'))
dt1 = dtm.strptime('06-14-2021', '%m-%d-%Y')
dt2 = dtm.strptime('14-6-2021', '%d-%m-%Y')
print('dt1 =', dt1, '    dt2 =', dt2)

# ISO time, tzinfo etc. is not experimented with here. It can be done if needed by referring to
# https://docs.python.org/3.6/library/datetime.html
