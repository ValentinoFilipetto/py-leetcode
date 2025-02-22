from collections import deque
from typing import Optional
from DataStructures import TreeNode

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None

        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    if node.val != node.left.val:
                        return False

                    q.append(node.left)
                if node.right:
                    if node.val != node.right.val:
                        return False

                    q.append(node.right)

        return True
