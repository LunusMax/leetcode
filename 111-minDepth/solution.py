from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

def main():
    # Create a sample binary tree
    # Example tree:
    #      1
    #     / \
    #    2   3
    #   / 
    #  4  
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    # Create an instance of Solution
    sol = Solution()

    # Call the minDepth method and print the result
    min_depth = sol.minDepth(root)
    print(f"The minimum depth of the binary tree is: {min_depth}")  # Expected output: 2

if __name__ == "__main__":
    main()
