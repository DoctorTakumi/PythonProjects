import random

class Game:
    def __init__(self):
        # getting PC's pick
        self.computer_pick = self.get_computer_pick()
        
        # getting user's pick
        self.user_pick = self.get_user_pick()
        
        # getting result of the game
        self.result = self.get_result()
        
    def get_computer_pick(self):
        # getting random num
        random_number = random.randint(1,3)
        
        # possible options
        options = {1: "rock", 2: "paper", 3: "scissors"}
        
        # returning the value
        return options[random_number]
    
    def get_user_pick(self):
        # defining valid choices
        valid_choices = ["rock", "paper", "scissors"]
        
        # infinite While loop
        # converting to lowercase
        while True:
            user_pick = input ("Enter rock/paper/scissors: ").lower()
            
            # terminate the loop in case of choosing r/p/s
            if user_pick in valid_choices:
                break
            else:
                print (f"{user_pick} is invalid choice! Please, enter rock, paper or scissors!")
                
        return user_pick
    
    def get_result(self):
        # condition for draw
        if self.computer_pick == self.user_pick:
            return "draw"
        
        # conditions for the user to win
        elif self.user_pick == "paper" and self.computer_pick == "rock":
            return "win"
        elif self.user_pick == "rock" and self.computer_pick == "scissors":
            return "win"
        elif self.user_pick == "scissors" and self.computer_pick == "paper":
            return "win"
        
        # in remaining conditions, user lose
        else:
            return "lose"
        
    def print_result(self):
        print (f"Computer's pick: {self.computer_pick}")
        print (f"Your pick: {self.user_pick}")
        print (f"You {self.result}!")
        
# creating an object of the Game class
def main():
    while True:
        game = Game()
        game.print_result()
        
        while True:
            play_again = input ("Do you want to play again: (y/n): ").lower()
            
            if play_again == "y" or play_again == "yes":
                break  # starts a game
            elif play_again == "n" or play_again == "no":
                print ("Thanks for playing!")
                return  # exits a game
            else:
                print ("Invalid input! Please enter y/n or yes/no!")
                
main()

# idea to specify a fixed number of games played
# while True:
#     game = Game(5) # number of games
#     game.print_result()