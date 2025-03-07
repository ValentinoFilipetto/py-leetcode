class Solution:
    def fib(self, n: int) -> int:
        fibValues = {0 :0, 1: 1}

        if n == 0:
            return 0

        if n == 1:
            return 1

        res1 = fibValues[n - 1] if n - 1 in fibValues.keys() else self.fib(n - 1)
        res2 = fibValues[n - 2] if n - 2 in fibValues.keys() else self.fib(n - 2)

        fibValues[n] = res1 + res2

        return res1 + res2
