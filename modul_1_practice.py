#a = 1 + int('1')
#print(a)
#x = 22 + 22
#print(x)
#y = str('22') + str('22')
#print(y)

# x = input('Enter x: ')
# y = input('Enter y: ')
# z = x + y
# print(z)

# import math

# RADIUS = 6371.01

# lat1 = 50.45
# lon1 = 30.523

# lat2 = 51.5072
# lon2 = -0.1275

# distance = RADIUS * math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon1) - math.radians(lon2)))
# print(distance)

user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")
