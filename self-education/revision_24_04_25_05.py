#print(int(True))
#print(int(False))

#float to integer
'''
print(int(3.06))
a = 5.52
print(type(a))
b = 4.03
print(type(b))
c = a + b
print(c)
print(type(c))
d = int(a + b)
print(d)
print(type(d))

e = -5.7
print(type(e))
f = -10.1
print(type(f))
g = e + f
print(g)
print(type(g))
print(int(g))

'''
'''

#string with numbers to integer

a = '230'
print(type(a))

b = '120'
print(type(b))

c = a + ' ' + b
d = a + b
print(c)
print(type(c))
print(d)
print(type(d))

e = int(a+b)
print(e)
print(type(e))

f = int(a)
g = int(b)

h = f + g

print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))

'''
'''

#to float

a = 3
print(a)
print(float(a))

b = '35'
c = float(b)
print(b)
print(type(b))
print(float(b))
print(type(c))

'''
'''

#a = -28
#print(abs(a))

#printing differences

#nr_1

info = ('What', 'is', 'your', 'name')

word = ' '
for i in info:
    word += i + ' '
print(word) #What is your name

#nr_2

info = ('What', 'is', 'your', 'name')

word = ' '
for i in info:
    word += i + ' '
    print(word) #What
                #What is
                #What is your
                #What is your name


number = 30
words = "seconds to Mars"
print(str(number) + words)  # 30seconds to Mars

first_name = input("Enter your first name: ")
print(first_name)
last_name = input("Enter your last name: ")
print(last_name)
print(first_name, last_name)
'''


'''
print("How are you", end= ' ')
print('doing?')

name = 'Joe'
age = 23
country = 'USA'
salary = 100.2

print(f"This is {name}. He is {age} years old. He came from {country} where his salary was {salary} per year.")

print('{} {} {} {}'.format(name, age, country, salary)) #Joe 23 USA 100.2
print('{3} {0} {2} {1}'.format(name, age, country, salary))  #100.2 Joe USA 23

print('{0:s} {1:d} {2:s} {3:f}'.format(name, age, country, salary))   #Joe, 23, USA, 100.200000
#print('{0:s} {1:s} {2:s} {3:s}'.format(name, age, country, salary))

s_1 = "Start"
d = 2
s_2 = "Speak"
print('{0:*^79}'.format(' The end '))
print('{0:<10} {1:^10} {2:>10}'.format(s_1, d, s_2))
'''

'''
#f-string

a = 6
b = 10
print("a + b =", a + b)
print(f'a + b = {a+b}')

print("Are\nyou\nokay\nor\nnot?")

name, age, country = "John", 25, "USA"
print(name)
print(age)
print(country)

print("Are you okay or not?", 2, 5, 20, "Do you hear me?", 100, sep = "!")

print("Are\vyou\nokay\vor\nnot?")
'''

'''
desire = "I want to rest"
direction = 'abroad!'

for i in range(3):
    print(desire, end = " ")
    print(direction)

a = 'Wroclaw'
print(a[:])
print(a[0])
print(a[1])
print(a[-1])
print(a[2:6])
print(a[::2])
print(a[-4:-2])
print(a[::1])
print(a[::2])
print(a[::3])
print(a[::4])
print(a[::-1])
print(a[-2::-2])
 
'''


'''
print(len('Create a function that takes a String as an argument.'))

a_letter = 'Create a function that takes a String as an argument.'

print(a_letter.count("a"))
print(a_letter.count("t"))
print(a_letter.count("b"))

print(len(str(545233767684354552778278572841676545432277)))
545233767684354552778278572841676545432277

to_do = "wake up at 7 am, do gimnastique, make some tea, learn programming language"
print(to_do.split(','))
'''

#first_number = float(input("First: "))
#second_number = float(input("Second: "))
#print("Sum: ", first_number + second_number)

'''
#methods of the string

example = 'create a function that takes a String as an argument. then just wait. after that you can rest.'
print(example.capitalize()) # Create a function that takes a String as an argument. then just wait. after that you can rest.'  #Only the first character is capitalized
example_2 = 'Create A Function That Takes a String as an Trgument. Then just wait. After That You can Rest.'
print(example_2.casefold()) #all the letters are small
print(example.upper()) #all the letters are capitalized
print(example.count("a")) # count a certain sign #3 (Create, funCtion, Can)
print(example.find("t"))
print(example.title()) #every new word starts with uppercase
#print(example.translate())
'''
a = "Meow meow"
print(a.ljust(40), a.rjust(0))
print(a.center(40))
print(a.rjust(40))
print(a.center(40))
print(a.rjust(40))
print(a.ljust(40))
print(a.center(40))

info = 'Create a function that takes a String as an argument. then just wait. after that you can rest.' 
print(info.replace("Create", "Delete"))

a = "meowmeow"
b = "meowmeowmeowmeow"
c = a+b
print(c)
print(a*3)

text = "I'd like to travel to Shanghai"
print(text[0:21])
print(text[:21])
print(text[22:])
print(text[12:18])
print(text.upper())
print(text.upper().lower())
print(text.split())


    

   
