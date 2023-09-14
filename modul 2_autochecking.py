# while True:

#     is_next = None
#     num = int(input("Enter your number of points: "))
#     if num >= 80:
#         is_next = True
#         print(is_next)
#         break
#     else:
#         is_next = False
#     print(is_next)
#     print("Try again.")

# print("You are the best!")


# num = float(input("Введіть число: "))
# while True:
#     if num > 0:
#         result = "Число додатнє"
#     elif num == 0:
#         result = "Це ноль"
#     else:
#         result = "Число від'ємне"
    
# print(result)



# try:
#     work_experience = float((input("Enter your full work experience in years: ")))
# except:
#     print("It's not a number")
while True:
    try:
        work_experience = (input("Enter your full work experience in years: "))
        work_experience = float(work_experience)

        if work_experience > 1 and work_experience <= 5 :
            developer_type = "Middle"
        elif work_experience <= 1 :
            developer_type = "Junior"    
        else:
            developer_type = "Senior"


        print(developer_type)
    except ValueError:
        print(input(f"Enter the number {work_experience} not with a comma only using a point. Example: 0,5 is wrong, 0.5 is correct. "))

    continue

    break

print("Thank you.")