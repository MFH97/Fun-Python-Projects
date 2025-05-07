import random

# Introduction
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

# Initialize scores
player_score = 0
com_score = 0

# Main game loop
while True:
    print("\nEnter your choice: \n1. Rock \n2. Paper \n3. Scissors \n0. Exit")
    
    # Get and validate user input
    try:
        choice = int(input("Your choice: "))
        while choice < 0 or choice > 3:
            choice = int(input("Please enter 0, 1, 2, or 3 only: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Exit condition
    if choice == 0:
        print("\nFinal Scores:")
        print(f"Player: {player_score}  Computer: {com_score}")
        if player_score > com_score:
            print("== Player wins overall! ==")
        elif com_score > player_score:
            print("== Computer wins overall! ==")
        else:
            print("== It's a tie overall! ==")
        break

    # Map choices to names
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    choice_name = choices[choice]
    
    print(f"\nYour choice: {choice_name}")
    print("Computer's turn...")
  
    # Computer's choice
    com_choice = random.randint(1, 3)
    com_choice_name = choices[com_choice]
    
    print(f"Computer's choice: {com_choice_name}")
    print(f"{choice_name} VS {com_choice_name}")
  
    # Determine winner
    if choice == com_choice:
        result = 'Draw'
    elif (choice == 1 and com_choice == 3) or \
         (choice == 2 and com_choice == 1) or \
         (choice == 3 and com_choice == 2):
        result = 'Player'
    else:
        result = 'Computer'

    # Update scores and display result
    if result == 'Draw':
        print("\n<== It's a Draw! ==>")
        player_score += 1
        com_score += 1
    elif result == 'Player':
        print("\n<== Player Won! ==>")
        player_score += 1
    else:
        print("\n<== Computer Won! ==>")  
        com_score += 1

    print(f"\nCurrent Scores: Player: {player_score}  Computer: {com_score}")
    print("<================================>")