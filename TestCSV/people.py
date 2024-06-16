"""
import csv
import os

with open('people.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

        #['Name', '   Age', ' Profession']
        #['Jack', '   23', '  Doctor']
        #['Miller', ' 22', '  Engineer']


print(os.getcwd())


with open("people.csv", "r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

        #{'Name': 'Jack', '   Age': '   23', ' Profession': '  Doctor'}
        #{'Name': 'Miller', '   Age': ' 22', ' Profession': '  Engineer'}
"""

# import csv
# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer.writerow([2, "Harry Potter", "Harry Potter"])


# import csv

# with open("students.csv", "w", newline= "") as file:
#     student = csv.writer(file)
#     student.writerow(["Name", "Surname", "Age", "Sex"])
#     student.writerow(["Lesia", "Klitka", 35, "F"])
#     student.writerow(["Vasyl", "Kor", 31, "M"])
#     student.writerow(["Olga", "Ku", 40, "F"])

# import csv

# with open("students2.csv", "r") as file:
#     reader = csv.reader(file, delimiter= "\t", skipinitialspace=True)
#     for row in reader:
#         print(row)

# import csv

# with open("quotes.csv", "r") as file:
#     reader = csv.reader(file, skipinitialspace=True)
#     for row in reader:
#         print(row)

        #['SN', 'Name', 'Quotes']
        #['1', 'Buddha', 'What we think we become']
        #['2', 'Mark Twain', 'Never regret anything that made you smile']
        #['3', 'Oscar Wilde', 'Be yourself everyone else is already taken']

import csv

with open("quotes.csv", "r") as file:
    reader = csv.reader(file, skipinitialspace=True, quoting=csv.QUOTE_ALL)
    for row in reader:
        print(row)

        #['SN', 'Name', 'Quotes']
        #['1', 'Buddha', 'What we think we become']
        #['2', 'Mark Twain', 'Never regret anything that made you smile']
        #['3', 'Oscar Wilde', 'Be yourself everyone else is already taken']
        

