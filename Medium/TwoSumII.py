from typing import List

# Pattern: Two Pointers
# Time complexity: O(n)
# Space complexity: O(1)
# NB: Input array is sorted


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            add = numbers[l] + numbers[r]
            if add == target:
                return [l + 1, r + 1] # A solution is guaranteed, so we can return here. 
            elif add > target:
                r -= 1
            elif add < target:
                l += 1