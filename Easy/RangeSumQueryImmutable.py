from typing import List

# Pattern: While loop
# Time complexity: O(n)
# Space complexity: O(1)

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        res = 0

        while left <= right:
            res += self.nums[left]
            left += 1

        return res