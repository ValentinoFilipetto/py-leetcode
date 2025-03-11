# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def addDigits(self, num: int) -> int:
        numberAsString = str(num)
        res = 0

        for n in numberAsString:
            res += int(n)

        if res < 10:
            return res
        else:
            return self.addDigits(res)