""""
Hangman game
1.A random fruit name is selected from a predefined list.

2.The player has (length of word + 2) chances to guess the word.

3.For each turn, the player guesses a single letter.

4.Correct guesses reveal all instances of that letter in the word.

5.The game ends when either:
 -The player guesses all letters correctly (win)
 -The player runs out of chances (lose)
""""

import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''.split()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
#Main game function
def play_hangman():
    word = random.choice(someWords).lower()
    print('Guess the word! HINT: word is a name of a fruit')
    print('_ ' * len(word)) #Shows underscores for each letter
    
    letterGuessed = '' #Tracks guessed letters, remaining chances, and game state
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    try:
        while chances > 0 and not flag:
            print(f"\nChances left: {chances}")
            print(display_hangman((len(word) + 2) - chances))
            
            guess = input('Enter a letter to guess: ').lower()
            
            # Input validation
            if not guess.isalpha() or len(guess) != 1:
                print('Please enter a single letter!')
                continue
            if guess in letterGuessed:
                print('You already guessed that letter!')
                continue
                
            letterGuessed += guess
            
            if guess in word:
                print('Good guess!')
            else:
                print('Wrong guess!')
                chances -= 1
                
            # Display current progress
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
                    
            # Check for win condition
            if all(char in letterGuessed for char in word): #all() to verify all letters guessed
                print(f"\nThe word is: {word}")
                print('Congratulations, You won!')
                flag = 1
                
        if not flag:
            print(f"\nYou lost! The word was {word}")
            
    except KeyboardInterrupt:
        print("\nBye! Try again later.")

if __name__ == '__main__':
    play_hangman()
