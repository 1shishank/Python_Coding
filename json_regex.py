#Python has a built-in package called json, which can be used to work with JSON data

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.load(x)

print(y["age"])

# Convert python to json

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)