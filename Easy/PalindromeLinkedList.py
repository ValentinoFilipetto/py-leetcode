from typing import Optional
from DataStructures import ListNode

# Pattern: Two Pointers
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []

        if not head:
            return False

        while head:
            res.append(head.val)
            head = head.next

        for i in range(len(res) // 2):
            if res[i] != res[len(res) - 1 - i]:
                return False

        return True
