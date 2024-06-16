import csv

with open('peopleTestCSV2.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)