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

"""When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null """

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

import re

"""
Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string """


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("rain", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)