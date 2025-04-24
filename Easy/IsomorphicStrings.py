from collections import defaultdict

# Pattern: Hash Map
# Time complexity: O(n^2)
# Space complexity: O(n)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = defaultdict(str)
        res = ""

        for i in range(0, len(s)):
            c1, c2 = s[i], t[i]

            if c2 in hashMap.values():
                continue
            hashMap[c1] = c2

        for i in range(0, len(s)):
            res += hashMap[s[i]]

        return res == t