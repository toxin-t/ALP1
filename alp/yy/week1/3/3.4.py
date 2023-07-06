'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''
name=input("What is your name ? ")
print("welcome "+name)
ice =input("so what is your favorite icecream flavor? " )
food= input("what is the favorite food? ")
ff= input("what pizza place is the best? " )
print("so your name is "+name+" and your favorite icecream flavor "+ice+" and your favorite food is "+food+" and you think "+ff+" is the best pizza place?" )
