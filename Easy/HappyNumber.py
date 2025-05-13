# Intuition: if, in the process of calculating the sum of squares of digits, we encounter a number that we have seen before, then we are in a cycle and the number is not happy.
# Pattern: Hash Set

# Time complexity: O(k * log n)
# k is the number of unique numbers encountered before either reaching 1 or entering a cycle, and the number of digits in n is proportional to log n

# Space complexity: O(k), k is the number of unique numbers encountered before either reaching 1 or entering a cycle.
# k is bounded by number of unique sums of squares, which is small (typically less than 243 for integers, so it is also bounded).


class Solution(object):
    def isHappy(self, n):
        numbers_so_far = set()

        while n != 1:
            res = 0

            for d in str(n):
                res += int(d) * int(d)

            if res in numbers_so_far:
                return False

            numbers_so_far.add(res)
            n = res

        return True