#Exercice 1
#Factorial

def factorial(n):

    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))
    
num = int(input("Enter an integer: "))

print("The factotial of", num, "is", factorial(num))