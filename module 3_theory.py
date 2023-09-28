# def print_hello():
#     print("Hello")


# def calculate_sum():

#     print("Calculation")

#     x = 3
#     y = 5

#     return x + y

# x = 2
# print(x)   # name 'x'is not definded  Есть х (стр 9) , но он изолирован внутри функции (стр 5) и не выходит за ее пределы. Сначала интерпретатор
            # читает стр 1, внутрь не заходит. Потом стр 5, внутрь не заходит и не подозревает, что есть какой-то х, пока мы не вызовем функцию.
            # а если мы допишем стр 14, то будет на экране результат со стр 14.

# global существует, но стараемся не использовать его внутри local
# 
# 

'''
def calculate_sum():

    x = 3
    y = 5

    def inner_func():
        print(x)
        # x = 10
        print(x)

    inner_func()

    return x + y

calculate_sum()
'''

# def calculate_sum(x):
    
#     y = 3

#     return x + y

# calculate_sum(5)   #TypeError: calculate_sum() missing 1 required positional argument: 'x'  
#                     # Нужно обязательно при вызове указать в скобках аргумент, но не х, а его значение, например 5. Правильный вариант ниже.

# result = calculate_sum(5)
# print(result)

#Ex 5

# def fun(a, b=2, c=3):
#     return a + b * c

# result = fun(5)
# print(result)


