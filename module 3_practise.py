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

def invite_to_event(username):

    name_invit = f"Dear {username}, we have the honour to invite you to our event"
    return name_invit

print(invite_to_event("username"))