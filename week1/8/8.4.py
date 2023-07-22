'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''
chosen = input("To choose a weapon from a list, press 1. To choose your own weapon, press 2: ")
if chosen == "1":
    weapons = ["rifle", "pistol", "baseball bat", "knife"]
    print("You have encountered a zombie.")
    print("Choose a weapon:")
    for weapon in weapons:
        print(weapon)
    weapon_choice = input().lower()
    if weapon_choice == "rifle":
        print("You died.")
    elif weapon_choice == "pistol":
        print("You killed the zombie.")
    elif weapon_choice == "baseball bat":
        print("You died.")
    elif weapon_choice == "knife":
        print("You died.")
    else:
        print("Invalid weapon choice.")
elif chosen == "2":
    print("Enter your weapon of choice: ")
    weapon_choice = input().lower()
    if weapon_choice == "rifle":
        print("You died.")
    elif weapon_choice == "pistol":
        print("You killed the zombie.")
    elif weapon_choice == "baseball bat":
        print("You died.")
    elif weapon_choice == "knife":
        print("You died.")
    else:
        print("Invalid weapon choice.")
else:
    print("Invalid input.")

#define a variable and have the input taken from the user

