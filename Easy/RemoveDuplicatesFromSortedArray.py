from typing import List

# time complexity = O(2N) os O(N)
# space complexity = O(1), as we sort in place.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l
