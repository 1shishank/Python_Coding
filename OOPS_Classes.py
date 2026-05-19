"""
class is like a blueprint to make objects


"""

class MyClass:
    x = 5

s1 = MyClass()
print(s1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.myfunc()

#del p1

print(p1)

""" A class function cannot be empty so if you make one use pass"""

class empty:
    pass

""" you can also set default values in init like 
def __init__(self,name,age=18):
    """

#you can call self multiple times in class in different ways 

class Hello:
    def __init__(self,name):
        self.name = name
    
    def greet (self):
        return "Hello" + self.name
    
    def welcome(self):
        message = self.greet()

        print(message + "welcome")

s1 = Hello("sd")
sd.welcome()

#Calling methods with parametres

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

