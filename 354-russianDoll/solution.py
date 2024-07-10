from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes by width in ascending order (if same width, by height in descending order)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract the heights from the sorted envelopes
        heights = [envelope[1] for envelope in envelopes]

        # Dynamic Programming with Binary Search to find the longest increasing subsequence of heights
        dp = []
        for h in heights:
            bisect = bisect_left(dp, h)
            if bisect == len(dp):
                dp.append(h)
            else:
                dp[bisect] = h

        return len(dp)

def main():
    # Create an instance of Solution
    sol = Solution()
    
    # Call the maxEnvelopes method and print the result
    resultado = sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
    print(resultado)  # Expected output: 3

if __name__ == "__main__":
    main()
