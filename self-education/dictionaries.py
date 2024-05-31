'''

#get access

classes = {
 'A':27,
 'B':24,
 'C':29
}
print("There is", classes[('B')], "people in that class" )

#add items

classes["D"] = 32
print(classes)

#del

classes = {
 'A':27,
 'B':24,
 'C':29
}

del classes['C']
print(classes)

#change items
classes['B'] = 33

print(classes)

for classe in classes:
    print(classes[classe])

print("Flats and people")

house = {
    1:3,
    2:1,
    3:4,
    4:2,
    5:3
}

print(house)

for flat in house:
    print("People in flat number", flat, ":", house[flat], "people")

#pop method

f2 = house.pop(2)
print(f2)
print(house)

f5 = house.pop(5)
print(f5)
print(house)

f2 = house.pop(2,3)
print(f2)
print(house)

#clear method

house.clear()
print(house)

#update method

a = {1:'one', 2: 'three'}
a1 = {2:'two'}

print(a)
a.update(a1)
print(a)

a2 = {3:'three'}
a.update(a2)
print(a)

#keys and values method

l = [(4, 'four'), (5, 'five')]
a.update(l)

print(a)

dictKeys = a.keys()


print(dictKeys)
print(a.values())

#get method

shifts = {"1":"6:00-14:00", "2":"14:00-22:00", "3":"22:00-6:00"}
print(shifts)

for shift in shifts:
    print(shift, shifts[shift])

text = input('Enter your shift: ')
print('Tomorrow I\'ll been working', shifts.get(text))

#popitem method

person = {'Name:':'Max', 'Age:': 35, 'Country:':"World"}
for data in person:
    print(data, person[data])

print(person.popitem())

person["Profession:"] = 'hacker'

print(person)

print(person.popitem())
print(person)

'''


#31.05.2024
#Revision of theory from 15.05.2024


# person_1_name = input("Enter the name of the 1-st person: ")
# person_1_age = input("Enter the age of the 1-st person: ")

# person_1_dict = {person_1_name, person_1_age}

# print(person_1_dict)


#converting from a list to a dictionary

colors = [["red", "green"], ["yellow", "purple"]]
colors_dict = dict(colors)
print(colors)
print(colors_dict) #{'red': 'green', 'yellow': 'purple'}

for key_color in colors_dict:
    print(key_color, "\t -",  colors_dict[key_color])   #red      - green
                                                        #yellow   - purple


#adding elements to a distionary

colors_dict["orange"] = "blue"
print(colors_dict) #{'red': 'green', 'yellow': 'purple', 'orange': 'blue'}

#changing the elements
colors_dict["orange"] = "yellow"
print(colors_dict) #{'red': 'green', 'yellow': 'purple', 'orange': 'yellow'}

#changing the keys
colors_dict = {'red':'green', 'yellow':'purple', 'orange':'blue', 'red':'blue'}
print(colors_dict) #{'red': 'blue', 'yellow': 'purple', 'orange': 'blue'}


#updating 
grades_positive = {"A":"90", "B":"75-89", "C":"60-74"}
print(grades_positive)
grades_new = {"A+":"95-100", "D":"51-59"}
grades_positive.update(grades_new)
print(grades_positive) #{'A': '90', 'B': '75-89', 'C': '60-74', 'A+': '95-100', 'D': '51-59'}


#del pop clear
del grades_positive["D"]
print(grades_positive) #{'A': '90', 'B': '75-89', 'C': '60-74', 'A+': '95-100'}

mark = grades_positive.pop("A+")
print(mark) #95-100 returns the value of the key
print(grades_positive) #{'A': '90', 'B': '75-89', 'C': '60-74'}

grades_positive.clear()
print(grades_positive) #{}


#in get

sounds = {"cat":"meow", "dog":"woof", "lion":"roar"}
print("meow" in sounds) #False in refers to the key
print("dog" in sounds) #True
print("roar" in sounds) #Fals
print(sounds["cat"])
print(sounds.get("dog", "dog is not in a dictionary")) #woof , get is used to avoid errors in dictionary
print(sounds.get("cow", "cow is not in a dictionary"))


#keys values setdefault

print(sounds.keys()) #dict_keys(['cat', 'dog', 'lion'])
sounds_values = sounds.values()
print(sounds_values) #dict_values(['meow', 'woof', 'roar'])
print(type(sounds_values)) #<class 'dict_values'>
sounds_values_list = list(sounds_values) #['meow', 'woof', 'roar']
print(sounds_values_list)
print(type(sounds_values_list)) #<class 'list'>
print(list(sounds_values)) #['meow', 'woof', 'roar']

sounds_add = sounds.setdefault("bird", "whistels")
print(sounds)
