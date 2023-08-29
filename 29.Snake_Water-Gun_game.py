import random

def snake_water_gun():
    choices = ["snake", "water", "gun"]
    computer_choice = random.choice(choices)
    
    your_choice = input("Enter your choice (snake/water/gun): ").lower()
    
    if your_choice not in choices:
        print("Invalid choice! Please choose from snake, water, or gun.")
        return
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {your_choice}")
    
    if your_choice == computer_choice:
        print("It's a tie!")
    elif your_choice == "snake":
        if computer_choice == "water":
            print("You win!")
        else:
            print("Computer wins!")
    elif your_choice == "water":
        if computer_choice == "gun":
            print("You win!")
        else:
            print("Computer wins!")
    elif your_choice == "gun":
        if computer_choice == "snake":
            print("You win!")
        else:
            print("Computer wins!")

snake_water_gun()
