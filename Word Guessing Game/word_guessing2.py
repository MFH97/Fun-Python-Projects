"""
This program is a simple word-guessing game.
The user has to guess the characters in a randomly selected word within a limited number of attempts.
The program provides feedback after each guess, helping the user to either complete the word or 
lose the game based on their guesses.
"""

import random

def word_guessingGame():
    print("Get ready to guess the colour...")
    words = ['red', 'blue', 'green', 'yellow', 'black', 'orange']
    word = random.choice(words)
    
    print("Guess the characters...")
    guesses = ''
    tries = 10
    
    while tries > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
                
        if failed == 0:
            print("\n\nYou win!")
            print("The word is:", word)
            return
        
        print()
        guess = input("Guess a character: ").lower()
            
        if len(guess) != 1:
            print("Only enter a single character at a time!")
            continue
            
        if guess in guesses:
            print("You already guessed that character!")
            continue
            
        guesses += guess
            
        if guess not in word:
            tries -= 1
            print("Wrong!")
            print("You have", tries, "more guesses")
                
        if tries == 0:
            print("\nYou lose! The colour was", word)

if __name__ == '__main__':
    word_guessingGame()