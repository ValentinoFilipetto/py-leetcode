from typing import List

# Pattern: Two Pointers
# Time complexity: O(n^2)
# Space complexity: O(n), as .sort() takes linear space.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            ## If nums[i - 1] was an `a` of a successful triplet,
            ## if we do not skip nums[i], we will add that very same triplet again.
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    ## this passage is necessary to avoid duplicate triplets.
                    ## At this point we already have [a, nums[l]]. If we were
                    ## to have [a, nums[l]] where nums[l] == nums[l - 1]
                    ## if there is nums[r] such that a + nums[l] + nums[r] == 0
                    ## that nums[r] will be unique, hence we would get a duplicate.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

