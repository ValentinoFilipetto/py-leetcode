# Pattern: Iteration
# Time complexity: O(log n)
# Space complexity: O(1)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if the number is less than 1, it cannot be a power of 3
        if n == 1:
            return True
        while n > 3:
            n /= 3
        return n == 3
