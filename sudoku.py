
def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None # If there is no empty spaces on the puzzle

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_values = puzzle[row]
    if guess in row_values:
        return False  # if we've repeated, then our guess is not valid!

    # now extract column values
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    # and then the square
    row_start = (row // 3) * 3    # 0, 3, 6     Ex: (10 // 3) = 3,    (5 // 3) = 1,    (1 // 3)  = 0
    col_start = (col // 3) * 3    # 0, 3, 6

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If we get here, The guess fits well, these check pass..
    return True




def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # Step 1: choose somewhere on the puzzle to guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there is nowhere left, means we have solved the puzzle..
    if row is None:
        return True

    # Step 2: if there is place to write, Then guess a number and check the possibilities
    for guess in range(1,10): # range(1,10) -> 1,2,3,...,9
        # Step 3: check if it is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # Step 4: Now recursively call our functions
            if solve_sudoku(puzzle):
                return True

        # if the guess is not valid, Will try another number
        puzzle[row][col] = -1 # Reset the guess

    # Step 6: if the above for loop doesn't return True, Means we haven't solved the puzzle.. Puzzle is UNSOLVABLE
    return False


if __name__=='__main__':
    example_board = example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print("Board before solving...")
    print(example_board)
    if solve_sudoku(example_board):
        print("Yay! You have solved the Puzzle..")
        print(example_board)
    else:
        print("Puzzle remain unsolved...")
        print(example_board)


    


    






