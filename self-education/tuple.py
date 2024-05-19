var = 'hello'
print(type(var))

b = ("Hi",)
print(type(b))

#immutable
cars = ("BMW", "Tesla")
print(cars)
#cars[0] = "Nissan"
#print(cars)

#len, for in

number = (1,1,2,2,3,3)
print("Total number: ", len(number))
for num in number:
    print(num)

banknotes = (10, 20, 50, 10, 10, 5, 50, 200, 200, 50, 10, 200, 20, 100)
if 100 in banknotes:
    print("100 is in my banknotes")
else:
    print ("100 is not in my banknotes")

del banknotes
