from collections import defaultdict
from typing import Optional
from DataStructures import ListNode

# Pattern: Hash map
# Time complexity: O(m + n)
# Space complexity: O(m + n)


class HashMapSolution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        map = defaultdict(int)

        while headA:
            map[headA] += 1
            headA = headA.next

        while headB:
            map[headB] += 1
            headB = headB.next

        for node in map:
            if map[node] == 2:
                return node

        return None


# Pattern: Two pointers
# Time complexity: O(m + n)
# Space complexity: O(1)


class ConstantMemorySolution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        l1, l2 = headA, headB

        # Traverse both lists, when one pointer reaches the end, redirect it to the head of the other list
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1
