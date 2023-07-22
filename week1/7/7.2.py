number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = input()
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer

# What does '!=' mean?
  # Answer

# How many variables are there in the code?
  # Answer

# How can you tell which lines of code are inside the loop?
  # Answer

# How many times will the loop repeat?
  # Answer

# What has to happen to make the program run the last line of code?
  # Answer 

#task 3
num = 56
guess = 0

while guess != num:
    guess = int(input("Guess the number: "))

    if guess < num:
        print("Too low, try again!")
    elif guess > num:
        print("Too high, try again!")
    else:
        print("Success! You have guessed the number correctly.")