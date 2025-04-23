# Pattern: Sliding window
# time complexity = O(m * n)
# space complexity = O(1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return -1

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                elif j == len(needle) - 1:
                    return i
        return -1
