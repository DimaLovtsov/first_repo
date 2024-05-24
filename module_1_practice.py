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

'''
user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")
'''

'''
n = int(input())
out = []
for i in range(n):
    k = 0
    while k < i + 1:
        out.append(i+1)
        k += 1
    if len(out) > n:
        break
out = out[0:n]
for i in out:
    print(i, end = " ")
'''
# a = int(input("Enter 'a': " ))
# b = int(input("Enter 'b': " ))

# print("The result is: ", a * b)

a = 'Python' 
b = str(3)
print(a +' '+ b)

c = 5
d = c

print(c, d)
print(id(c))
print(id(d))

e = 10
f = e
print(e is f)
print(id(e), id(f))

f = 11
print(e is f)
print(id(e), id(f))

print(type(e))
print(type(a))



             