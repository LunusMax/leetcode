# Search Matrix

## Problem Statement
Given an `m x n` matrix where each row is sorted in ascending order from left to right, and each column is sorted in ascending order from top to bottom, write an efficient algorithm that searches for a target value in the matrix. The function returns `true` if the target is found, otherwise `false`.

## Solution Approach

This solution provides two methods for searching the target in the matrix. Here is a step-by-step breakdown of the algorithm:

### Step 1: Check for Empty Matrix
Before proceeding with the search, the algorithm checks if the matrix is empty. If the matrix is empty or the first row is empty, it returns `false` immediately.

### Step 2: Define Matrix Dimensions
The number of rows and columns in the matrix are determined.

### Solution 1: Iterative Search (O(m + n))
1. Initialize `row` to 0 and `col` to the last column index (`cols - 1`).
2. Use a while loop to traverse the matrix:
   - If the current element (`matrix[row][col]`) is equal to the target, return `true`.
   - If the current element is greater than the target, move left by decrementing `col`.
   - If the current element is less than the target, move down by incrementing `row`.
3. If the target is not found after the loop, return `false`.

### Solution 2: Binary Search (O(log(m * n)))
1. Treat the matrix as a flattened array and use binary search.
2. Initialize `left` to 0 and `right` to `rows * cols - 1`.
3. Use a while loop to perform binary search:
   - Calculate the middle index (`mid`).
   - Determine the middle element (`value_mid`) in the matrix.
   - If `value_mid` is equal to the target, return `true`.
   - If `value_mid` is less than the target, move the `left` pointer to `mid + 1`.
   - If `value_mid` is greater than the target, move the `right` pointer to `mid - 1`.
4. If the target is not found, return `false`.

### Complexity
- **Time Complexity**: 
  - Iterative Search: O(m + n), where m is the number of rows and n is the number of columns.
  - Binary Search: O(log(m * n)).
- **Space Complexity**: O(1), no additional space is used.

## Examples
**Example 1:**
Input:
```python
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
