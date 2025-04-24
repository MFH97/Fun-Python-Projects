'''

Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that 
integer in the minimum number of guesses

'''
import random

print("Welcome to Number Guessing game!")
print("\nYou can guess any numbers from 1 to 100")
print("\nLet's start the game....")

number_to_guess = random.randrange(100)

chances = int(input("\nHow many guesses you want? "))
guessCounter = 0



while guessCounter < chances:
    guessCounter += 1
    my_guess = int(input("Enter your guess: "))
    
    if my_guess == number_to_guess:
        print(f'\nThe number is {number_to_guess} and you got it right! in the {guessCounter} attempt')
        break
    
    elif guessCounter >= chances and my_guess != number_to_guess:
        print(f"Dang! The number is {number_to_guess} better luck next time!")
        
    elif my_guess > number_to_guess:
        print("You guessed too high!")
    
    elif my_guess < number_to_guess:
        print("You guessed too low!")
