import csv


with open ('machine_2024.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONE, escapechar='|')
    line_to_read = int(input("Enter a number of lines you want to read: "))
    current_line = 0
        
    for row in csv_reader:
        print(row[:5])
        current_line += 1
        if current_line > line_to_read:
            break


            