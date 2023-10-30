import random

# Initialize scores
user_score = 0
computer_score = 0

# Map between user input and choices
choices = {
    'rock': 'Rock',
    'paper': 'Paper',
    'scissors': 'Scissors'
}

# Function to get user's choice
def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")

# Function to get computer's choice
def get_computer_choice():
    return random.choice(list(choices.keys()))

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "User"
    else:
        return "Computer"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "User":
        user_score += 1
        print("You win this round!")
    elif winner == "Computer":
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("It's a tie!")

    print(f"User: {user_score} - Computer: {computer_score}")

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Final Scores:")
        print(f"User: {user_score} - Computer: {computer_score}")
        break
