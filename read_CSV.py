import csv

with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)