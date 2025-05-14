# Pattern: Math + HashMap
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def titleToNumber(self, columnTitle):
        res = 0
        letter_to_number = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

        reversed_column_title = columnTitle[::-1]

        # we start from index 1 because 26 ** 0 = 1
        for i in range(1, len(reversed_column_title)):
            letter_as_number = letter_to_number[reversed_column_title[i]]
            res += letter_as_number * (26 ** i)

        return res + letter_to_number[reversed_column_title[0]]
