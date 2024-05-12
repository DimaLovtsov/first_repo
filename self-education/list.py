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