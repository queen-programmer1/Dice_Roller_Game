import random

userInput = input("Roll the dice? (y/n): ")


while True:
    if userInput == "y":
        print((random.randrange(1,6), random.randrange(1,6)))
        userInput = input("Roll the dice? (y/n): ")
        
    elif userInput == "n":
        print("Thanks for playing! :)")
        break
    
    else:
        print("Invalid choice") 
        userInput = input("Roll the dice? (y/n): ")