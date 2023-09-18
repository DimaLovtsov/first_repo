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


# while True:
#     try:
#         work_experience = (input("Enter your full work experience in years: "))
#         work_experience = float(work_experience)

#         if work_experience > 1 and work_experience <= 5 :
#             developer_type = "Middle"
#         elif work_experience <= 1 :
#             developer_type = "Junior"    
#         else:
#             developer_type = "Senior"


#         print(developer_type)
#     except ValueError:
#         print(input(f"Enter the number {work_experience} not with a comma only using a point. Example: 0,5 is wrong, 0.5 is correct. "))
#         continue

#     break

# print("Thank you.")


#Ex 8

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0

# for ch in message:
#     if ch == search:
#         result += 1
    
# print(result)

#Ex 9

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = first if first < second else second
# print(gcd)

#10


# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     for i in range(num + 1):
#         sum += i 
#         print(sum)
       

# print("Bye!")

sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
           
    for i in range(num + 1):
        sum = sum + i
        print(sum)
        num = int(input("Enter integer (0 for output): "))
print("Bye")