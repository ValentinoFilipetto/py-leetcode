from typing import List

# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def summaryRanges(self, nums):
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(nums[i]))

            i += 1

        return res
