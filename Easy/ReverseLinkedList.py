from typing import Optional
from DataStructures import ListNode

# Pattern: Sorting
# Time complexity: O(n)
# Space complexity O(n)


class LinearSpaceSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array_of_nodes = []
        my_linked_list = ListNode(0)
        res = my_linked_list

        while head:
            array_of_nodes.append(head.val)
            head = head.next

        reversedArray = array_of_nodes[::-1]

        for val in reversedArray:
            my_linked_list.next = ListNode(val)
            my_linked_list = my_linked_list.next

        return res.next


# Pattern: Two Pointers
# Time complexity: O(n)
# Space complexity O(1)


class ConstantSpaceSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


# Recursive solution: to be added
