from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        longestArray = []
        shortestArray = []

        if len(nums1) > len(nums2):
            longestArray = nums1
            shortestArray = nums2
        elif len(nums2) > len(nums1):
            longestArray = nums2
            shortestArray = nums1
        else:
            longestArray = nums1
            shortestArray = nums2

        for num in longestArray:
            if num in shortestArray:
                res.append(num)
                shortestArray.remove(num)

        return res
