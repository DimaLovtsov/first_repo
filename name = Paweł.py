age = " I'm 34 "
print(age)

age = f'2+2'
print(age)

city1 = 'Kryvyi'
city2 = 'Rih'
city = f"My city is {city1} {city2}"
print(city)

miasto = input("Ваше місто: ")
tryb = input("Вас цікавлять заняття онлайн чи оффлайн: ")
czas = input("Ви бажаєте займатися зранку, вдень чи ввечері: ")

wroclaw = "У Вроцлаві у нас зараз є такі варіанти: "
poznan = "На даний момент у Познані ми можемо вам запропонувати тільки:  "

if miasto == "Вроцлав": print(wroclaw)  
if miasto == "Познань": print(poznan)
