
'''
#Exercice 1

greet = "Hello"

def greet_func():

    print("Global: ",greet) #Global:  Hello

greet_func()


#Exercice 1.1

greet = "Hello"

def greet_func():

    greet = "Hi"
    print("Local: ",greet) #Local:  Hi

greet_func()
'''

#Exercice 1.2

greet = "Hello Hello"

def greet_func():
    
    global greet
    greet = "Hi Hi"
    print("Local: ",greet)  #Local:  Hi Hi, NOT global Hello Hello

greet_func()
print(greet) #Hi Hi, because the line 32


#Exercice 1.3

greet = "Hello Hello"

def greet_func():
    
    #global greet
    greet = "Hi Hi"
    print("Local: ",greet)  #Local:  Hi Hi, NOT global Hello Hello

greet_func()
print(greet) #Hello Hello


#Exercice 2.1 nested local

def first():
    one_five = "fisrt 1-5"

    def second():
        one_five = "second 1-5"
        print(one_five) #second 1-5

    second()
    print(one_five) #fisrt 1-5

first()

#Exercice 2.2 nonlocal

def first():
    one_five = "fisrt 1-5"

    def second():
        nonlocal one_five
        one_five = "second 1-5"
        print(one_five) #second 1-5

    second()
    print(one_five) #second 1-5, because the line 74

first()