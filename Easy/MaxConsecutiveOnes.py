from typing import List

# Pattern: Simple iteration with tracking
# Note: It is not Sliding Window because in the Sliding Window pattern,
# the window typically expands and contracts dynamically, with two pointers (start and end) explicitly managing the window's boundaries.

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, tmpCount = 0, 0

        for num in nums:
            if num == 1:
                count += 1
                continue
            elif num == 0:
                if count > tmpCount:
                    tmpCount = count
                count = 0

        return max(tmpCount, count)