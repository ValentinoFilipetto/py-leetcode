from collections import deque
from typing import List, Optional
from DataStructures import TreeNode

# Pattern: BFS
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])

        if not root:
            return []

        res = [[root.val]]

        while q:
            nodes_visited = []
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    nodes_visited.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    nodes_visited.append(node.right.val)

            if len(nodes_visited) != 0:  # otherwise we would append "empty levels"
                res.append(nodes_visited)

        return res
