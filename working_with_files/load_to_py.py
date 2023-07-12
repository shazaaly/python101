import json

# create a JSON string
json_string = '{"name": "John Doe", "age": 30, "is_student": true,"hobbies": ["reading", "writing", "coding"]}'

# convert the JSON string to a Python dictionary
data = json.loads(json_string)

# print the Python dictionary
print(data)

