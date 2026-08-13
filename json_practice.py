import json

person = {
    "name": "Sara" ,
    "age": 25 ,
    "city": "Tehran"
    }

json_text = json.dumps(person)
print(json_text)
print(type(json_text))

parsed_back=json.loads(json_text)
print(parsed_back)
print(type(parsed_back))
print(parsed_back["name"])

with open("person.json", "w") as file:
    json.dump(person, file)

with open("person.json", "r") as file:
    loaded_person= json.load(file)

print(loaded_person)
print(loaded_person["city"])