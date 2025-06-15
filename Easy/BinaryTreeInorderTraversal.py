from typing import List, Optional
from DataStructures import TreeNode

# Pattern: DFS
# Time complexity = O(n)
# Space complexity = O(n)


class RecursiveDfsSolution:
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


# Time complexity = O(n)
# Space complexity = O(n)


class IterativeDfsSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
