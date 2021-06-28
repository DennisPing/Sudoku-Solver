# Sudoku-Solver

Solve sudoku using backtracking

## Python and Pip Requirements

- Python 3
- pyautogui

## How to Run

`python sudoku.py`

## Example Console Input

```
Row 1: 030000000
Row 2: 590000700
Row 3: 004350000
Row 4: 000090560
Row 5: 000807042
Row 6: 000004000
Row 7: 006000000
Row 8: 801000900
Row 9: 040200801
```

## Example Console Output

```
Sudoku puzzle solution:
Time taken: 0.185 seconds
[[1, 3, 2, 7, 4, 9, 6, 8, 5],
 [5, 9, 8, 6, 1, 2, 7, 3, 4],
 [7, 6, 4, 3, 5, 8, 2, 1, 9],
 [4, 2, 7, 1, 9, 3, 5, 6, 8],
 [9, 1, 5, 8, 6, 7, 3, 4, 2],
 [6, 8, 3, 5, 2, 4, 1, 9, 7],
 [2, 5, 6, 9, 8, 1, 4, 7, 3],
 [8, 7, 1, 4, 3, 5, 9, 2, 6],
 [3, 4, 9, 2, 7, 6, 8, 5, 1]]
 ```

## Autocomplete on Sudoku.com

This sudoku solver automatically keys in the answers onto https://sudoku.com/

![gif](https://github.com/DennisPing/Sudoku-Solver/blob/main/sudoku-demo.gif)

I gave the program 5 seconds to wait for you to press the first square in the puzzle.

You can change the wait time in the code.
