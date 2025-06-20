from typing import List

# Pattern: Backtracking (DFS)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        rem = nums[:]

        def dfs(stack, rem):
            if not rem:
                res.append(stack.copy())
                return

            for i in range(len(rem)):
                stack.append(rem[i])
                dfs(stack, rem[:i] + rem[i + 1 :])
                stack.pop()

        dfs(stack, rem)
        return res
