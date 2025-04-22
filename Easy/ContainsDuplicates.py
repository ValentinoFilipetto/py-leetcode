from typing import List

# PATTERN: Sliding Window
# Time complexity: O(n log n), because of sorting
# Space complexity: O(1)


class SortingSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(0, len(nums) - 1):

            if nums[i] == nums[i + 1]:
                return True

        return False

# PATTERN: Hash set
# Time complexity: O(n), since set lookup is O(1) in Python due to hash set implementation
# Space complexity: O(n)


class SetSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            if num in my_set:
                return True

            my_set.add(num)

        return False
