class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # List digits of the number
        digits = []
        temp = x  # Use a temporary variable to avoid modifying x
        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            temp = temp // 10

        # Create a list of reversed digits
        digits_reversed = digits[::-1]

        # Compare lists
        for i in range(len(digits)):
            if digits[i] != digits_reversed[i]:
                return False
        return True

def main():
    # Create an instance of Solution
    sol = Solution()

    # Test the isPalindrome method with an example
    number = 121
    result = sol.isPalindrome(number)
    print(f"The number {number} is a palindrome: {result}")  # Expected output: True

    # Additional test cases
    number = -121
    result = sol.isPalindrome(number)
    print(f"The number {number} is a palindrome: {result}")  # Expected output: False

    number = 10
    result = sol.isPalindrome(number)
    print(f"The number {number} is a palindrome: {result}")  # Expected output: False

    number = 1221
    result = sol.isPalindrome(number)
    print(f"The number {number} is a palindrome: {result}")  # Expected output: True

if __name__ == "__main__":
    main()
