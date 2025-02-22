from collections import deque
from typing import Optional
from DataStructures import TreeNode

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 0

        if not root:
            return 0

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level
