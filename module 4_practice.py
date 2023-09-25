#Ex 1 

#У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення та повертає суму платежу наприкінці місяця.

payment = (input("Введіть платежі через кому: "))

def amount_payment(payment):
    
    
    list = [payment]

    s = 0

    for number in range(payment):
        if list[number] > 0:
            s += list[number]

    return(s)

amount_payment(3)
print(amount_payment)


def amount_payment(payment):
    
    list = [3, 4, -8, 2, 0, -1, 1]

    s = 0

    for number in range(list):
        if number > 0:
            s += number

    return(s)

amount_payment(3, 4, -8, 2, 0, -1, 1)
print(amount_payment)