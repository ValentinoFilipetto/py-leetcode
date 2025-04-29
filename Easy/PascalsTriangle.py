from typing import List

# Pattern: DP
# Time complexity: O(n^2), where n is numRows. We have n rows and each row contains up to n elements.
# Space complexity: O(n^2), considering the final array


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(0, numRows):

            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                res.append([1])
                for j in range(0, len(res[i - 1])):
                    if j < len(res[i - 1]) - 1:
                        res[-1].append(res[i - 1][j] + res[i - 1][j + 1])
                res[-1].append(1)

        return res
