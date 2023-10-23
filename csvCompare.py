import csv
import openpyxl

# Open and read the first CSV file
with open('data1.csv', 'r', encoding='utf-8') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

# Open and read the second CSV file
with open('data2.csv', 'r',encoding='utf-8') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

# Compare based on a common column (e.g., the first column)
matches = []
differences = []

# Based on title and price
for row1 in data1:
    for row2 in data2:
        if row1[0] == row2[0]:
            if row1[2] > row2[2]:
                print("Title: ",row1[0])
                print("Price: ",row2[2])  
            else:
             print("Title: ",row1[0])
             print("Price: ",row1[2])  
            break
    else:
        differences.append(row1)

# Based on ratings
for row1 in data1:
    for row2 in data2:
        if row1[0] == row2[0]:
            if row1[3] > row2[3]:
                print("Title: ",row1[0])
                print("Price: ",row2[2])  
                print("Rating: ",row2[3])
            else:
             print("Title: ",row1[0])
             print("Price: ",row1[2]) 
             print("Rating: ",row1[3]) 
            break
    else:
        differences.append(row1)


