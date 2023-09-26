# num = [1, 2, 41, 3, 5, 41, 8]
# num.sort()
# print(num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[1:10:3]

print(odd_numbers)
print(even_numbers)
print(three_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[1:10:3]
numbers_copy = numbers[:]

print(odd_numbers)
print(even_numbers)
print(numbers_copy)


items_a = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
items_b = items_a[0, 1, 2]