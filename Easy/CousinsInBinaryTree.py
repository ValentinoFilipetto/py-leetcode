# Definition for a binary tree node.
from collections import deque
from typing import Optional

# Time complexity: O(n)
# Space complexity: O(1)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        parents = []

        if not root:
            return 0

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                    if node.left.val == x or node.left.val == y:
                        parents.append(node.val)

                if node.right:
                    q.append(node.right)

                    if node.right.val == x or node.right.val == y:
                        parents.append(node.val)

            if len(parents) < 2:
                parents = []

            if len(parents) == 2 and parents[0] != parents[1]:
                return True

        return False
