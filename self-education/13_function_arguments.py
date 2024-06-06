'''

#Exercice 1

def full_name(first_name, last_name):
    print(first_name, last_name)

full_name(first_name = "John", last_name = "Doe")


#Exercice 2

def full_name(first_name, last_name):
    
    full_name = first_name + " " + last_name
    return full_name

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

result = full_name(first_name, last_name)
print(result)


#Exercice 3

def full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

def get_user_input():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

first_name, last_name = get_user_input()

result = full_name(first_name, last_name)
print(result)


#Exercice 4
def highest_digit(n):
   return max(list(str(n)))

print(highest_digit(12345))

'''

#Exercice 5

def evaluate_expression(expression):
    return eval(expression)

expression = "2 + 3 * 4 - 5"
print(evaluate_expression(expression))