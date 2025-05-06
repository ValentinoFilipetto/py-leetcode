from typing import List

# Pattern: Two Pointers
# Time complexity = O(n)
# Space complexity = O(n)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i, j = 0, len(nums) - 1

        while i <= j:
            if nums[i] ** 2 > nums[j] ** 2:
                res.append(nums[i] ** 2)
                i += 1
            else:
                res.append(nums[j] ** 2)
                j -= 1

        return res[::-1]
