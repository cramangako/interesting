import random

secret = random.randint(1, 100)
turns = 0
choice = 0

while choice != secret:
    choice = int(input("Choose your number: "))
    turns += 1
    if choice == secret:
        print(f"lucky duck did it in {turns} moves")
    elif choice > secret:
        print("Secret number is lower")
    else:  # choice < secret
        print("Secret number is higher")
