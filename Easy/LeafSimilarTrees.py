from typing import Optional
from DataStructures import TreeNode

# Pattern: DFS
# Time complexity: O(n + m)
# Space complexity: O(n + m)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_sequence1, leaf_sequence2 = [], []

        def dfs(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)

            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(root1, leaf_sequence1)
        dfs(root2, leaf_sequence2)

        return leaf_sequence1 == leaf_sequence2
