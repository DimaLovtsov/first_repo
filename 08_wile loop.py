'''

#range

#Create a program which sums numbers from 1 to 100

storage = 0
for i in range(1, 101):
    storage = storage + i

print(storage)

#a power table

Input = int(input("Enter your number: "))

count = 0

while count <=5:
    Power = Input ** count
    print(Input, "**", count, "=", Power )
    count = count + 1

'''
'''
#a multiplication table reverse

Input = int(input("Enter a number lesser than 10: "))

count = 10

while count >=1:
    new = Input * count
    print(Input, "*", count, "=", new)
    count = count - 1

'''
'''

Input = int(input("Enter a number lesser than 10: "))

for count in range(1, 10):
    new = Input * count
    print(Input, "*", count, "=", new)

'''
'''
total = 0

for i in range (1, 11):
    total = total + i

total = int(total*2 - 10)
print(total)
'''
'''
count = 0

while count <= 10:
    print("Hello")
    count = count + 1
break
    '''

'''
print("Hi")

count = 0
for i in range (0, 11):
    count = count + i
for i in range (0, 10):
    count = count + i

print(count)
'''
'''
number = int(input("Enter a number within 0-10: "))

count = 1

while count <=10:
    multi = number * count
    print (multi)
    count = count + 1

number = int(input("Enter a number within 0-10: "))

for i in range (1, 11):
    multi = number * i
    print (multi)
'''
'''
# Calculate the sum of numbers until user enters 0

number = int(input('If you want to get a sum of numbers enter a number one by one. Then enter "0" to get a result: '))

total = 0

while number != 0:
    total += number
    number = int(input("Enter numbers: "))

print("The sum is", total)
'''
'''
while True:
    name = input("Enter your name: ")
    
    if name == "end":
        print(f'Bye')
        break

    print(f"Hi {name}")    
'''

#guess a number
'''
while True:
    number = input("Enter a number as many times as you guess: ")

    if number == "48":
        print(f"Congratulations! Your number {number} is guessed.")
        break

    if number > "48":
        print("The number is less.")
    
    if number < "48":
        print("The number is bigger.")

    print(f"TryAgain")
'''

while True:
    number = input("Enter a number as many times as you guess: ")

    if number > "67":
        print("The number is less.")

    elif number < "67":
        print("The number is bigger.")


    else:
        print(f"Congratulations! Your number {number} is guessed.")
        break
       
    print(f"Try again")