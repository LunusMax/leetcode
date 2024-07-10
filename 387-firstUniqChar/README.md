# First Unique Character in a String

## Problem Statement
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## Solution Approach

This solution provides three methods for finding the first unique character in a string. Here is a step-by-step breakdown of each algorithm:

### Solution 1: Quadratic Complexity (O(n^2))
1. Iterate through each character in the string.
2. For each character, check the remaining characters in the string to see if it repeats.
3. If a character does not repeat, return its index.
4. If no unique character is found, return `-1`.

### Solution 2: Linear Complexity Using Hash Table (O(n))
1. Create a dictionary to count occurrences of each character.
2. Iterate through the string, updating the dictionary with character counts.
3. Iterate through the string again, checking the dictionary for the first character with a count of `1`.
4. Return the index of the first unique character.
5. If no unique character is found, return `-1`.

### Solution 3: Linear Complexity Using Array (O(n))
1. Define a function to get the position of a character relative to 'a'.
2. Create an array to count occurrences of each character.
3. Iterate through the string, updating the array with character counts.
4. Iterate through the string again, checking the array for the first character with a count of `1`.
5. Return the index of the first unique character.
6. If no unique character is found, return `-1`.

### Complexity
- **Time Complexity**:
  - Solution 1: O(n^2)
  - Solution 2: O(n)
  - Solution 3: O(n)
- **Space Complexity**:
  - Solution 1: O(1)
  - Solution 2: O(n)
  - Solution 3: O(1)

## Examples
**Example 1:**
Input:
```python
s = "leetcode"
