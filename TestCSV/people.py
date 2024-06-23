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

# import csv

# with open("quotes.csv", "r") as file:
#     reader = csv.reader(file, skipinitialspace=True, quoting=csv.QUOTE_ALL)
#     for row in reader:
#         print(row)

        #['SN', 'Name', 'Quotes']
        #['1', 'Buddha', 'What we think we become']
        #['2', 'Mark Twain', 'Never regret anything that made you smile']
        #['3', 'Oscar Wilde', 'Be yourself everyone else is already taken']


#Exercise 4

# import csv

# with open("people.csv", "r") as file:
#     reader = csv.reader(file)

#     with open("new_people_2.csv", "w") as new_file:
#         writer = csv.writer(new_file, delimiter="/", skipinitialspace=True)

#         for line in reader:
#             writer.writerow(line)


#Exercice 5
#DictReader

# import csv

# with open("people.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line)

        #{'Name': 'Jack', '   Age': '   23', ' Profession': '  Doctor'}
        #{'Name': 'Miller', '   Age': ' 22', ' Profession': '  Engineer'}
        #it's 2 dictionaries

# with open("people.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

        #['Name', '   Age', ' Profession']
        #['Jack', '   23', '  Doctor']
        #['Miller', ' 22', '  Engineer']
        #it's 3 lists

#Exercice 5 
#Dictionaries indeks

# import csv

# with open ("people.csv", 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file, skipinitialspace=True)

#     for line in csv_reader:
#         print(line["Age"])

#         #22
#         #23


#Exercice 6
#DictWriter

import csv

with open ("people.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("new_people_3", "w") as new_csv_file:
        fieldnames = ["Name", "Age", "Profession"]
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter="|")

        for line in csv_writer:
            csv_writer.writerow(line)





    
        

