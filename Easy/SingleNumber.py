from typing import List

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # because n ^ 0 = n, for any n.

        for num in nums:
            res ^= num

        return res
