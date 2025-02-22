from collections import deque
from typing import List, Optional
from DataStructures import TreeNode

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        print(q)

        if not root:
            return []

        res = [[root.val]]

        while q:
            to_append = []
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    to_append.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    to_append.append(node.right.val)

            if len(to_append) != 0:
                res.append(to_append)

        return res
