from typing import List

# Pattern: Loops and Array Manipulation.
# Time complexity = O(n)
# Space complexity = O(1)

# The space complexity of this algorithm is considered "amortized O(1)" because,
# in most cases, the algorithm modifies the input list in place without allocating additional space.
# However, in specific edge cases (e.g., when all digits are 9), a new list of size n + 1 is created,
# which temporarily increases the space complexity to O(n).


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        if digits[0] == 0:
            res = [1]
            res.extend(digits)
            return res
