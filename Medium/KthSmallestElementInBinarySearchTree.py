from collections import deque
from typing import Optional
from DataStructures import TreeNode

# Pattern: BFS
# Time complexity: O(n log n), because of sorting of the list of nodes.
# Space complexity: O(n)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        list_of_nodes = [root.val]

        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    list_of_nodes.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    list_of_nodes.append(node.right.val)

        list_of_nodes.sort()

        return list_of_nodes[k - 1]
