#Ex 1 

#У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення та повертає суму платежу наприкінці місяця.

# payment = (input("Введіть платежі через кому: "))

# def amount_payment(payment):
    
    
#     list = [payment]

#     s = 0

#     for number in range(payment):
#         if list[number] > 0:
#             s += list[number]

#     return(s)

# amount_payment(3)
# print(amount_payment)


# def amount_payment(payment):
    
#     list = [3, 4, -8, 2, 0, -1, 1]

#     s = 0

#     for number in range(list):
#         if number > 0:
#             s += number

#     return(s)

# amount_payment(3, 4, -8, 2, 0, -1, 1)
# print(amount_payment)

#правильний варіант нижче

# def amount_payment(payment):
#     s = 0
#     for number in payment:
#         if number > 0:
#             s += number
#     return s

# my_list = [3,4,5, -1]
# print(amount_payment(my_list))


#Ex 2

# При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. 
# Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, 
# сортує його в порядку зростання і повертає змінений список як результат.


# value_list = [5, 27, 269, 8, 1, -126, 12, 22, 18]
# value_list.sort()
# print(value_list)

# first = value_list.pop(0)
# second = value_list.pop()

# print(first)
# print(second)

# result = value_list
# print(result)

# min = value_list[0]
#     max = value_list[0]
#     first = a.pop(a)
#     second = a.pop(a)

#     return(a)

# print(prepare_data(1))

# def prepare_data(data):

#     value_list = [5, 27, 269, 8, 1, -126, 12, 22, 18]
#     value_list.sort()
#     print(value_list)

#     first = value_list.pop(0)
#     second = value_list.pop()

#     return value_list

# print(prepare_data(1))

# def prepare_data(data):

#     data = []

#     first = data.pop(0)
#     second = data.pop()

#     return data

# print(prepare_data(1))

#правильне рішення завдання 2

# def prepare_data(data):

#     data.remove(min(data))
#     data.remove(max(data))
#     new_data = sorted(data)
#     return new_data

# data = [5, 27, 269, 8, 1, -126, 12, 22, 18]
# print(prepare_data(data))


# Ex 3. Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, а перед останнім ставимо союз "and", як у прикладі нижче:

# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar
# Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.

# def format_ingredients(items):
    
#     items_a = ", ".join(items[0:-1]) + ' and ' + items[-1]
#     return(items_a)

# a = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# print(format_ingredients(a))


def format_ingredients(items):

    a = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
    new_items = a.pop(-1)
    print(new_items)
    items_add = new_items.insert(3, 'and')
    list = items_add.extend(new_items)
    return list


print(format_ingredients(list))