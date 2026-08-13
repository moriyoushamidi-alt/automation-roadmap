import csv
young_contacts=[]

with open("contacts.CSV", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        age=int(row["age"])
        if age < 28:
            young_contacts.append(row)

with open("young_contacts.csv", "w", newline="") as file:
    writer=csv.DictWriter (file, fieldnames=["name", "email", "age"])    
    writer.writeheader()  
    writer.writerows(young_contacts)
           
            
print(young_contacts)            