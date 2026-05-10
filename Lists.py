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