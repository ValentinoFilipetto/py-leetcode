from typing import List

# Pattern: Two Pointers
# Time complexity = O(n)
# Space complexity = O(1), as we modify the array in place.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # number of unique elements

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l

