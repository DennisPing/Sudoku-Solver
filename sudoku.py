from pprint import pprint
from time import time, sleep
from io_manager import prompt_input, push_to_screen

""" Reference guide from Kylie Ying: https://youtu.be/tvP_FZ-D9Ng """

def find_next_empty(puzzle):
    """ Return row, col tuple (or None, None) if there is no empty square"""
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r,c
    return None, None # No open square found

def is_valid(puzzle, guess, row, col):
    """ Return True if guess is valid, False if guess is not valid"""
    for i in range(9):
        if (puzzle[row][i] == guess or puzzle[i][col] == guess):
            return False

    # Find out which subsquare we are in
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # All checks passed!
    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True # Puzzle is solved
    
    for guess in range(1,10):
        # Check if this a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess 
            if solve_sudoku(puzzle):
                return True

        # Backtrack and try a new number
        puzzle[row][col] = 0

    # Unsolvable edge case
    return False

def main():
    puzzle = prompt_input()
    start = time()
    if not solve_sudoku(puzzle):
        print("Oops, this sudoku puzzle is not solvable.")
    print("Sudoku puzzle solution:")
    end = time()
    print(f"Time taken: {round(end - start, 3)} seconds")
    pprint(puzzle)

    sleep(5)
    push_to_screen(puzzle)

if __name__ == '__main__':
    main()