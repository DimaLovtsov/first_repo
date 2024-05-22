'''

#new

def greet():
    print("Hello")
    print("How do you do?")

greet()
'''

'''
def greet(name):
    print("Hello ", name)
        
greet(input("Enter your name: "))

        
# pass argument

'''

'''
def multiply_numbers(n1, n2):
    result = n1*n2
    print("The result is: ", n1, '*', n2, '=', result)

#n1 = 3
#n2 = 5

number_one = 4
number_two = 6

#multiply_numbers(n1, n2)
multiply_numbers(number_one, number_two)


def multiply_numbers(n1, n2):
    result = n1*n2
    return result

n1 = 3
n2 = 5
result = multiply_numbers(n1, n2)


print('The return result is: ', result)


'''
'''

print("Example 4")
def multiply_numbers(n1, n2):
    result = n1*n2
    return result

result1 = multiply_numbers(2, 7)
result2 = multiply_numbers(3, 8)
result3 = multiply_numbers(4, 9)

print('The result 4 is: ', result1)
print('The result 4 is: ', result2)
print('The result 4 is: ', result3)

'''


#Example 5  
#You have 5 marks. You need to 1) find an average score, 2) based the average to A,B,C or D


''''''
'''
# find the average marks and return it
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)
    
    average_marks = sum_of_marks/number_of_subjects
    
    return average_marks

# compute grade and return it
def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
grade =compute_grade(average_marks)

print("Your average marks is", average_marks)
print("Your grade is", grade)
'''
#??? how do input marks???
'''
empty_marks = []
mark = 0

while mark <5:
    print(input("Enter your mark: "))
    empty_marks.append(mark)
    mark += 1

marks = empty_marks
'''
'''
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    num_of_marks = len(marks)
    average_marks = sum_of_marks/num_of_marks

    return average_marks



def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = "A"
    elif average_marks >= 60.0:
        grade = "B"
    elif average_marks >= 50.0:
        grade = "C"
    else:
        grade = "F"

    return grade


marks = [90, 90, 90, 95, 92]

average_marks = find_average_marks(marks)
grade = compute_grade(average_marks)

print(average_marks)
print(grade)

'''


'''
#Exercise
#Can you create a program to add and multiply two numbers?
#For this, create two functions add_numbers() and multiply_numbers(). These functions 
    #should compute the result and return them to the function call and should print 
    #from outside the function.

def add_numbers(num1, num2):
    result_sum = num1 + num2
    return result_sum


def multiply_numbers(num1, num2):
    result_multiply = num1*num2
    return result_multiply

num1 = 4
num2 = 8

result_sum = add_numbers(num1, num2)
result_multiply = multiply_numbers(num1, num2)

print("The sum is: ", result_sum)
print("The product is: ", result_multiply)
'''


'''
#Excercise
#Write a function to check if a given number is prime or not.
#Return True if the number is prime, otherwise return False.

def prime_number(num):
    if num <= 1:
        return False
    elif num <=3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        return True


num = int(input("Enter a number: "))
if prime_number(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')




def is_prime(n):
    if n <= 1:
        return False
    elif n <=3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        return True


num = 9
if is_prime(num):
    print (True)
else:
    print(False)
    '''


#Exercise
#calculate the simple interest

def simple_interest(principal, rate, time):
    calculation_simple_interest = (principal * rate * time) / 100
    final_amount = calculation_simple_interest + principal
    return (calculation_simple_interest, final_amount)



n = simple_interest(1000, 5, 2) 
print(n)