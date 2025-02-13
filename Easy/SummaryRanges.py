from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        if not nums:
            return res

        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                if i < len(nums):
                    start = nums[i]

        return res
