def invite(guest_1, guest_2):
    x = "Dear {} and {}.".format(guest_1, guest_2)
    y = "We invite you!"
    return x + " " + y
    
one = input("Enter the person one: ")
two = input("Enter the person two: ")

print(invite(one, two))