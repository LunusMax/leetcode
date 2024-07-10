# Smallest Number

## Problem Statement
Given an integer `num`, rearrange its digits to form the smallest possible number. If the number is negative, rearrange its digits to form the smallest possible negative number.

## Solution Approach

This solution rearranges the digits of the given integer to form the smallest possible number, handling both positive and negative numbers. Here is a step-by-step breakdown of the algorithm:

### Step 1: Check if the Number is Negative
- If the number is negative, make it positive and set a flag to remember that it was originally negative.

### Step 2: Convert the Number to a String and then to a List of Digits
- Convert the number to a string to iterate over each digit.
- Convert each character back to an integer and store it in a list.

### Step 3: Sort the Digits
- If the number is negative, sort the digits in descending order.
- If the number is positive, sort the digits in ascending order.

### Step 4: Handle Leading Zeros for Positive Numbers
- If the number is positive and the smallest digit is zero, find the first non-zero digit and swap it with the zero.

### Step 5: Convert the List of Digits Back to a Number
- Convert the list of digits back to a string and then to an integer.

### Step 6: Restore the Negative Sign if Necessary
- If the number was originally negative, add the negative sign back.

### Complexity
- **Time Complexity**: O(n log n), where n is the number of digits in the number. The sorting operation dominates the complexity.
- **Space Complexity**: O(n) for storing the digits of the number.

## Examples
**Example 1:**
Input:
```python
num = 310
