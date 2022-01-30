#GAME CREDITS: guimaion
#A variation to be implemented with quantum key distribution should time permit
#Play battleship with the security of knowing that your transmissions are secure and safe from prying ears
#Intermediate 3rd party to mediate the communications

from random import randint
board = []
for x in range(5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#asking the user for a guess
for turn in range(4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print("You sunk my battleship!")
        break
    else:
        #warning if the guess is out of the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Out of Bounds")
        
        #warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print("Already Guessed.")
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print("Miss!")
            board[guess_row][guess_col] = "X"
        
        # Print turn and board  
        print("Turn " + str(turn+1))
        print_board(board)
