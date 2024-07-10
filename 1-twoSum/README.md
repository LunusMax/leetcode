# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## Solution Approach

This solution uses a hash table to find the indices of the two numbers that add up to the target. Here is a step-by-step breakdown of the algorithm:

### Step 1: Initialize a Hash Table
A hash table (dictionary in Python) is used to store the numbers and their indices as we iterate through the array.

### Step 2: Iterate Through the Array
For each element in the array:
1. Calculate the complement by subtracting the current element from the target.
2. Check if the complement exists in the hash table:
   - If it does, return the indices of the current element and the complement.
   - If it does not, store the current element and its index in the hash table.

### Step 3: Return the Result
If no solution is found by the end of the iteration, return an empty list (although the problem guarantees that a solution exists).

### Complexity
- **Time Complexity**: O(n), where n is the number of elements in the array. The algorithm iterates through the array once.
- **Space Complexity**: O(n), where n is the number of elements in the array. The hash table stores up to n elements.

## Examples
**Example 1:**
Input:
```python
nums = [2, 7, 11, 15]
target = 9
