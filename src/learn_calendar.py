import calendar


print(dir(calendar))

this_year = calendar.calendar(2021)
print(this_year)

c = calendar.Calendar()
print('Weekdays:', [i for i in c.iterweekdays()])
print('Monthdates:', [i.strftime('%Y-%m-%d') for i in c.itermonthdates(2020, 2)])
print('Monthdays:', [i for i in c.itermonthdays(2021, 1)])
print('Monthdays2:', [i for i in c.itermonthdays2(2021, 6)])
print()
print('Monthdatescalendar:', [i.strftime('%Y-%m-%d') for i in c.itermonthdates(2021, 2)])
print('Monthdayscalendar:', [i for i in c.itermonthdays(2021, 2)])
print('Monthdays2calendar:', [i for i in c.itermonthdays2(2021, 2)])
print()
print('Yeardatescalendar:')
w = 0
for i in c.yeardatescalendar(2021, 2):
    for j in i:
        for k in j:
            print(w, list(map(lambda x: x.strftime('%Y-%m-%d'), k)))
            w += 1
print('Yeardayscalendar:')
for i in c.yeardayscalendar(2021, 4):
    for j in i:
        print(j)
print('Yeardays2calendar:')
for i in c.yeardays2calendar(2021, 6):
    for j in i:
        print(j)
print()

print('calendar.firstweekday() =', calendar.firstweekday())
print('calendar.isleap(2020) =', calendar.isleap(2020))
print('calendar.leapdays(2012, 2021) =', calendar.leapdays(2012, 2021))
print('calendar.weekday(2021, 6, 9) =', calendar.weekday(2021, 6, 9))
print('calendar.weekheader(8):', calendar.weekheader(8))
print('calendar.weekheader(2):', calendar.weekheader(2))
print('calendar.weekheader(9):', calendar.weekheader(9))
print('calendar.monthrange(2021, 6) =', calendar.monthrange(2021, 6))
print('calendar.monthcalendar(2021, 7):', calendar.monthcalendar(2021, 7))
print(calendar.month(2021,7))
print()

print(calendar.day_name)
print(calendar.day_abbr)
print(calendar.month_name)
print(calendar.month_abbr)
