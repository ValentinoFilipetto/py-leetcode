from collections import defaultdict

# Pattern: Hash map
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(
            int
        )  # this allows us to do count[letter] += 1, without checking for the existence of letter

        for letter in s:
            count[letter] += 1

        for i, letter in enumerate(s):
            if count[letter] == 1:
                return i

        return -1
