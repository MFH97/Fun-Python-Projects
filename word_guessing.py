"""
This program is a simple word-guessing game.
The user has to guess the characters in a randomly selected word within a limited number of attempts.
The program provides feedback after each guess, helping the user to either complete the word or 
lose the game based on their guesses.
"""
import random

print("Get ready to guess the programming language...")
name = input("What's your name? ")
print("Good luck! ", name.title() +"\n")

words = ['c++','java','python','html','ruby','javascript']
word = random.choice(words) #randomly picks a word from words list

print("Guess the characters")

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
        print()
        print("\nYou win!")
        print('The word is: ', word)
        break
    
    print()
    guess = input("Guess a character: ").lower()  # Convert guess to lowercase
    
    # Check if the guess is a single character
    if len(guess) != 1:
        print("Please enter only one character at a time!")
        continue
        
    # Check if the character was already guessed
    if guess in guesses:
        print("You already guessed that character!")
        continue
        
    guesses += guess
    
    if guess not in word:
        tries -= 1
        print("Wrong!")
        print("You have", tries, 'more guesses')
        
        if tries == 0:
            print()
            print("\nYou lose! Better luck next time")
            print("The word was:", word)
