from typing import Optional
from DataStructures import TreeNode

# Pattern: DFS
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
