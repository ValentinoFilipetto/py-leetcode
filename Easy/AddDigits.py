# Pattern: ?
# Time complexity: O(d x log n)
# Space complexity: O(n)

# Explanation:
# String conversion: converting num to a string takes O(d) time, where d is the number of digits in num.
# Iteration: the for loop also takes O(d) time.
# Recursion: the function is called recursively; in each recursive call, the number of digits decreases significantly
# approximately by a factor of 10. Therefore, the number of recursive calls is O(log n), where n is the value of num.


class StringConversionSolution:
    def addDigits(self, num: int) -> int:
        numberAsString = str(num)
        res = 0

        for n in numberAsString:
            res += int(n)

        if res < 10:
            return res
        else:
            return self.addDigits(res)


# Time complexity: O(d x log n)
# Space complexity: O(n)


class NoStringConversionSolution:
    def addDigits(self, num: int) -> int:
        res = 0

        while num > 9:
            res += num % 10
            num /= 10

        res += num

        if res < 10:
            return res
        else:
            return self.addDigits(res)
