# Intuition: Instead of moving 0's to the end of the array, we move positive numbers to the front.
# Patter: Two Pointers
# Time complexity: O(n)
# Space complexity: O(1), as we change the array "in place"

class Solution(object):
    def moveZeroes(self, nums):
        l = 0

        for r in range(len(nums)):
            if nums[r]: # if nums[r] is positive, swap
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return nums