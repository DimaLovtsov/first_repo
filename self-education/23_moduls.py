#Exercice 1
#Create a module "module_invite" and save it as a modul (file "module_invite")
#import the module "module_invite"

# import module_invite

# one = input("Enter the person one: ")
# two = input("Enter the person two: ")

# result = module_invite.invite(one, two)

# print(result)


import calendar

print(dir(calendar))

#['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError',
#  'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar',
#  'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 
# 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__',
#  '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth',
#  '_get_default_locale', '_locale', '_localized_day', '_localized_month', 
# '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime',
#  'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format',
#  'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr',
#  'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek',
#  'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']

from calendar import day_name

n = 1
for day in day_name:
    print ("Day", n, "-", day)
    n += 1

from datetime import date, timedelta
d_1 = date(2024, 6, 11)
print(d_1)

d_2 = date(2024,7,15)
print(d_2)

all_d = d_2 - d_1
print(all_d)


first_day = date(2024, 6, 11)
duration = timedelta(days=34)


for d in range (duration.days + 1):
    day = first_day + timedelta(days=d)
    print(d + 1, ")", day)


shift_day = ['day', 'day', 'day', 'day']
shift_night = ['night', 'night', 'night', 'night']
day_off = ['day off', 'day off']

calendar_shifts  = []

#Cycle number 1. There are 5 cycles in total.

for shift in range(5):
    calendar_shifts.extend(shift_night)
    calendar_shifts.extend(day_off)
    calendar_shifts.extend(shift_day)
    calendar_shifts.extend(day_off)
    shift += 1

print(calendar_shifts)