# Are Numbers Ascending

## Problem Statement
Given a string `s` containing words and numbers, determine if the numbers are in ascending order. Only the numbers need to be validated, and the rest of the string can be ignored.

## Solution Approach

This solution verifies if the numbers within a given string are in strictly ascending order. Here is a step-by-step breakdown of the algorithm:

### Step 1: Split the String
The string `s` is split into individual words using the `split()` method. This allows easy iteration over each word in the string.

### Step 2: Extract Numbers
Iterate over each word in the split string and check if the word is numeric using the `isnumeric()` method. If a word is numeric, convert it to an integer and add it to the `numbers` list.

### Step 3: Check Ascending Order
- Initialize `last_number` with the first number in the `numbers` list.
- Iterate over the remaining numbers in the `numbers` list:
  - If the current number is greater than `last_number`, update `last_number` to the current number.
  - If the current number is not greater than `last_number`, return `False` immediately, indicating that the numbers are not in ascending order.
- If all numbers are in ascending order, return `True`.

### Complexity
- **Time Complexity**: O(N), where N is the length of the string. The string is split and iterated through once to extract the numbers and check their order.
- **Space Complexity**: O(N) for storing the numbers extracted from the string.

## Examples
**Example 1:**
Input:
```python
s = "1 box has 3 blue 4 red 5 green and 7 yellow marbles"
