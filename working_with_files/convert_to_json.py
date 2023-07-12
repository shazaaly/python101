
import json

# create a Python dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'is_student': True,
    'hobbies': ['reading', 'writing', 'coding']
}

json_str = json.dumps(data)
print(json_str)

with open("hello.txt", "w") as file:
    json.dump(data, file)
