
# num = int(input("Number: "))

# n1 = num // 100
# n2 = num % 10

# if n1 == n2:
#     print("Yes")
# else:
#     print("No") 

# num = input("Number: ")

# if len(num) != 3 :
#     print ("Please enter 3 numbers")
# else:
#     n1 = int(num[0])
#     n2 = int(num[1])
#     n3 = int(num[2])

#     if n1 != n3 and n2 != n3 and n2 != n1:
#         print("All the digits are different")

#     elif (n1 == n3 or n2 == n3 or n2 == n1) and not (n1 == n2 and n1 == n3):
#         print("There are only two digits are the same")

# month = 3
# match month:
#     case 3 | 4 | 5:
#         season = "spring"
#     case 6 | 7 | 8:
#         season = "summer"
#     case 9 | 10 | 11:
#         season = "automn"
#     case 12 | 1 | 2:
#         season = "winter"
# print(season)

#У банк поклали 100 долларів аід 5% річних. Обчислити 10 років

# deposit = 100
# percent = 0.05
# T = 10

# for year in range(1, T + 1)
#     new_deposit = deposit*(1 + percent / 12) ** 12
#     deposit = new_deposit
# print(deposit)

# print(deposit * (1 + percent / 12) ** (12*10))

# num = int(input("Enter the number from 0 to 100: "))
# sum = 0
# counter = 0

# while counter < num:
#     counter += 1
#     sum += counter
#     print(f"{sum}")

# for num in range (0,5):
#     print(num)

# for num in range (0,30,3):
#     print(num)

# for symbol in "Good morning":
#     print(symbol) 

# play_today = input("Max, are you going to play Dota today? ")
# game = True if play_today == "yes" else False
# print("Saturday is nice" if game else "bad")


'''
def format_ingredients(items):

    a = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
    new_items = a.pop(-1)
    a.append('and')
    a.extend(new_items)
    print(a)
    
    return a

items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
print(format_ingredients(items))

'''
'''

#If Ania has a day off

from datetime import date, datetime

a = datetime(2024, 5, 23)

b = datetime(2024, 7, 15)

print(a)
print(b)

result = b - a
print(result)

print("Step number 2: ")

from datetime import date, timedelta

first_date = date(2024, 5, 23)
duration = timedelta(days = 53)

for d in range(duration.days + 1):
    day = first_date + timedelta(days=d)
    print(day)

'''


'''

from datetime import date, timedelta

first_date = date(2024, 5, 23)
duration = timedelta(days = 60)


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
print(len(calendar_shifts))


for d in range(duration.days + 1):
    day = first_date + timedelta(days=d)
    print(day)
 
for shift in calendar_shifts:
    print(shift) 
       


#
       





#calendar_shifts = [(shift_night, day_off, shift_day, day_off)*5]
#for shift in calendar_shifts:
    
    
'''


def day_shift( day, shift):
    return day + ":" + shift

print(day_shift("23.05.2024", "night"))


def multiply(*numbers):

    result = 1
    for num in numbers:
        result *= num
    
    return result



print(multiply(3, 5, 10, 100))