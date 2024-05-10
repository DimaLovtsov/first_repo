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