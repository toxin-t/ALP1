'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1 there is no input so nothing will show up

age = 18 

if age > 18: 
 print("You are old enough to drive") 

# Example code 2 the same thing no input so nothing will show up

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 

# Example code 3 because this have an input text will show up

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
