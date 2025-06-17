from typing import List

# Pattern: Backtracking
# How backtracking works:
# - build a solution step by step (often recursively)
# - at each step, make a choice from a set of options
# - if a choice leads to a valid solution, continue
# - if a choice leads to a dead end (violates constraints), undo the last choice (backtrack) and try another option
# - repeat until all possibilities are explored.

# Time complexity: O(4^n / sqrt(n))
# The number of valid parentheses combinations for n pairs is the nth Catalan number, which grows as O(4^n / sqrt(n)).
# Space complexity: O(4^n / sqrt(n))
#  - For storing all valid combinations in the result list (output space).
#  - The recursion stack can go as deep as 2n, but the dominant space is for storing results.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_n, closed_n, stack):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n, stack)
                stack.pop()

            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1, stack)
                stack.pop()

        backtrack(0, 0, stack)
        return res
