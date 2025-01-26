from typing import List

# time complexity = O(m * n)
# space complexity = O(1)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i + 1 > len(strs[j]) or strs[0][i] != strs[j][i]:
                    return res

            res += strs[0][i]

        return res
