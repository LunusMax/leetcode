from typing import List

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Split the string into words
        numbers = []
        s = s.split()

        # Extract numeric values from the string
        for char in s:
            if char.isnumeric():
                numbers.append(int(char))
        
        # Check if the numbers are in ascending order
        last_number = numbers[0]
        for num in numbers[1:]:
            if num > last_number:
                last_number = num
                continue
            else:
                return False
            
        return True

def main():
    # Create an instance of Solution
    sol = Solution()
    
    # Call the areNumbersAscending method and print the result
    answer = sol.areNumbersAscending("5 box has 3 blue 4 red 6 green and 12 yellow marbles")
    print(answer)  # Expected output: False

if __name__ == "__main__":
    main()
