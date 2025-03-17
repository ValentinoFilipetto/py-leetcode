from typing import List

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, h = 0, len(s) - 1

        while l <= h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1

        return s