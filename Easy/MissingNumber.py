from typing import List

# Time complexity: O(nlog n)
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


# Time complexity: O(n)
# Space complexity: O(n)


class XorSolution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = 0

        for num in nums:
            missing_number = missing_number ^ num
        for num in range(len(nums) + 1):
            missing_number = missing_number ^ num

        return missing_number
