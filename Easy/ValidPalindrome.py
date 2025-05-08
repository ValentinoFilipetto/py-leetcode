# Pattern: Two Pointers
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        cleaned_string = "".join([char for char in s.lower() if char in alphanumeric])

        if len(cleaned_string) == 0:
            return True

        reversed_cleaned_string = cleaned_string[::-1]

        for j in range(len(cleaned_string)):
            if cleaned_string[j] != reversed_cleaned_string[j]:
                return False

        return True
