from typing import Optional
from DataStructures import TreeNode

# Intuition: because we are dealing with a BST, the inorder traversal will give us a sorted array of values.
# Pattern: DFS
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, min_diff = None, float('inf')

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            nonlocal prev, min_diff # otherwise, prev and min_diff will be treated as local variables
            if prev:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node

            dfs(node.right)

        dfs(root)
        return min_diff