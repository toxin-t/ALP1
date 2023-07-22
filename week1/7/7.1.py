# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.line 10 to 12 is in a loop and 20 to 22

# Explain the circumstances in which the loop will run. so a loop will start with (while)


print("What is the capital of France?")
answer = input() 

while answer != "Paris":
  print("Incorrect! Try again.")
  answer = input("What is the capital of France?")

print("Correct!")

# Example code 2

counter = 1

while counter < 5:
  print("This code is inside the loop")
  counter += 1


