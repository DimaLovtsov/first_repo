'''

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)

import random

print(random.randrange(30,100))

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]

print(random.choice(list1))
print(random.choice(list2))

random.shuffle(list1)
random.shuffle(list2)

print(list1)
print(list2)

print(random.random())

'''

# Square root calculation

import math
x = math.sqrt(9)

print(x)

a = math.ceil(5.01)
b = math.floor (5.01)

print(a)
print(b)

c = math.pow(3, 3)
print(c)

d = math.pi
print(d)

e = math.factorial(6)
print(e)