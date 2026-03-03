import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("===================================")
    print("   ROCK - PAPER - SCISSORS GAME   ")
    print("===================================")
    print("Type 'rock', 'paper', or 'scissors'")
    print("Type 'exit' to quit\n")

    while True:
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print("\nGame Over!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.\n")
            continue

        computer_choice = get_computer_choice()

        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!\n")
        elif winner == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        print("-----------------------------------")

play_game()