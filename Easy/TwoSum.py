from typing import List

# time complexity = O(N)
# space complexity = O(N)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[num] = i
