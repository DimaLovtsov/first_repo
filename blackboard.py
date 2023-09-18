
# num = int(input("Number: "))

# n1 = num // 100
# n2 = num % 10

# if n1 == n2:
#     print("Yes")
# else:
#     print("No") 

# num = input("Number: ")

# if len(num) != 3 :
#     print ("Please enter 3 numbers")
# else:
#     n1 = int(num[0])
#     n2 = int(num[1])
#     n3 = int(num[2])

#     if n1 != n3 and n2 != n3 and n2 != n1:
#         print("All the digits are different")

#     elif (n1 == n3 or n2 == n3 or n2 == n1) and not (n1 == n2 and n1 == n3):
#         print("There are only two digits are the same")

# month = 3
# match month:
#     case 3 | 4 | 5:
#         season = "spring"
#     case 6 | 7 | 8:
#         season = "summer"
#     case 9 | 10 | 11:
#         season = "automn"
#     case 12 | 1 | 2:
#         season = "winter"
# print(season)

#У банк поклали 100 долларів аід 5% річних. Обчислити 10 років

# deposit = 100
# percent = 0.05
# T = 10

# for year in range(1, T + 1)
#     new_deposit = deposit*(1 + percent / 12) ** 12
#     deposit = new_deposit
# print(deposit)

# print(deposit * (1 + percent / 12) ** (12*10))

# num = int(input("Enter the number from 0 to 100: "))
# sum = 0
# counter = 0

# while counter < num:
#     counter += 1
#     sum += counter
#     print(f"{sum}")

# for num in range (0,5):
#     print(num)

# for num in range (0,30,3):
#     print(num)

# for symbol in "Good morning":
#     print(symbol) 

play_today = input("Max, are you going to play Dota today? ")
game = True if play_today == "yes" else False
print("Saturday is nice" if game else "bad")