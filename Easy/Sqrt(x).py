# Pattern: Binary Search
# Time complexity: O(log n)
# Space complexity: O(1)

# Idea: the integer square root to be found is the largest integer m such that m^2 ≤ x.

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)

            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m # keep track of the largest m such that m^2 <= x
            else:
                return m
        return res
