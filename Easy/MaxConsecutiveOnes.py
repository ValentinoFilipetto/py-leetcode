from typing import List

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, tmp = 0, 0

        for num in nums:
            if num == 1:
                count += 1
                continue
            elif num == 0:
                if count > tmp:
                    tmp = count
                count = 0
            
        return max(tmp, count)