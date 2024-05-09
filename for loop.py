#for loop
#I have coins in my pocket. I named them coins. 
coins = ["5 gr", "1 zł", "10 gr", "5 zł", "10 gr", "20 gr", "2 zł"]
for i in coins:
    print (i)

#Spell your name
name = "Monkey"
for i in name:
    print(i)


languages = ['Swift', 'Python', 'Go']
for language in languages:
    print('Hi, ', language,"!")


for i in range(6):
    # inner loop
    for j in range(6): 
        print(f'i = {i}, j = {j}')


number = 2
while number <= 100:
    print(number)
    number = number + 3

for x in range(3, 15):
    print(x)
    x += 3

#multiplication

number = int(input("Enter an integer: "))

for i in range(1, 11):
    new = number * i
    print(number, "*", i, "=", new)