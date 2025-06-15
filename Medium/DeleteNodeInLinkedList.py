from DataStructures import ListNode

# Pattern: Linked List manipulation (in place)
# Time complexity: O(1)
# Space complexity: O(1)
# NB: it is guaranteed that the given node is not the last node in the linked list.


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
