import random

print("Rock, Paper, Scissors")

user_score = 0
computer_score = 0
rounds_played = 0

while True:
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    rounds_played += 1
    print(f"Score => You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

print("\nGame Over!")
print(f"Total rounds played: {rounds_played}")
print(f"Final Score => You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("The computer won the game. Better luck next time!")
else:
    print("The game ended in a draw.")
 