from typing import List

# Pattern: Geometry
# Time complexity: O(1)
# Space complexity: O(1)


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Extract coordinates for better readability
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        a1, b1, a2, b2 = rec2[0], rec2[1], rec2[2], rec2[3]

        return (
            x1 < a2  # rec1's left edge is to the left of rec2's right edge
            and x2 > a1  # rec1's right edge is to the right of rec2's left edge
            and y1 < b2  # rec1's bottom edge is below rec2's top edge
            and y2 > b1
        )  # rec1's top edge is above rec2's bottom edge
