# import csv

# with open('people.csv', 'r') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


import csv
import os

file_path = 'TestCSV/people.csv'
print(f"Current working directory: {os.getcwd()}")
print(f"Looking for file at: {os.path.abspath(file_path)}")

try:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found. Please check the path and filename.")