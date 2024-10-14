import math

class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']
        
    # method to print the board
    def print_board(self):
        print ('\n')
        print (' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print ('-----------')
        print (' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print ('-----------')
        print (' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        
    # method to print out the board with numbers 1-9 for visual representation
    def print_numbered_board(self):
        print('\n')
        print(' 1 | 2 | 3')
        print('-----------')
        print(' 4 | 5 | 6')
        print('-----------')
        print(' 7 | 8 | 9')
        
    def update_board(self, position, type):
        # adding try...except to prevent players select position other than position-1 
        try:
            # player select position n, n-1 index is being updated
            # if position is not filled, update the board
            if self.board[position-1] == ' ':
                self.board[position-1] = type
                return True
            # if position if already filled, ask user to select another position
            else:
                print ("Position already selected. Select another position!")
                return False
        except:
            print ("Invalid position! Select another position!")
        
    # adding win conditions
    # if three same symbols appears in a row - return True
    def check_winner (self, type):
        if (self.board[0] == type and self.board[1] == type and self.board[2] == type) or \
           (self.board[3] == type and self.board[4] == type and self.board[5] == type) or \
           (self.board[6] == type and self.board[7] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[3] == type and self.board[6] == type) or \
           (self.board[1] == type and self.board[4] == type and self.board[7] == type) or \
           (self.board[2] == type and self.board[5] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[4] == type and self.board[8] == type) or \
           (self.board[2] == type and self.board[4] == type and self.board[6] == type):
            return True
        else:
            return False
        
    # adding draw condition - if all fields are filled and no row is connected
    # if draw - return True
    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False

class Player:
    def __init__(self, type):
        self.type = type  # type refers to "X" or "O"
        self.name = self.get_name()
        
    def get_name(self):
        if self.type == "X":
            name = input ("Player selecting X, enter your name: ")
        else:
            name = input ("Player selecting O, enter your name: ")
        return name
    
class Game:
    def __init__(self):
        # board attribute to store an object of the Board class
        self.board = Board()
        
        # player1 and player2 attributes to store objects for the 1st and 2nd player
        self.player1 = Player("X")
        self.player2 = Player("O")
        
        # current_player attribute to identify the turn of either player
        self.current_player = self.player1
        
        # showing the numbered board for visual representation
        print ("\nHere is the layout of the board with numbered positions:")
        self.board.print_numbered_board()
        
    def play(self):
        # infinite loop to run the game
        while True:
            # adding try...except to remind players that only numbers 1-9 are valid input
            try:
                message = f"\n{self.current_player.name}, enter your position (1-9): "
                position = abs(int(input(message)))  # convert the input to its absolute value (preventing user from inputting negative values)
                
                # the update_board() method to return True if the user selected position is not filled yet
                if self.board.update_board(position, self.current_player.type):
                    self.board.print_board()
                    
                    # checking winner each time after the board is updated
                    if self.board.check_winner(self.current_player.type):
                        print (self.current_player.name, "wins!")
                        break
                    
                    # checking draw each time after the board is updated
                    elif self.board.check_draw():
                        print ("Game is a draw!")
                        break
                    
                    # switching players when board is updated
                    else:
                        if self.current_player == self.player1:
                            self.current_player = self.player2
                        else:
                            self.current_player = self.player1
            except:
                print ("Invalid input! Enter a number between 1 and 9!")
                
    # adding a possibility to start a new game
    def play_again(self):
        while True:
            play_again = input ("Do you want to play another game? (y/n): ").lower()
            if play_again == "y" or play_again == "yes":
                print ("Great, let's go!")
                return True
            elif play_again == "n" or play_again == "no":
                print ("Thank you for playing!")
                return False
            else:
                print ("Invalid input! Please enter y/no or yes/no!")
                
def main():
    while True:
        game = Game()
        game.play()
        if not game.play_again():
            break
        
main()