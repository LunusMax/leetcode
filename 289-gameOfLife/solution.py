from typing import List
import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        board_copy = copy.deepcopy(board)
        rows, cols = len(board, 0)
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1), (0, 1), 
                      (1, -1), (1, 0), (1, 1)]  # Neighbours

        for row in range(rows): # Nested loops to go through list of lists
            for col in range(cols):
                alive_neigh = 0
                for dm, dn in directions:
                    m = row + dm
                    n = col + dn
                    if m in range(rows) and n in range(cols) and board_copy[m][n] == 1:
                        alive_neigh += 1

                if board_copy[row][col] == 1 and alive_neigh < 2: # Condition 1 - Underpopulation
                    board[row][col] = 0
                elif board_copy[row][col] == 1 and alive_neigh >= 2 and alive_neigh <= 3: # Condition 2
                    board[row][col] = 1
                elif board_copy[row][col] == 1 and alive_neigh > 3: # Condition 3 - Overpopulation
                    board[row][col] = 0
                elif board_copy[row][col] == 0 and alive_neigh == 3: # Condition 4 - Reproduction
                    board[row][col] = 1
                else:
                    board[row][col] = 0

def main():
    # Create an instance of Solution
    sol = Solution()

    # Define the board
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    # Call the gameOfLife method
    sol.gameOfLife(board)

    # Print the resulting board
    for row in board:
        print(row)

if __name__ == "__main__":
    main()
