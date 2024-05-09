print("Long time no see")
# assing value to weekend_offer variable 
weekend_offer = 'Would you like to have classes on Saturdays or Sundays?'
print (weekend_offer)
# assing value to new weekend_offer variable
weekend_offer = 'Choose one of those days: Saturday or Sunday'
print (weekend_offer)
weekdays, weekend, online = 'Tuesday and Thurthday', 'Saturday or Sunday', '2 times a week'
print(weekdays)
print(weekend)
print(online)
#import constant file
import constant
print(constant.PRICE_DARIA_WEEKDAYS)
print(constant.PRICE_DARIA_WEEKEND)
print("City:", "Rome")
int_number = 105
float_number = 3.2
new_num = int_number + float_number
print('Value:', new_num)
print('Datatype:', type(new_num))
age_1 = '35'
age_2 = 33
print(age_1, type(age_1))
print(age_2, type(age_2))
total_age = int(age_1) + age_2
print(total_age, 'Total age type: ' , type(total_age))

a = 'Fuck'
b = 0
d = 'ff'
e = str(b)
c = a + e + d
print(c)
print(type(b))

x = str(3)
y = int(4)
r = float(5)
print(x, y, r)

print('How old', end =' ')
print('are you?')

print('What', 'would', 'you', 'like?', sep = '_')
print('Be' + ' careful!')

Dima = 35
Ania = 33
print('The age of Dima is {} and the age of Ania is {}'.format(Dima,Ania))

num_1 = input('Enter a number of banknotes you have: ')
num_2 = input('Enter a sum of money you want to get in: ')

print('Your banknotes: ', num_1)
print('You"ve put: ', num_2)