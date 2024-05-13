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

mixed_list = ['Hello', -34, 'Java', True]
print('1.', mixed_list[-1])
mixed_list[1] = "Hi"
print('2.', mixed_list)
mixed_tuple = (1, 3, 4, 5)
mixed_tuple[1] = 100
print('3.', mixed_tuple)