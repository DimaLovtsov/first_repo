
'''
#Ex 1. 
#how many seconds in an hour?

to_do = input("Choise '1' if you want to transfer minutes to seconds \
or '2' if you want to transfer hours to seconds. Enter 'stop' to quit the program: ")


while True:
    if to_do == "1":
        message_1 = input("Enter the number of minutes: ")
        if message_1 == "stop":
            print("bye")
            break
        result_1 = float(message_1) * 60
        print(f"There is {result_1} seconds in {message_1} minutes")
        

    elif to_do == "2":
        message_2 = input("Enter the number of hours: ")
        if message_2 == "stop":
            print("bye")
            break
        result_2 = float(message_2) * 60 * 60
        print(f"There is {result_2} seconds in {message_2} hours")

    elif to_do == "stop":
        print("Ok then. Bye.")
        break

    else:
        print("You've entred invalid date.")
        break

    continue
'''

'''
#Ex2
#min to hours, to days, etc

input_text = float(input("Enter the number of hours: "))
second_per_hour = input_text * 60 * 60
print("There is secoconds in hour: ", second_per_hour)
        
second_per_day = second_per_hour * 24
print("There is secoconds in day: ", second_per_day)

day_devide_hour = (second_per_day / second_per_hour)
print("Day devides by hour: ", day_devide_hour)

day_devide_hour = (second_per_day // second_per_hour)
print("Day devides by hour: ", day_devide_hour)
'''

# Ex 3.8

favorite = 7
print(favorite)

name_start = "David"
print(name_start.upper())
print(name_start.lower())
print(name_start.swapcase())

poem = '''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''

print(poem[:15])
print(len(poem))
print(poem.startswith("Yes"))
print(poem.endswith("I shall live!"))
print("I shall live!" in poem)

word = ","
print(poem.find(word))
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())
print(poem.isalpha())