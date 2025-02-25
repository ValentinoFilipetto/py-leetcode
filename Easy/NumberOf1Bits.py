# Explanation: if n is a binary number, n % 2 = 1 if the rightmost digit in n
# is one, else it is 0. To count all the 1s, we shift n by one position
# at every iteration, i.e. n = n >> 1

# Time complexity: O(1)
# Space complexity: O(1)

# as n is always a 32-bit integer, hence the while loop will
# always run at most 32 times.


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n % 2
            n = n >> 1

        return count
