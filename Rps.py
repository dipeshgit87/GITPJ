import random

# Options
choices = ["rock", "paper", "scissors"]

# Get user's choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Get computer's choice
computer_choice = random.choice(choices)
print("Computer chose:", computer_choice)

# Determine winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")