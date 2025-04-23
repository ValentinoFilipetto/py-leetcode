# Pattern: DP via hash map
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def fib(self, n: int) -> int:
        fibValues = {0 :0, 1: 1}

        def solver(n: int) -> int:
            if n in fibValues:
                return fibValues[n]

            fibValues[n] = solver(n - 1) + solver(n - 2)
            return fibValues[n]

        return solver(n)
