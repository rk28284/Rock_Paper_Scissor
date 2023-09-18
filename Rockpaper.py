import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    tie_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Enter 'quit' to end the game.")

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        computer_choice = random.choice(choices)

        if user_choice == 'quit':
            break

        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue

        print(f"\nYou chose {user_choice}.")
        print(f"The computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print("It's a tie!")
            tie_score += 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nScore - You: {user_score}  Computer: {computer_score}  Ties: {tie_score}\n")

    print("Thank you for playing!")

play_game()