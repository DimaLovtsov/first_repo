'''

name = input("Write your name: ")


if name == "Dima":
    print ("Correct!")
else:
    print ("Wrong name")



#selling alcohol

print("Hello, nice to meet you!")
age = int(input("How old are you: "))

if int(age) >= 18:
    print("Fine! You can buy our products.")
elif int(age) >= 16:
    print("You don't have the full acsess but you can buy some products.")
else:
    print("Sorry! Come back when you will be 16 y.o. at least.")

#courses

print("Hello! Before we start", end = " ")
country = input("tell us what is your country of origin?: ")

result = "We don't have any courses for russian citizens" if country == "Russia" else "Good"
print(result) 

#insta first lesson free

subscribe = False
comment = True

if subscribe == True and comment == True:
    print("Here is a free first lesson for you!")
else:
    print("Subscribe or comment our posts or do it both")

    '''

#student score

score1 = int(input("Enter your score for the listening: "))
if score1 >=50:
    if score1 >= 95:
        print("Excellent")
    elif score1 >= 90:
        print("Very good")
    elif score1 >= 75:
        print("Good")
    elif score1 >= 50:
        print("Satisfactory")

else:
    print("Fail. Sorry, try the exam again")

#number positive

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")



    