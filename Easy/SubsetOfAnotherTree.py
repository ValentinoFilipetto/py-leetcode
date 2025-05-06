from typing import Optional
from DataStructures import TreeNode

# Pattern: DFS
# Time complexity: O(n * m) where n is the number of nodes in the main tree and m is the number of nodes in the subtree.
# Space complexity: O(h) where h is the height of the main tree due to recursion stack.


class Solution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
