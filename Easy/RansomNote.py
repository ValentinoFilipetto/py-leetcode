from collections import defaultdict

# Pattern: Hash Map
# Time complexity: O(n + m)
# Space complexity: O(k), where k is the number of unique characters in magazine,
# (at most 26 for lowercase English letters, so effectively O(1) for English alphabet, but O(k) in general).


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_map = defaultdict(int)

        for letter in magazine:
            my_map[letter] += 1

        for letter in ransomNote:
            if letter in my_map and my_map[letter]:
                my_map[letter] -= 1
            else:
                return False

        return True
