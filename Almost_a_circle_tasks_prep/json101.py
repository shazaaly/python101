import json

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
