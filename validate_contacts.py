import csv
import json

valid_contacts=[]
invalid_contacts = 0

with open("contacts.CSV", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["name"] != "" and "@" in row["email"]:
            valid_contacts.append(row)
        else:
            invalid_contacts= invalid_contacts+1  

with open("valid_contacts.json", "w") as file:
    json.dump(valid_contacts, file)



print(f"valid: {len(valid_contacts)}") 
print(f"invalid: {invalid_contacts}")