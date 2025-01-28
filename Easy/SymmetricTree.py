# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

        return sameTree(root.left, root.right)
