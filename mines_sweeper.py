""" 
12 Beginner Python Projects - Coding Course
https://www.youtube.com/watch?v=8ext9G7xspg

"""

import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # Let's create the Board
        self.board = self.make_new_board() # plant Bombs
        self.assign_values_to_board()

        # Where we have digged.. Let's keep track of it..
        self.dug = set() # if we dig at (0,0) then self.dug = {(0,0)}


    def make_new_board(self):

        # generate the new board

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # This creates Array like this
        # [[None, None, None,..., None]
        # [None, None, None,...., None]
        # [None, None, None,...., None]
        # [...........................]
        # ......................, None]

        # plant Bombs
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) 
            row = loc // self.dim_size
            col = loc % self.dim_size

            # * -> is the Bomb
            # If there is a Bomb planted already in the - loc - position skip and move to next iteration
            if board[row][col] == '*': 
                continue

            board[row][col] = '*' # Plant the Bomb
            bombs_planted +=1

        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can pre-compute these and it'll save us some
        # effort checking what's around the board later on :)
        
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # There is a Bomb already, We don't want to calculate anything here...
                    continue
                self.board[r][c]= self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!

        num_neighboring_bombs = 0

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # Our origional location, Don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs +=1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        # Keep track of that we dug here

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        # If we got 0 - We have to dig around

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep







        
def play(dim_size=10, num_bombs=10):
    # Step 1: Create the Board and plant bombs
    board = Board(dim_size, num_bombs)
    # Step 2: Show the user board and ask where they want to dig
    # Step 3a: If the location is bomb Game is Over!!!
    # Step 3b: If the location is not the bomb, Dig recursively at least near to Bomb
    # Step 4: repeat Step 2, 3a & 3b untill there is no more places to dig

    safe = True

    while len(board.dug) < board.dim_size ** 2 - board.num_bombs:
        print(board)
        # Input examples:    0,0     Or   0, 0    Or       0,   0
        user_input = re.split(',(\\s)*', input("Where would you like to dig ? Input as (row, col): "))
        (row, col) = int(user_input[0]),  int(user_input[-1])
        if row < 0 or col < 0 or row >= board.dim_size or col >= board.dim_size:
            print("Invalid location, try again..")
            continue

        # If the input is valid, We will dig
        safe = board.dig(row, col)

        if not safe:
            # We hit a Bomb
            break # Game Over, RIP..
    
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY, GAME OVER.... :(")
        # Let's reveal the board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
       


if __name__=='__main__': # Good Practice...
    play()



    
