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