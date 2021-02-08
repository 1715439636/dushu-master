import csv
with open('data.csv', 'r') as f:
     reader = csv.reader(f)
     print(type(reader))

     for row in reader:
         print(row)