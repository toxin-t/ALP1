# Starter Code
number1 = int(input("Please enter a number "))
number2 = int(input("Please enter another number "))
number3 = int(input("Please enter a third number "))

if number1 > number2:
    print("Number 1 is bigger than number 2")
elif number2 > number1:
    print("Number 2 is bigger than number 1")
else:
    print(" numbers are the same")

if number3 > number1 and number3 > number2:
    print("Number 3 is bigger than number 1 and number 2")
elif number3 < number1 and number3 < number2:
    print("Number 3 is smaller than number 1 and number 2")
elif number3 == number1 and number3 == number2:
    print("Number 3 is the same as number 1 and number 2")
elif number3 == number1:
    print("Number 3 is the same as number 1")
elif number3 == number2:
    print("Number 3 is the same as number 2")
elif number3 > number1:
    print("Number 3 is bigger than number 1")
else:
    print("Number 3 is smaller than number 1")