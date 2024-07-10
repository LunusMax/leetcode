from typing import List

class Solution:
    def smallestNumber(self, num: int) -> int:

        if num < 0:
            is_negative = True
            num = -num
        else:
            is_negative = False
        
        string = str(num)
        nums = [int(i) for i in string]

        if is_negative:
            nums = sorted(nums, reverse=True)
        else:
            nums = sorted(nums)

        if not is_negative and nums[0] == 0:
            for i in range(1, len(nums)):
                if nums[i] != 0:
                    nums[0], nums[i] = nums[i], nums[0]
                    break
        
        final_answer = int(''.join(map(str, nums)))
        
        if is_negative:
            final_answer = -final_answer

        return final_answer

def main():
    # Create an instance of Solution
    sol = Solution()

    # Call the smallestNumber method and print the result
    answer = sol.smallestNumber(310)
    print(answer)  # Expected output: 103

if __name__ == "__main__":
    main()
