from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a hash table to store the numbers and their indices
        hash_table = {}
        n = len(nums)
        
        # Iterate through the array
        for i in range(n):
            # Calculate the complement of the current number
            complement = target - nums[i]
            
            # Check if the complement exists in the hash table
            if complement in hash_table:
                # If found, return the indices of the current number and the complement
                return [hash_table[complement], i]
            
            # Store the current number and its index in the hash table
            hash_table[nums[i]] = i

        # If no solution is found, return an empty list
        return [] 

def main():
    # Create an instance of Solution
    solution = Solution()
    
    # Define the input list and target
    nums = [2, 7, 11, 15]
    target = 17
    
    # Call the twoSum method and print the result
    print(solution.twoSum(nums, target))  # Expected output: [0, 3]

if __name__ == "__main__":
    main()
