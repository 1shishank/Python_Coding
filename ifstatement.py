#normal if statement
age = 20
if age < 18:
    print("age is less than 18")
else:
    print("age is above 18")

print("a") if age < 18 else print("B")

# Using Pass if you want to skip you leave it blank it will give error
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

print("Python Match")

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Looking forward to the Weekend")