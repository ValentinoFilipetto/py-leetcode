from typing import Optional
from DataStructures import TreeNode

# Pattern: DFS
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
