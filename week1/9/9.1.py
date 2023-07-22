# Example Code 1 
#This code will call three subroutines Each of these subroutines will print out a statement

def say_hi():
  print("Why hello there!")

def offer_drink():
  print("Would you care for a spot of tea?")

def offer_food():
  print("Biscuit?")

def say_bye():
  print("Cheerio then.")


offer_drink()
say_hi()
offer_food()

# Example code 2
#This code defines three different subroutines, each performing a simple math operation and returning the result
def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2

def maths3():
  num1 = 50
  num2 = 5
  return num1 * num2

outputNum = maths2()
print(outputNum)

# Example Code 3
# What does the function location() do?
# It takes a string argument representing the country and prints a string saying "I am from " followed by the country.
def location(country):
  print("I am from " + country)


location("Brazil")

