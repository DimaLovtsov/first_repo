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


def discount_price(price, discount):
    def apply_discount():
        
        nonlocal price
        discount = price/int("100")
        price -= discount

    apply_discount()
    return price


result = discount_price(10, 1)
print(result)