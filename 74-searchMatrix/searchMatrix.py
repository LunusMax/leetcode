from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # If the matrix is empty, return False
        if not matrix or not matrix[0]:
            return False
        
        # Define the number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # SOLUTION 1
        # Iterative Search (Complexity: O(m + n))
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1 # Move left
            else:
                row += 1 # Move down

        # SOLUTION 2
        # Binary Search (Complexity: O(log(m * n)))
        left = 0
        right = rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2

            # Find the element at mid index
            value_mid = matrix[mid // cols][mid % cols]

            if value_mid == target:
                return True
            elif value_mid < target:
                left = mid + 1
            else:
                right = mid - 1
                     
        return False

def main():
    # Create an instance of Solution
    sol = Solution()
    
    # Call the searchMatrix method and print the result
    resultado = sol.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3)
    print(resultado)  # Expected output: True

if __name__ == "__main__":
    main()
