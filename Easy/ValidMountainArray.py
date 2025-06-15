from typing import List

# Pattern: Iteration
# Time complexity: O(n), where n is the length of the array.
# Space complexity: O(1)


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0

        # Check for strictly increasing sequence
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == len(arr) - 1:
            return False

        # Check for strictly decreasing sequence
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

        return i == len(arr) - 1
