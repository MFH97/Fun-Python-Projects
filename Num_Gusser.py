'''



'''
import random

def number_guessingGame (guess):
    number_to_guess = random.randrange(10)
    numOfGuesses = 5
    guessCounter = 0
    
    while guessCounter < numOfGuesses:
        guessCounter += 1
        tracker = numOfGuesses - guessCounter #Track no of guess 
        
        guess = int(input("Guess a no: ")) #Prompt user to guess
        
        if guess == number_to_guess:
            print("Congrats! The num: ", guess)
            break
        elif guess > number_to_guess:
            print("Too High! " + str(tracker) + " guess left")
        
        elif guess < number_to_guess:
            print("Too Low! " + str(tracker) + " guess left")
    return guess
#Initialize guess variable
guess = int
print("Guess a number form 1-10")

if __name__ == '__main__':
    number_guessingGame(guess)