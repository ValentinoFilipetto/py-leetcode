# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowelsFound = []
        index = 0
        res = ""

        for c in s:
            if c in vowels:
                vowelsFound.append(c)

        reversedVowelsFound = vowelsFound[::-1]

        for i in range(len(s)):
            if s[i] in vowels:
                res += reversedVowelsFound[index]
                index += 1
            else:
                res += s[i]

        return res