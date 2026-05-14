# A function is a block of code which only runs when you call it 

def funcname():
    print("hello world")

funcname()

def ftoc(b):
    return (b-32) *5/9

print(ftoc(-2))

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")