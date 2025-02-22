from typing import List, Optional
from DataStructures import TreeNode

# Time complexity = O(n)
# Space complexity = O(n)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
