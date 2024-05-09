#07_if_else
'''
number_1 = int(input("Enter a number one: "))
number_2 = int(input("Enter a number two: "))
number_3 = int(input("Enter a number three: "))

if number_1 < number_2 and number_1 < number_3:
    result = number_2 * number_3
    
elif number_2 < number_1 and number_2 < number_3:
    result = number_1 * number_3
    
else:
    result = number_1 * number_2

print(result)
'''

while True:
    name = input('Who are you?')   
    if name != 'Joe':
        print("The wrong name.")
        continue
    if name == "Joe":
        break

print("'Hello, Joe.")

while True:
    password = input('What is the password? (It is a fish.)')
    if password != 'swordfish':
        print("You've entred the wrong password. Try again.")
        continue
    elif password == 'swordfish':
        print('Access granted.')
        break