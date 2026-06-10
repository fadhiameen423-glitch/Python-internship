import json

student = [
    {"ID":1,"Name":"Fadhi","Age":20},
    {"ID":2,"Name":"Aber","Age":20},
    {"ID":3,"Name":"Ayas","Age":20},
    {"ID":4,"Name":"Sathyan","Age":20},
    {"ID":5,"Name":"Gautham","Age":20},
]

with open("students.json", "w") as f:
   json.dump(student , f , indent=2)

with open("students.json") as f:
    data=json.load(f)

for student in data:
   print(f"ID: {student['ID']}")
   print(f"Name: {student['Name']}")
   print(f"Age: {student['Age']} \n")