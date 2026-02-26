#Dice Roller Game - a program that simulates rolling 2 dice 
#The user has to enter "y" to roll the dice and "n" to end the game
#The program continues to run even when the user inputs an "invalid choice", 
#The program only terminates once the user enter "n", ending the game

import random

dice_rolled_counter = 0 
number_of_dice = int(input("How many dice do you want to roll? "))
userInput = input("Roll the dice? (y/n): ")




while True:
    diceResults = []
    if userInput == "y":
        for i in range(number_of_dice):
            roll = random.randrange(1,6)
            diceResults.append(roll)
            
        
        dice_rolled_counter = dice_rolled_counter + 1
        print(tuple(diceResults))
        diceResults.clear()
        userInput = input("Roll the dice? (y/n): ")
        
        
    elif userInput == "n":
        print("Thanks for playing! :)")
        print("You rolled the dice " + str(dice_rolled_counter) + " times during this game.")
        break
    
    else:
        print("Invalid choice") 
        userInput = input("Roll the dice? (y/n): ")