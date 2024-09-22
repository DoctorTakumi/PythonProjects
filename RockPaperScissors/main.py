import random

# function to return rock, paper or scissors based on RNG
def get_computers_choice():
    
    # generating random number between 1 and 3
    random_number = random.randint(1,3)
    
    # creating a dictionary with 1-3 and R/P/S
    options = {1: "rock", 2: "paper", 3: "scissors"}
    
    computers_choice = options [random_number]
    
    return computers_choice


def get_user_input():
    # defining valid choices
    valid_choices = ["rock", "paper", "scissors"]
    
    # taking user input and converting to lowercase
    while True:
        user_input = input ("Enter rock/paper/scissors: ").lower()
    
        if user_input in valid_choices:
            return user_input
        else:
            print (f"{user_input} is invalid choice. Please enter rock, paper or scissors.")


def get_result (user_pick, computer_pick):
    
    # condition for draw
    if user_pick == computer_pick:
        return "Draw"
    
    # conditions for user to win
    elif user_pick == "paper" and computer_pick == "rock":
        return "Win"
    elif user_pick == "rock" and computer_pick == "scissors":
        return "Win"
    elif user_pick == "scissors" and computer_pick == "paper":
        return "Win"
    
    # remaining conditions will result user to lose
    else:
        return "Lose"
    
    
computer_pick = get_computers_choice()

user_pick = get_user_input()
    
result = get_result (user_pick, computer_pick)

print (f"Computer's pick: {computer_pick}")
print (f"Your pick: {user_pick}")
print (f"You: {result}")