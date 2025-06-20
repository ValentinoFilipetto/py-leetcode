# Definition for a binary tree node.
from collections import deque
from typing import Optional
from DataStructures import TreeNode

# Pattern: BFS
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        parents = []

        if not root:
            return False

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

            if (
                len(parents) == 2 and parents[0] != parents[1]
            ):  # To be cousins, they must have same depth and different parents
                return True

        return False
