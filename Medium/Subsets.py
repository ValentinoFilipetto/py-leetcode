from typing import List

# Pattern: backtracking (DFS)
# Time complexity:
# Space complexity:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to add the number
            subset.append(nums[i])
            dfs(i + 1)

            # decision to NOT add the number
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
