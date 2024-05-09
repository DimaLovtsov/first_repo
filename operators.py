print("How old ", "\n")
print("\t are you?")

a = 3
b = 3

print(" a == b =", a == b)
print(" a != b =", a != b)
print(" a < b =", a < b)
print(" a > b =", a > b)
print(" a <= b =", a <= b)
print(" a >= b =", a >= b)

a = 7
b = 2

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a ** b = ", a ** b)
print("a % b = ", a % b)
print("a // b = ", a // b)

a = 20
b = 3

print(a//b)
print(a % b )


#assignment opearators

weekday = 444
weekend = 480
#weekday += weekend
#print(weekday)

weekend -= weekday
print(weekend)

print(True and True)
print(True and False)
print(False and False)

print(True or False)
print(False or True)
print(False or False)

print(not False)
print(not True)

#Identity

a = "Why not?"
b = "Why not"

print(a)
print(b)
print(a is b)

#Identity

a = "Why not?"
b = "Why not?"

print(a)
print(b)
print(a is b)

#membership / in  not in

name = 'Dima'
print(name)
print("i" in name)

name = input("Enter your name?" )
print(name)
print("i" in name)

#task 1 -- km to miles

km = 0.621371
kilometer = float(input("Enter kilometers: "))
distance = kilometer*km
print("The distance in miles is: ", distance)

print(min(21, 156, 16, 45))