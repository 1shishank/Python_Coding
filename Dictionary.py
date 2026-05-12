"""Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
x = thisdict["model"]
print(x)
y= thisdict.get("model")
print(y)
x = thisdict.keys()
print(x)
thisdict["colors"]="White"
x = thisdict.keys()
print(x)
x=thisdict.values()
print(x)

print("Updating the dictionary")
thisdict.update({"year":2020})
print(thisdict)

for a in thisdict:
    print(a)
for a in thisdict:
    print(thisdict[a])

for x,y in thisdict.items():
    print(x,y)

mydict = thisdict.copy()
print(mydict)

print("Nested Dictionary")

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
for x, obj in myfamily.item:
    print(x)
    for y in obj:
        print(y + ":"+ obj[y])

"""Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""