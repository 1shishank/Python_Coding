# List are used to store multiple ites in a single variable

mylist = ["apple","banana","grapes"]
print(mylist)

thislist = list(("one","two","three","four"))
print(thislist)
# accesing list
print(thislist[1])
print(thislist[-1])
print(thislist[1:3])

#check if items exist

if "one" in thislist:
    print("one is the list")

# to change list items

thislist[2]="third"
print(thislist)

# to add to a list use append

thislist.append("five")
thislist.extend("six")
print(thislist)

#the extend method can add any objects

thistuple = ("aps")
thislist.extend(thistuple)

#to insert at a specific index use insert

thislist.insert(1,"first")
print(thislist)

# to remove from a tupple
thislist.remove("s")
print(thislist)
#remove method removes first occurance of the item

thislist.pop(2)
print(thislist)
#if you do not specify it removes last index
# to deleted the list use del thislist
# to clear use thislist.clear



"""looping a list"""
print("looping a list")

newlist =[7,8,9,10]
for x in newlist:
    print(x)

for i in range(len(newlist)):
    print(i)
    print(newlist[i])

# using a while loop
i = 0
print("while loop")
while i< len(newlist):
    print(newlist[i])
    i = i+1

print(" for loop in shortcut")
[print(x) for x in newlist]
print("list comprehnsion")

findlist = []

for x in newlist:
    if x == 7 :
        findlist.append(x)

print(findlist)

# [expression for item in iterable if condition == True]

newlist = [x for x in newlist if 8 == x ]
print(newlist)

## sorting 

newlist = [100, 50, 65, 82, 23]
newlist.sort()
print(newlist)
newlist.sort(reverse=True)
print(newlist)

##customize sort fucntion
##numbers near to 50  using key = function

def myfunc(n):
    return abs(n-50)
newlist.sort(key=myfunc)
print(newlist)

## copying a alist

copylist=newlist.copy()
print("This is the copy of newlist", copylist)

"""Overall List Methods
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list """