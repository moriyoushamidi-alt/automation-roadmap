import csv 

filtered_peopel = []

with open ("contacts.CSV" ,"r") as file:
     reader = csv.DictReader(file)
     for row in reader:
          age = int(row["age"])
          if age > 24:
               filtered_peopel.append(row)

with open ("filtered_contacts.csv", "w", newline="") as file:
    writer= csv.DictWriter(file, fieldnames=["name", "email", "age"])
    writer.writeheader ()
    writer.writerows(filtered_peopel)

    print(f"{len(filtered_peopel)} people found with age above 24.")                