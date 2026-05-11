myset = {"apple","banana","cherry"}
print(myset)
#Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

myset.add("Orange")
print(myset)

thisset.update(myset)
print(thisset)