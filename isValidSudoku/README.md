# Valid Sudoku

## Problem Statement
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated based on the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Link to the problem: [Valid Sudoku on LeetCode](https://leetcode.com/problems/valid-sudoku/description/)

## Solution Approach

This solution verifies the validity of a partially filled Sudoku board by ensuring there are no duplicate numbers in any row, column, or 3x3 sub-box. Here is a step-by-step breakdown of the algorithm:

### Step 1: Initialize Data Structures
Three lists of sets are initialized to keep track of the numbers present in each row, column, and 3x3 sub-box:
- `rows`: A list of 9 sets, each corresponding to one row of the Sudoku.
- `columns`: A list of 9 sets, each for one column.
- `boxes`: A list of 9 sets, where each set corresponds to one of the 9 sub-boxes in the grid.

### Step 2: Traverse Each Cell
The algorithm iterates over each cell in the 9x9 board using a nested loop (first by rows, then by columns):
- `i`: Index for rows.
- `j`: Index for columns.

### Step 3: Process Each Element
For every element at the position `[i][j]`:
- If the element is a '.', it is skipped as it represents an empty cell.
- If the element is a number:
  1. **Check Row**: Determine if this number already exists in the current row's set. If yes, the board is immediately invalid.
  2. **Check Column**: Determine if this number is already in the current column's set. If yes, the board is invalid.
  3. **Check Box**: Calculate which of the 9 boxes the element belongs to using the formula `box_index = (i // 3) * 3 + (j // 3)`. Check if the number exists in the corresponding box's set. If it does, the board is invalid.

### Step 4: Update Data Structures
If the number is not found in any of the sets (row, column, box), it is added to the respective sets to track further appearances as the board is processed.

### Step 5: Validity
- If no duplications are found throughout the entire board, the function concludes that the Sudoku board setup is valid and returns `True`.
- If any duplication is found in any of the checks, the function returns `False` immediately.

### Complexity
- **Time Complexity**: O(1), since the board size is fixed and the algorithm traverses each of the 81 cells once.
- **Space Complexity**: O(1), due to the fixed size of the board and storage structures.

## Examples
**Example 1:**
Input:
```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
