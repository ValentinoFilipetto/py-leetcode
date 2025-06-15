# Pattern: Stack
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, c in enumerate(s):
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif c == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            elif c == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
