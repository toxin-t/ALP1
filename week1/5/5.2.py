'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer it would be too low

# What happens if you input the guess '6'?
  # Answer it would be too high

# What happens if you input the guess '5'?
  # Answer it would be correct

# What happens if you input the guess '-5'?
  # Answer it would give me an error because 5- is not between 1 and 10

# What happens if you input the guess '0'?
  # Answer it would be too low

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer bigger than  smaller than

# What happens if you change line 9 to if guess = number: ?
  # Answer nothing will change

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer it han an print code


