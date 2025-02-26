from typing import List

# Time complexity: O(m), where m is the length of nums1
# Space complexity: O(m)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hashSet = set(nums1)

        for num in hashSet:
            if num in nums2:
                res.append(num)

        return res