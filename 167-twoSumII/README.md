# Two Sum II

## Problem Statement
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. The answer should be returned as a list of the two indices (1-based indexing).

## Solution Approach

This solution uses the two-pointer technique to find the indices of the two numbers that add up to the target. Here is a step-by-step breakdown of the algorithm:

### Step 1: Initialize Two Pointers
Two pointers (left and right) are initialized at the beginning and end of the array.

### Step 2: Iterate Through the Array
For each step in the loop:
1. Calculate the sum of the values at left and right.
2. If the sum equals the target:
   - Return [left + 1, right + 1] (since the array is 1-indexed).
3. If the sum is less than the target, increment left to increase the sum.
4. If the sum is greater than the target, decrement right to decrease the sum.

### Step 3: Return the Result
The function returns once the correct pair is found. The problem guarantees exactly one solution.

### Complexity
- **Time Complexity**: O(n), where n is the number of elements in the array. The algorithm makes a single pass using two pointers.
- **Space Complexity**: O(1), since it uses only constant extra space.

## Examples
**Example 1:**
Input:
```python
nums = [2, 7, 11, 15]
target = 9

Output:
[1, 2]
