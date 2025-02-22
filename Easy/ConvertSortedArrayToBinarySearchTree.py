from typing import List, Optional

# Time complexity: O(n)
# Space complexity: O(log n), as we consider the height of the returned tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l, r):
            m = l + ((r - l) // 2)
            root = TreeNode(nums[m])

            if l <= r:
                root.left = helper(l, m - 1)
                root.right = helper(m + 1, r)
            else:
                return None

            return root

        return helper(0, len(nums) - 1)
