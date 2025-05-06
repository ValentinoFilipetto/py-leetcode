from typing import List

# Pattern: Hash Map
# Time complexity = O(n)
# Space complexity = O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[num] = i
