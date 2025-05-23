from DataStructures import TreeNode

# Pattern: DFS
# Time complexity: O(n)
# Space complexity: O(h) for recursion stack, where h is the height of the tree

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or original == target: # if original is null, cloned will also be null
            return cloned

        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

