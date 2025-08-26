from random import randint

moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == 1 and computer == 3) or \
         (player == 2 and computer == 1) or \
         (player == 3 and computer == 2):
        return "win"
    else:
        return "lose"

def main():
    print("Welcome to Rock Paper Scissors")
    while True:
        try:
            choice = int(input("Choose your hand: 1 for Rock, 2 for Paper, 3 for Scissors (0 to quit): "))
            if choice == 0:
                print("Goodbye!")
                break
            if choice not in [1, 2, 3]:
                print("Invalid choice. Try again.")
                continue

            computer = randint(1, 3)
            print(f"You chose {moves[choice]}, computer chose {moves[computer]}.")

            result = get_winner(choice, computer)
            if result == "draw":
                print("It's a draw! Try again.")
            elif result == "win":
                print("You win!")
            else:
                print("You lost.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main()
