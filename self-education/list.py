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

'''

#29.05.2024 Revision lists

#How to create a new list

a = [1, 2, 3, 4]
b = a.copy()
c = list(a)
d = a[:]

print(a, b, c, d)
print(a + b + c + d)

b[0] = 5
print(b)
print(a)

city = "Antananarivu"
city_list = list(city)  #
print(city_list)

city_list_join = "".join(city_list)  #['A', 'n', 't', 'a', 'n', 'a', 'n', 'a', 'r', 'i', 'v', 'u']
print(city_list_join) #Antananarivu

#SPLIT function

date = "12.06.2013"
date_list = date.split(".")
print(date_list)

many_slashes = "hi//there///how/are//you/doing/?"
print(many_slashes.split('/'))  #['hi', '', 'there', '', '', 'how', 'are', '', 'you', 'doing', '?'] #only one slash is splited, the other once " "
print(many_slashes)

#INDEX method

country = "Great Britain"
country_list = list(country)

position = country_list.index('G') + 1
print(position)

labels = ["Jack Daniels", "Baccardy", "Glen", "Red Label"]
rating = labels.index("Glen") + 1
print(rating)

#list of lists

number_list = [5, 7, 12]
word_list = ["Sun", "Moon", "Day", "Night"]
sign_list = ["/", ".", ":", "%"]

sum_list = [number_list, word_list, sign_list]

print(sum_list) #[[5, 7, 12], ['Sun', 'Moon', 'Day', 'Night'], ['/', '.', ':', '%']]
print(sum_list[2][3]) # % 
print(sum_list[1][2])

#change of elements
number_list[1] = 183
print(number_list)

#slicing

sum_list_slicing_1 = sum_list[0:1]
print(sum_list_slicing_1) #[[5, 183, 12]]

sum_list_slicing_2 = sum_list[0:2]
print(sum_list_slicing_2) #[[5, 183, 12], ['Sun', 'Moon', 'Day', 'Night']]

sum_list_slicing_3 = sum_list[1:3]
print(sum_list_slicing_3) #[['Sun', 'Moon', 'Day', 'Night'], ['/', '.', ':', '%']]

sum_list_slicing_4 = sum_list[::-1]  
print(sum_list_slicing_4) #[['/', '.', ':', '%'], ['Sun', 'Moon', 'Day', 'Night'], [5, 183, 12]]


    #0  1  2  3   4   5    6  7  8  9   10  11
x = [2, 4, 7, 9, 15, 204, 13, 3, 6, 11, 42, 18]

print(x[2:6]) #[7, 9, 15, 204]
print(x[7:10:2]) #[3, 11]
print(x[-2:-5:-1]) #[42, 11, 6]

#APPEND & INSERT methods

visited = ["Wroclaw", "Warsaw", "Krakow"]
visited.append("Lublin")
print(visited)

visited.insert(0, "Rumia")
print(visited)

visited.insert(3, "Gdansk")
print(visited)

#Extend method

group_1 = ["Girl 1", "Girl 2", "Girl 3"]
group_2 = ["Boy 1", "Boy 2", "Boy 3"]

group_1.extend(group_2)
print(group_1) #['Girl 1', 'Girl 2', 'Girl 3', 'Boy 1', 'Boy 2', 'Boy 3']
group_2.extend(group_1)
print(group_2) #['Boy 1', 'Boy 2', 'Boy 3', 'Girl 1', 'Girl 2', 'Girl 3', 'Boy 1', 'Boy 2', 'Boy 3']


#   DELETE, REMOVE, POP methods
print(group_1[3:6])
del group_1 [3:6] #['Boy 1', 'Boy 2', 'Boy 3']
print(group_1) #['Girl 1', 'Girl 2', 'Girl 3'] after str 415

days = ["Mon", "Tue", "Wed", "Thurth", "Friday","Satur", "Sun"]
weekend_days = days.pop(-1) + days.pop(-1)
print(days) #['Mon', 'Tue', 'Wed', 'Thurth', 'Friday']
print(weekend_days) #SunSatur

days.remove("Tue")
print(days) #['Mon', 'Wed', 'Thurth', 'Friday']

#IN NOT IN

grades = [87, 69, 95, 51, 63, 77, 49]
print(69 in grades) #True
print(77 not in grades) #False

#LEN

print(len(x))
print(len(grades))

#SORT SORTED methodes

letters = ["a", "f", "d", "k", "y", "b", "e", "c"]

letters_sorted = sorted(letters)
print(letters_sorted)

letters.sort()
print(letters)

letters.append("m")
print(letters_sorted) #['a', 'b', 'c', 'd', 'e', 'f', 'k', 'y', 'm']
print(letters) #['a', 'b', 'c', 'd', 'e', 'f', 'k', 'y']

letters.sort(reverse=True)
print(letters) #['y', 'm', 'k', 'f', 'e', 'd', 'c', 'b', 'a']

#RANGE

game_result = list(range(0,101))
print(game_result)

game_result_10 = list(range(0,101,10))
print(game_result_10)

print(min(game_result_10))
print(max(game_result))
print(len(game_result))
print(sum(game_result))
print(sum(game_result_10))

net, passw = 'netia', '123'
print(net)
print(passw)

letters = [3.14, 'inch', 2.14, 'inch', True]
letters.remove('inch')
print(letters)


'''

#Exercices 4.17.2
#Exercice 2

vehicles = ['car', 'bus', 'moto', 'bike']
print("I'd like to bye a", vehicles[3],".")


#Exercice 3
#Create a list years_list that contains the year you were born and each subsequent
#  year up to your fifth birthday. For example, if you were born in 1995, the list will
# look like this: years_list = [1995, 1996, 1997, 1998, 1999, 2000]. Print the year in 
# which you turned 3 years old, from the years contained in the years_list. Remember,
# in the first year, you were 0 years old. Add one more year to the end of the list and
# print the list. In which of the years listed in years_list were you the oldest?

years_list = [1905, 1906, 1907, 1908, 1909, 1910]
years_list_3 = years_list[3]
print(years_list_3)
years_list.append(1911)
print(years_list)
print(years_list[-1])

#Exercice 4

things = ["wallet", "mirror", "umbrella"]
rain = things[2]
print(rain.capitalize())
print(things)
print(rain.upper())
print(things)
things.pop(-1)
print(things)

#Exercice 5

languages = ["Georgian", "Estonian", "Ukranian"]
small_letter = languages[2]
print(small_letter.lower())
languages.reverse()
print(languages)
big_letter = languages[0].upper()
#print(big_letter.upper())
print(big_letter)
languages[0] = big_letter
print(languages)

#Exercice 6

internet = "Web", "Google", "DALLE", "Python"
internet_list = list(internet)
print(internet_list)

internet_tuple = tuple(internet)
print(internet_tuple)

internet_list[2] = "Windows"
print(internet_list)
#internet_tuple[2] = "Windows"

#Exercices 4.17.3

#Exercice 1

foreign_languages = ['Franch', "Ukranian", "Albanian", "German", "American English", "Polish"]
print(foreign_languages)
foreign_languages.reverse()
print(foreign_languages)
foreign_languages.sort()
print(foreign_languages)
print(sorted(foreign_languages))

#Exercice 2 v1

#numbers_user = input("Enter 4 numbers with spaces: " )

# numbers_user_list = list(numbers_user)
# print(numbers_user_list)

# while " " in numbers_user_list:
#     numbers_user_list.remove(" ")
    
# print(numbers_user_list)

# a = list(map(int, numbers_user_list))
# print(a)

# b = list(map(float, numbers_user_list))
# print(b)
#print(sum(a))

#Exercice 2 v2

#numbers_user_str = input("Enter 4 integers with spaces: " )

#split a string for different parties
# numbers_user_list = numbers_user_str.split()
# print(numbers_user_list)

# #convert a string to an integer
# list_int = list(map(int, numbers_user_list))
# print(list_int)

# #add all the elements
# list_sum = sum(list_int)

# print(list_sum)


#Exercice 3 v1

# cities = ["Paris", "Berlin", "Rome", "Vienna", "London", "Sidney"]

# cities0_4 = cities[0:5]
# print(*cities0_4, sep = ", ", end = " ") 
# print("and " + cities[-1])


#Exercice 3 v2

# cities = ["Paris", "Berlin", "Rome", "Vienna", "London", "Sidney"]

# print(', '.join(cities[0:5]) + " and " + cities[-1])

# #Exercice 3 v3

# cities_str = input("Enter 6 cities without a space but whith comma: ")
# print(cities_str)
# a = cities_str.split(',')
# print(a)

# print(", ".join(a[0:5]) + " and " + a[-1] + ".")


#Exercice 4
# numbers = input("Enter 5 numbers with one space between them: ")

# num_list = list(numbers.split(" "))
# num_list_copy = num_list.copy()

# num_list_copy.sort()

# print(num_list_copy)

# num_list_copy.reverse()
# print(num_list_copy)


#Exercice 5

#1.Create a list and convert to list

he_said = "Where are you from?"
he_said_list = list(he_said)
print(he_said) # Where are you from?
print(type(he_said)) #<class 'str'>
print(he_said_list) #['W', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 'f', 'r', 'o', 'm', '?']
print(type(he_said_list)) #<class 'list'>
print(he_said.split(" ")) #['Where', 'are', 'you', 'from?']
print(*he_said.split(" "), sep = "\n" ) #Where
                                        #are
                                        #you
                                        #from?


#2.lenght a list, join -> to convert a list into a string

rivers = ["Nile", "Amazon", "Congo", "Niger"]
print(len(rivers)) #4
print("-".join(rivers)) #Nile-Amazon-Congo-Niger

#3.slicing, index, changing elements

mountains = ["Everest", "K2", "Makalu"]
print(mountains[1:3]) #['K2', 'Makalu']
print(mountains[-1::-1]) #['Makalu', 'K2', 'Everest']
print(mountains.index("Everest"))  #0
mountains[-1] = "Karpacz"
print(mountains) #['Everest', 'K2', 'Karpacz']


#4. Append, insert, extend

states_1 = ["Columbia", "Arizona", "Texas", "Alabama", "Florida"]
states_2 = ["Hawaii", "Iowa"]

states_1_copy = states_1.copy()
states_2_copy = states_2.copy()

states_1.append(states_2)
print(states_1) #['Columbia', 'Arizona', 'Texas', 'Alabama', 'Florida', ['Hawaii', 'Iowa']]

state_a = "Newada"
state_b = "NY"

states_2.append(state_a)
print(states_2) #['Hawaii', 'Iowa', 'Newada']

states_2.insert(1, state_b)
print(states_2) #['Hawaii', 'NY', 'Iowa', 'Newada']

states_1.insert(2, states_2)
print(states_1) #['Columbia', 'Arizona', ['Hawaii', 'NY', 'Iowa', 'Newada'], 'Texas', 'Alabama', 'Florida', ['Hawaii', 'NY', 'Iowa', 'Newada']]

states_1_copy.extend(states_2_copy)
print(states_1_copy) #['Columbia', 'Arizona', 'Texas', 'Alabama', 'Florida', 'Hawaii', 'Iowa']
print(states_1[2][1]) #NY


#5 Delete Remove Pop

sizes = [46, 34, 45, 35, 44, 43, 36, 37, 39, 42, 38, 40]

del sizes [0:3]
print(sizes) #[35, 44, 43, 36, 37, 39, 42, 38, 40]

sizes.remove(42)
print(sizes) #[35, 44, 43, 36, 37, 39, 38, 40]

sizes.pop(3)
print(sizes) #[35, 44, 43, 37, 39, 38, 40]



#6 join split count 

birthdays = [12/12/2012, 11/11/2011, 15/5/2003, 30/4/1986, 26/2/2001, 2/11/2003]



# 7.Sort Sorted in not in revers
temperatures = [40.1, 27.2, 39.6, 14.0, -2.2, 23.8, -4.5]
temperatures.sort()
print(temperatures)
print(-2.2 in temperatures)
print(7 in temperatures)
temperatures.reverse()
print(temperatures)

temp_sort = sorted(temperatures)
print(temp_sort)

temperatures.remove(14.0)
print(temperatures)
print(temp_sort)


# 8. split remove _
nickenames = "a_l_e_x, f_e_l_i_c_i_a___"
nickname_list = nickenames.split("_")
print(nickname_list)

# 9. count min max

rolls = [1,2,3,4,5,6,7,8,9,10]
print(min(rolls))
print(max(rolls))
print(sum(rolls))


#6 join split count 

birthdays = ["12/12/2012", "11/11/2011", "15/5/2003", "30/4/1986", "26/2/2001", "2/11/2003"]
print(birthdays)
birthdays_str = " ".join(birthdays)
print(birthdays_str)
print(birthdays_str.split("/"))
print(birthdays_str.count("2003"))


#Exercice 6

keywords = ("for", "if", "else", "in", ":")

code = """for each token in the postfix expression : if the token is a number : print('Convert it to an integer and add it to the end of values')
else print('Append the result to the end of values')
"""
print(code)
