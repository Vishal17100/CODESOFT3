import random

def play():
    """At initially user and computer's points are 0"""
    user_points = 0
    computer_points = 0

    while True:
        """Taking user's and computer's choice"""
        user_choice = input("Choose rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])

        """If user win increase it's point by 1"""
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_points += 1
        else:
            print("Computer wins!")
            computer_points += 1

        print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")
        print(f"Score: You - {user_points}, Computer - {computer_points}")

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play()