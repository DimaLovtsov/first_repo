'''

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[:])
print(my_list[2:])
print(my_list[:3])
print(my_list[1:3])
print(my_list[::3])

#append

workdays = ['Mon','Thursday', 'Friday']
print(workdays)
workdays.append('Saturday')
print(workdays)

#insert 

animals = ['cat', 'dog', 'bear']
print(animals)
animals.insert(2, 'mouse')
print(animals)

i_took = ['phone', 'passport', 'money']
print(i_took)
i_took.insert(0, 'water')
print(i_took)

i_took = ['phone', 'passport', 'money']
print(i_took)
i_took.insert(1, 'water')
print(i_took)

i_took = ['phone', 'passport', 'money']
print(i_took)
i_took.insert(2, 'water')
print(i_took)

#extend

print("Let's add two lists with extend")

group_dasza = ['Ira', 'Nata', 'Nadia', 'Oleh', 'Vika']
group_diana = ['Ira', 'Aleks', 'Danil', 'Vero', 'Lesia']

group_dasza.extend(group_diana)
print(group_dasza)

print("Let's add two lists with append")

group_dasza = ['Ira', 'Nata', 'Nadia', 'Oleh', 'Vika']
group_diana = ['Ira', 'Aleks', 'Danil', 'Vero', 'Lesia']

group_dasza.append(group_diana)
print(group_dasza)

#Change List Items

numbers = [1, 2, 3, 4]
numbers[2] = 8
print(numbers)

#remove

numbers = [5, 10, 14, 16, 20]
numbers.remove(14)
print(numbers)

#len function 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Total letters: ", len(letters))

#pop

languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
print('Return Value:', languages.pop(-2))
print(languages)
print('Return Value:', languages.pop(-1))
print(languages)

number = [3, 6, 9, 12, 15]
print(number.pop(-3))
print(number)
print(number.pop(-2))
print(number)
print(number.pop(-2))
print(number)

#clear

prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.clear()
print('Here:', prime_numbers)

prime_numbers = [2, 3, 5, 7, 9, 11]
print(prime_numbers.clear())

# Operating System List
systems = ['Windows', 'macOS', 'Linux', '123', '456']
print('Original List:', systems)

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[3:1:-1]

# updated list
print('Updated List:', reversed_list)

'''
'''
mixed_list = ['Hello', -34, 'Java', True]
print('1.', mixed_list[-1])
mixed_list[1] = "Hi"
print('2.', mixed_list)
mixed_tuple = (1, 3, 4, 5)
mixed_tuple[1] = 100
print('3.', mixed_tuple)
'''

'''
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
print(months)
print(months[:])
print(months[3])
index = months.index("September")
print(index)
for month in months:
    print(month)

months[3] = "APRIL"
print(months)

months[3:6] = "APRIL", "MAY", "JUNE"
print(months)
print(months[::3])

months.remove("APRIL")
print(months)
print("Total: ", len(months))

months_ext = months.pop(8)
print(months_ext)
print(months)

months_ext_2 = months.pop(-1)
print(months)

del months[:7]
for month in months:
    print(month)

index = months.index("September")
print(index)
'''

'''
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
print(months)
months.sort()
print("Sorted list is: ", months)
months.sort(reverse=True)
print("Sorted revers is: ", months)

for month in months:
    print(month)

ages = [15, 14, 23, 45, 29, 45, 32, 29, 50, 45]
ages_29 = ages.count(29)
print(ages_29)
ages_45 = ages.count(45)
print(ages_45)

ages.sort()
print(ages)

for age in ages:
    if age < 17:
        print(age)
        
        print(ages)
        
print("Ages older 17: ", ages)
'''
'''
ages = [15, 14, 23, 45, 29, 45, 32, 29, 50, 45]
ages_29 = ages.count(29)
print(ages_29)
ages_45 = ages.count(45)
print(ages_45)

ages.sort()
print(ages)

ages_to_remove = 29

while ages_to_remove in ages:
    ages.remove(ages_to_remove)

print(ages)

under_17 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

while under_17 in ages:
    under_17.clear()

print(ages)
'''

'''
ages = [15, 14, 23, 45, 29, 45, 32, 10, 8, 29, 50, 45]

ages.sort()
print(ages)

while ages.count(45):
    ages.remove(45)


print(ages)
'''
'''
ages = [15, 14, 23, 45, 8, 12, 29, 45, 32, 10, 8, 29, 23, 50, 45, 16, 23, 14, 17, 17]

ages.sort()
print(ages)

ages_above_17 = []

for age in ages:
    if age < 17:
            continue
    else:
        ages_above_17.append(age)

print(ages_above_17)

'''
'''
#not finished
from collections import Counter
ages = [15, 14, 23, 45, 8, 12, 29, 45, 32, 10, 8, 29, 23, 50, 45, 16, 23, 14, 17, 17]

ages.sort()
print(ages)

age = Counter(ages)
   
age_multiply = [element for element, count in age.items() if count > 1]

ages = [age for age in ages if age not in age_multiply]

print(ages)
'''

'''
list = [3, 5, 8, 10]
list_power = [num**2 for num in list]
print(list_power)

list = [3, 5, 8, 10]
print(list)
list_plus = [num+5 for num in list]
print(list_plus)

list = [3, 5, 8, 10]
print(list)
list_less = [num>9 for num in list]
print(list_less)
'''
'''
list = [3, 5, 8, 10]
print(list)
list_less = [num for num in list if num > 8]
print(list_less)

ages = [15, 14, 23, 45, 8, 12, 29, 45, 32, 10, 8, 29, 23, 50, 45, 16, 23, 14, 17, 17]

ages.sort()
print(ages)
ages_above_16 = [age for age in ages if age > 16]
print(ages_above_16)
'''
'''
ages = [15, 14, 23, 45, 8, 12, 29, 45, 32, 10, 8, 29, 23, 50, 45, 16, 23, 14, 17, 17]
ages_above_16 = [age for age in ages if age > 16]
print(ages_above_16)

numbers_10 = [num for num in range (1, 100) if num // 10 == 2]

print(numbers_10)

print("0 is a girl, 1 is a boy")
children = [1, 0, 0, 0, 1, 1, 0]
children_boy_girl = ["Boy" if child % 2 == 1 else "Girl" for child in children]
children_boy_girl.sort()
print(children_boy_girl)

children_boy = [child for child in children if child == 1]

while children_boy.count(1)>0:
    children_boy[0] = "boy"

print(children_boy)

children_girl = [child for child in children if child == 0]
print(children_boy)
print(children_girl)
'''

print("0 is a girl, 1 is a boy")
children = [1, 0, 0, 0, 1, 1, 0]

children_set = set(children)
print(children_set)