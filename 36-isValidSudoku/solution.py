from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Create sets for the elements
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Traverse the elements
        for i in range(9):
            for j in range(9):

                # Define element
                element = board[i][j]

                # Skip "."
                if element == '.':
                    continue

                # Check if the number already exists in the row, column, or box
                if element in rows[i]:
                    return False
                
                if element in columns[j]:
                    return False
                
                # Determine the index of each box
                box_index = (i // 3) * 3 + (j // 3)
                if element in boxes[box_index]:
                    return False
                
                # Add the tested integer to the sets
                rows[i].add(element)
                columns[j].add(element)
                boxes[box_index].add(element)
        
        # If no duplicate was found
        return True


# Solution instance
sol = Solution()

# Call and print the result
result = sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".","8","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(result)
