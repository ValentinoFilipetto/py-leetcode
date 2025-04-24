from typing import List

# Pattern: Horizontal Scanning
# time complexity = O(m x n) where m is the length of the shortest string and n is number of strings.
# space complexity = O(m), where m is the length of the shortest string in strs.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i + 1 > len(strs[j]) or strs[0][i] != strs[j][i]:
                    return res

            res += strs[0][i]

        return res
