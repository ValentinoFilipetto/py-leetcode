import math

# Pattern: Math
# Time complexity: O(sqrt(n))
# Space complexity: O(1)

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 5:
            return False

        sum = 1
        # The loop iterates from 2 to the square root of num (inclusive). This is because divisors come in pairs,
        # e.g. for 28 divisors are (1, 28), (2, 14), (4, 7), and one of the divisors in each pair is always less than
        # or equal to the square root of num.
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                # if i divides num evenly, then both i and num // i are divisors of num.
                sum += i + num // i

        return sum == num