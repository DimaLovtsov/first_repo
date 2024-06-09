#Exercice 1 v1
#Factorial with recursive function

# def factorial(n):

#     if n == 1:
#         return 1
#     else:
#         return (n * factorial(n - 1))
    
# num = int(input("Enter an integer: "))

# print("The factotial of", num, "is", factorial(num))



#Exercice 1 v2
#Factorial without a recursive function, only using for loop

# number = int(input("enter a number: "))
# result = 1 #start counting for factorial

# for i in range(1, number+1):
#     result *= i

# print(f"The factorial {number} is {result}")

#Exercice 2 v1
#Calculating steps FOR LOOP

# def walk(steps):
#     for step in range(1, steps + 1):
#         print(f"You take step #{step}.")
    
# walk(int(input("Enter steps: ")))   


#Exercice 2 v2.1
#Calculating steps Recursive down

# def walk(steps):
#     if steps == 0:
#         return
#     print(f'You take a step # {steps}')  #10, 9, 8...
#     walk(steps - 1) #10, 9, 8...

# walk(int(input("Enter steps: ")))


#Exercice 2 v2.2
#Calculating steps Recursive up

# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps - 1) 
#     print(f'You take a step # {steps}') 
    

# walk(int(input("Enter steps: ")))

'''Explanation

Condition if steps == 0::

This condition checks if the steps parameter is equal to zero.
steps is an argument to the function that indicates the number of steps to 
take return:

The return statement ends the execution of the current function and returns 
control back to the place where the function was called.
If no value is specified with return, the function returns None by default.
Role of return in the walk Function
In this context, return acts as the base case for the recursive function walk.
 The base case is essential to prevent infinite recursion and ensure that the
   function eventually terminates. Here's how it works:

Base Case:

When steps is equal to 0, the return statement is executed, and the function 
terminates for that specific call.
This stops further recursion and returns control back to the previous call of
 the function.
Recursive Case:

If steps is not 0, the function calls itself with the argument steps - 1.
Step-by-Step Example
Let's consider the call walk(3):

First call walk(3):

steps is 3.
The condition if steps == 0: is not met.
walk(2) is called.
Second call walk(2):

steps is 2.
The condition if steps == 0: is not met.
walk(1) is called.
Third call walk(1):

steps is 1.
The condition if steps == 0: is not met.
walk(0) is called.
Fourth call walk(0):

steps is 0.
The condition if steps == 0: is met.
The return statement is executed, and the current call walk(0) terminates,
 returning control back to walk(1).
After reaching the base case (steps == 0), the recursion starts to unwind:

Returning to walk(1):

The statement print(f'You take a step # {steps}') is executed, printing 
"You take a step # 1".
Returning to walk(2):

The statement print(f'You take a step # {steps}') is executed, printing 
"You take a step # 2".
Returning to walk(3):

The statement print(f'You take a step # {steps}') is executed, printing 
"You take a step # 3".

'''

#Exercice 3.1
#Febonacci sequence is slow if n > 40

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for n in range(1, 38):
#     print(n, ":", fibonacci(n))



#Exercice 3.2
#Febonacci sequence whit Memoization

fibonacci_memory = {}


def fibonacci(n):

    if n in fibonacci_memory:
        return fibonacci_memory[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_memory[n] = value
    return value
    
for n in range(1, 100):
    print(n, ":", fibonacci(n))