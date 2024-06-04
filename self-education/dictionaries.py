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

# 5.10 sets

vowels = "aou"
consonant = "vrdoflu"

vowels_set = set(vowels)
consonant_set = set(consonant)

print(vowels_set) #{'a', 'o', 'u'}
print(consonant_set) #{'r', 'v', 'f', 'o', 'd', 'l', 'u'}

#union, all the elements are here one time
vow_cons = vowels_set | consonant_set
print(vow_cons) #{'r', 'f', 'd', 'o', 'v', 'u', 'a', 'l'} , a repeated common element "ou"

#intersection, only the common elements
vow_cons_inters = vowels_set & consonant_set
print(vow_cons_inters) #{'o', 'u'}

#symmetric difference, without the common elements
vow_cons_sym = vowels_set ^ consonant_set
print(vow_cons_sym) #{'a', 'v', 'l', 'r', 'd', 'f'}

#difference, A-B, B-A
vow_con_sym_dyf_A_B = vowels_set - consonant_set
print(vow_con_sym_dyf_A_B) #{'a'}
vow_con_sym_dyf_B_A = consonant_set - vowels_set
print(vow_con_sym_dyf_B_A) #{'d', 'f', 'v', 'r', 'l'}



print("a" in vowels_set)
print(sounds["cat"])
#print(sounds["elephant"])



#Exercices 5.12.2

#Exercice 5.12.2.1

famous_person = {
    "first_name":"Nikola",
    "last_name":"Tesla" ,
    "century":"XIX",
    "progress":"wireless communication" 
    }

print(famous_person)
print(famous_person.keys())
print(famous_person.values())

for key in famous_person:
    print(key, "\t", famous_person[key])


#Exercice 5.12.2.2

name_numbers = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4
}


print("zero: ", name_numbers["zero"]) #zero:  0
print("one: ", name_numbers["one"])
print("two: ", name_numbers["two"])
print("three: ", name_numbers["three"])
print("four: ", name_numbers["four"])

name_numbers_list = list(name_numbers.items())
print(name_numbers_list)


#Exercice 5.12.2.4

public_transport_list = ["boat", "bus", "plane", "train"]
public_transport_set = set(public_transport_list)
print(public_transport_set)


#Exercice 5.12.2.4

who = ("cyclist", "driver", "pedestrian")
who_set = set(who)
print(who_set)


#Exercice 5.12.2.5

meal = {"breakfast":"coffee", "lunch":"milk", "dinner":"tea"}
meal_set = set(meal)
print(meal_set) #{'dinner', 'breakfast', 'lunch'}
meal_set_values = set(meal.values())
print(meal_set_values) #{'tea', 'coffee', 'milk'}
meal_set_items = set(meal.items())
print(meal_set_items) #{('dinner', 'tea'), ('breakfast', 'coffee'), ('lunch', 'milk')}



#Exercice 5.12.3.1

glossary = {
    "URL":"Universal resource locator, an easy-to-remember address for calling a web page.",
    "Wi-Fi":"A wireless method of sending information using radio waves.",
    "Programming":"The art of creating a program.",
    "Pixel":("Short for 'picture element', the fundamental unit of a digital image, "
        "typically a tiny square or dot that contains a single point of color of a larger image.")
}

print("URL", "\n", glossary["URL"],"\n", sep="")

print("Wi-Fi", "\n", glossary["Wi-Fi"], "\n", sep="")

print("Programming", "\n", glossary["Programming"],"\n", sep="")

print("Pixel", "\n", glossary["Pixel"],"\n", sep="")
    


#Exercice 5.12.3.2 v1
#Where runs the river

# message = (input("""To know where exactly runs the river enter:
#       1 for Amazon,
#       2 for Nile,
#       3 for Mississippi: """))

# regions = {"Amazon":"South America", "Nile":"Africa", "Mississippi":"North America"}

# if message == "1":
#     print("The Amazon runs through ", regions["Amazon"])
# elif message == "2":
#     print("The Nile runs through ", regions["Nile"])
# else:
#     print("The Mississippi runs through ", regions["Mississippi"])


#Exercice 5.12.3.2 v2
#Where runs the river

# regions = {"Amazon":"South America", "Nile":"Africa", "Mississippi":"North America"}

# regions_keys = list(regions.keys())
# print(regions_keys)

# regions_values = list(regions.values())
# print(regions_values)

# print("The {} runs through {}".format(regions_keys[0], regions_values[0]))
# print("The {} runs through {}".format(regions_keys[1], regions_values[1]))
# print("The {} runs through {}".format(regions_keys[2], regions_values[2]))


#Exercice 5.12.3.2 v3
#Where runs the river

# print("Exercice 5.12.3.2")
# regions = {"Amazon":"South America", "Nile":"Africa", "Mississippi":"North America"}

# regions_keys = list(regions.keys())
# regions_values = list(regions.values())

# for i in range (3):
#     print("The {} runs through {}".format(regions_keys[i], regions_values[i]))

# del regions["Amazon"]

# print(regions)


#Exercice 5.12.3.4 

e2g = {
    "stork":"storch",
    "hawk":"falke",
    "woodpecker":"specht",
    "owl":"eule"
}

print(e2g)
print(e2g.get("hawk", "It's not in a dictionary"))

for key in e2g.keys():
    print(key)  #stork
                #hawk
                #woodpecker
                #owl

for value in e2g.values():
    print(value)    #storch
                    # falke
                    # specht
                    # eule

#for key, value in e2g.items():
    #print(f"{key} - {value}")

e2g_items = e2g.items()
print("stork :", e2g["stork"])

e2g.update({"smok":"rauch", "spark":"funke"})

print(e2g) ##{'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule', 'smok': 'rauch', 'spark': 'funke'}


e2g_keys_list = list(e2g.keys()) 
print(e2g_keys_list) #['stork', 'hawk', 'woodpecker', 'owl', 'smok', 'spark']

e2g_values_list = list(e2g.values())
print(e2g_values_list) #['storch', 'falke', 'specht', 'eule', 'rauch', 'funke']


'''
#Exercice 5.12.3.6
#Morse alphabet

while True:

    letter = input("Enter a letter: ")

    alphabet_morse = {
        "a":".-",
        "b":"-...",
        "c":"-.-.",
        "d":"-..",
        "e":".",
        "f":"..-.",
        "g":"--.",
        "h":"....",
        "i":"..",
        "j":".---",
        "k":"-.-",
        "l":".-..",
        "m":"--",
        "n":"-.",
        "o":"---",
        "p":".--.",
        "q":"--.-",
        "r":".-.",
        "s":"...",
        "t":"-",
        "u":"..-",
        "v":"...-",
        "w":".--",
        "x":"-..-",
        "y":"-.--",
        "z":"--.."     
    }

    letter = letter.lower()

    if letter in alphabet_morse:

        print(alphabet_morse[letter])

'''

#Exercice 5.12.3.7





physics = ["nuclear physics", "optics", "thermodynamics"]
computer_science = "computer science"
biology = {}

science = physics, computer_science, biology
humanities = {}
public = {}

subjects = science, humanities, public


print(physics)


#print(subjects[science_dictionary])
#print(subjects['science']['physics'])
