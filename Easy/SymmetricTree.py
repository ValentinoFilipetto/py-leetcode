from typing import Optional
from DataStructures import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

        return sameTree(root.left, root.right)
