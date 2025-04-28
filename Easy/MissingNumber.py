from typing import List

# Pattern: Sorting
# Time complexity: O(n x log n)
# Space complexity: O(1)

class SortingSolution:
    def missingNumber(self, nums: List[int]) -> int:
        max_number = len(nums)

        nums.sort()

        if nums[-1] != max_number:
            return max_number

        if nums[0] != 0:
            return 0

        for i in range(0, max_number - 1):
            if nums[i + 1] > nums[i] + 1:
                return nums[i] + 1

# Pattern: bitwise operators (XOR)
# Time complexity: O(n)
# Space complexity: O(n)
# Intuitive idea: Imagine you have a range [0, n] and an array nums with one number missing.
# XOR all the numbers in the range and the array together:
# - Numbers that appear in both the range and the array cancel out.
# - The missing number is the only one left because it does not have a counterpart in the array.

class XorSolution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = 0

        # It accumulates the XOR of all the elements in the array.
        # This step effectively "marks" all the numbers present in the array.
        for num in nums:
            missing_number = missing_number ^ num
        # All the numbers in the array will cancel out their counterparts in the range from 0 to n.
        # The only number that will remain is the missing number.
        for num in range(len(nums) + 1):
            missing_number = missing_number ^ num

        return missing_number
