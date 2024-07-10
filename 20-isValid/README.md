# Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{`, `'}'`, `'['`, and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## Solution Approach

This solution uses a stack to validate if the given string `s` has valid parentheses. Here is a step-by-step breakdown of the algorithm:

### Step 1: Initialize a Stack and a Dictionary
- Use a stack to keep track of opening brackets.
- Use a dictionary to map closing brackets to their corresponding opening brackets.

### Step 2: Iterate Through the String
- For each character in the string:
  - If the character is an opening bracket (`'('`, `'{'`, `'['`), push it onto the stack.
  - If the character is a closing bracket (`')'`, `'}'`, `']'`):
    - Check if the stack is empty or if the top element of the stack does not match the corresponding opening bracket. If either condition is true, return `False`.
    - Otherwise, pop the top element from the stack.

### Step 3: Check the Stack
- After processing all characters, check if the stack is empty. If it is empty, the string is valid; otherwise, it is not.

### Complexity
- **Time Complexity**: O(n), where n is the length of the string. Each character is processed once.
- **Space Complexity**: O(n), where n is the length of the string. In the worst case, the stack will store all opening brackets.

## Examples
**Example 1:**
Input:
```python
s = "()"
