'''
In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:
- Rename the function so that it has a sensible name. Don't forget to rename it when it is called.
- Call the function with the argument 'Sweden'.
- Get the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.
'''
def country_of_origin(country):
  print("I am from " + country)

country_of_origin("sweden")

user_country = input("Enter a country: ")
country_of_origin(user_country)

# Renamed the function to (country_of_origin)
# Called the function with the argument (Sweden)
# Added a user input prompt to get a country from the user and pass it as an argument to the function



