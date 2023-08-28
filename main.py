print("Hello World")
print("Hello Git")
print("Привіт, Діма. Як справи?")

s1 = "Hello,"
s2 = " World!"
joined_string = s1 + s2
print(joined_string)
print(s1+s2)

name = 'Dima'
hello_string = f'Hello, {name}!'
print(hello_string)

name = input("введіть своє ім'я: ")
print("Привіт, ", name, "!")

name = input("введіть своє ім'я: ")
print(f"Привіт, {name}!")

a = 3
b = 5
c = 2
x = a+b*c
print(x)


a = int(input('Введіть перше число: ')) 
b = int(input('Введіть друге число: ')) 
c = int(input('Введіть третє число: '))
s = a+b*c
print(s)

x = 5**2+2**3+10*10
print(x)

int(input('Введіть ваш вік: '))
# user_age = 15
user_age = 16
user_status = 'adult' #'adult' for users older 16
print(user_status)

namesurename = input("Введіть своє ім'я та прізвище: ")
print(f"Добрий день, {namesurename}! Напишіть, будь ласка, з якого ви міста?")
city = input("Моє місто: ")
print(f"Зараз в місті {city} в нас є два набори")