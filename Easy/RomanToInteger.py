# Pattern: Hash Table
# Time complexity = O(n)
# Space complexity = O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        i = 0

        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        while i < len(s):
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                integer += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
            else:
                integer += roman_to_int[s[i]]
                i += 1

        return integer
