from typing import List

class Solution:
    """ Class to check if a given sudoku board is valid. """
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        
        Args:
        board (List[List[str]]): The 9x9 Sudoku board.
        
        Returns:
        bool: True if the board is valid, False otherwise.
        """
        rows, columns, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == '.':
                    continue
                if element in rows[i] or element in columns[j] or element in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                rows[i].add(element)
                columns[j].add(element)
                boxes[(i // 3) * 3 + (j // 3)].add(element)
        
        return True

if __name__ == "__main__":
    sol = Solution()
    result = sol.isValidSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])
    print(result)
