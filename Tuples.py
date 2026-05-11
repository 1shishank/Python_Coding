mytuple = ("one","two","three")
print(mytuple)
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
in same ways you can append or remove
"""

y= list(mytuple)
y[1]="first"
mytuple=tuple(y)
print(mytuple)

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

## Index method finds the first occurance of the specified value

x = fruits.index("cherry")
print(x)