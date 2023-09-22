# Ex 1

# def greeting():
#     print('Hello world!')

# greeting()


# Ex 2

# def invite_to_event():
    
#     username = input("Write your name: ")
#     return username

# def invite(username):
#     print(f"Dear {username}, we have the honour to invite you to our event!")

# def main():
#     username = invite_to_event()
#     invite(username)

# main()

# def invite_to_event(username):

#     name_invite = f"Dear {username}, we have the honour to invite you to our event!"
#     return name_invite

# invite_to_event("Vasya")

# def invite_to_event(username):

#     name_invit = f"Dear {username}, we have the honour to invite you to our event"
#     return name_invit

# print(invite_to_event("username"))



# Ex 3



# a = 5
# b = 0


# def fun():
#     global a
#     a = 10
#     b = 2


# fun()
# print(a) 
# print(b)  



# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def calculate_trip_price(distance_km):

#     global total_trip
#     total_trip += 1

#     return base_rate + price_per_km * distance_km

# result = calculate_trip_price(10)
# print(result)


# Ex 4

# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x


# result = func_outer()
# print(result)


# def discount_price(price, discount):
#     def apply_discount():
        
#         nonlocal price
#         discount = price/int("100")
#         price -= discount

#     apply_discount()
#     return price


# result = discount_price(10, 1)
# print(result)


#Ex 5

# def get_fullname(first_name, last_name, middle_name=''):
#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     else:    
#         return f"{first_name} {last_name}"
    

#Ex 8

# def cost_delivery(quantity, *_, discount=0):
#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result

# print (cost_delivery(2, 1, 2, 3))


#Ex 9

def cost_delivery(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

print(cost_delivery.__doc__)


#Ex 10

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    a = factorial(n)  # a = n!
    b = factorial(n - k)  # b = (n - k)!
    c = factorial(k)  # c = k!

    return int(a / (b * c))  # n! / ((n - k)! · k!)
    # return int(factorial(n) / (factorial(n - k) * factorial(k)))  # n! / ((n - k)! · k!)


Ex 11 fibonacci


def fibonacci(n):
    
    if n == 0:
        return 0

    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(iterative_fibonacci(8))

