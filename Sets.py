myset = {"apple","banana","cherry"}
print(myset)
#Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

myset.add("Orange")
print(myset)

thisset.update(myset)
print(thisset)

# in set items are unchangagble but you can add or remove
# so pop remove update etc just like list work here

print("Adding Sets")
print(myset)
print(thisset)
set3 = myset.union(thisset)
print(set3)