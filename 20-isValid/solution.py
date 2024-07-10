from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in brackets.values():  # If it's an opening bracket
                stack.append(char)
            elif char in brackets.keys():  # If it's a closing bracket
                if stack == [] or brackets[char] != stack.pop():
                    return False
            else:
                return False  # Invalid character
        
        return stack == []  # Ensure stack is empty at the end

def main():
    # Create an instance of Solution
    sol = Solution()

    # Call the isValid method and print the result
    resultado = sol.isValid("()")
    print(resultado)  # Expected output: True

    # Additional test cases
    print(sol.isValid("()[]{}"))  # Expected output: True
    print(sol.isValid("(]"))  # Expected output: False
    print(sol.isValid("([)]"))  # Expected output: False
    print(sol.isValid("{[]}"))  # Expected output: True

if __name__ == "__main__":
    main()
