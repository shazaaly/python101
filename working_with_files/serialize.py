import pickle
obj = {
    "name": "John Dou",
    "age": 56,
    "hobbies": ['reading', 'football']
}

serialize = pickle.dumps(obj)
print(serialize)

deserialize = pickle.loads(serialize)
print(deserialize)
