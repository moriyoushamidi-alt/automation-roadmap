import csv
import json

contacts_list=[]
with open ("filtered_contacts.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        contacts_list.append(row)

api_payload=json.dumps(contacts_list)
print("THis is what we'd SEND to an API:")
print(api_payload)

with open ("contacts_backup.json", "w") as file:
    json.dump(contacts_list, file)

print("\nbackup saved to contacts_backup.json")

with open ("contacts_backup.json", "r") as file:
    loaded_contacts = json.load(file)

print ("\nloaded back from file:")
print(loaded_contacts)
print(f"number of contacts: {len(loaded_contacts)}")    
