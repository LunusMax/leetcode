# Max Envelopes

## Problem Statement
Given a number of envelopes with widths and heights, find the maximum number of envelopes you can Russian doll (i.e., put one inside the other). An envelope `[i]` can fit into another envelope `[j]` if both the width and height of envelope `[i]` are smaller than those of envelope `[j]`.

Link to the problem: [Max Envelopes on LeetCode](https://leetcode.com/problems/russian-doll-envelopes/)

## Solution Approach

This solution finds the maximum number of envelopes that can be nested within each other by using a combination of sorting and dynamic programming (DP) with binary search. Here is a step-by-step breakdown of the algorithm:

### Step 1: Sort Envelopes
First, the envelopes are sorted by their widths in ascending order. If two envelopes have the same width, they are sorted by their heights in descending order. This ensures that envelopes with the same width cannot be nested within each other, avoiding conflicts during the DP process.

### Step 2: Extract Heights
After sorting, only the heights of the envelopes are considered for the dynamic programming part. This reduces the problem to finding the longest increasing subsequence (LIS) of heights, since widths are already sorted.

### Step 3: Dynamic Programming with Binary Search
The algorithm maintains a dynamic programming list (`dp`) to keep track of the LIS of heights:
- For each height, use binary search (`bisect_left`) to determine its position in the `dp` list.
- If the height is larger than all elements in `dp`, it is appended to the end of the list.
- Otherwise, replace the existing element at the found position with the current height to maintain the smallest possible values in `dp`.

### Complexity
- **Time Complexity**: O(n log n), where n is the number of envelopes. Sorting takes O(n log n), and each insertion in the `dp` list takes O(log n) due to binary search.
- **Space Complexity**: O(n), for storing the heights and the dynamic programming list.

## Examples
**Example 1:**
Input:
```python
envelopes = [[5,4],[6,4],[6,7],[2,3]]
