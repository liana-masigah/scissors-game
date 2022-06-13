import random

print("In this Rock Paper Scissors game: \n" + "R stands for Rock \n" + "P stands for Paper, and \n" + "S stands for Scissors")

while True:
    print("Enter choice \n 1 for R, \n 2 for P, and \n 3 for S \n")
    user_choice = int(input("Enter a choice: "))

    choice_list = ["R", "P", "S"]
    comp_choice = random.choice(choice_list)

    while user_choice > 3 or user_choice < 1:
        user_choice = (input("Enter a valid input: "))

    if user_choice == 1:
        choice_name = "R"
    elif user_choice == 2:
        choice_name = "P"
    else:
        choice_name = "S"

    print(f"\nYou chose {choice_name}, computer chose {comp_choice}.\n")

    if choice_name == comp_choice:
        print(f"Both players selected {choice_name}. It's a tie!")
    elif choice_name == "R":
        if comp_choice == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif choice_name == "P":
        if comp_choice == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice_name == "S":
        if comp_choice == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

