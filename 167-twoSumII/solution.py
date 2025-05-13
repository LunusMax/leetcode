from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            
            if sum == target:
                ans = [left + 1, right + 1]
                return(ans)
                
            elif sum < target:
                left += 1
            else:   
                right -= 1


def main():
    # Create an instance of Solution
    solution = Solution()
    
    # Define the input list and target
    nums = [2, 7, 11, 15]
    target = 9
    
    # Call the twoSum method and print the result
    print(solution.twoSum(nums, target))  # Expected output: [0, 3]

if __name__ == "__main__":
    main()
