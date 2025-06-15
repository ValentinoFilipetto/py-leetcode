# Pattern: Stack
# Time complexity: O(n) for pop and peek, O(1) for push and empty
# Space complexity: O(n) for stack1 and stack2


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        res = None

        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        res = self.stack2.pop()

        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return res

    def peek(self) -> int:
        res = None

        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        res = self.stack2[-1]  # peek

        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        self.stack2 = []
        return res

    def empty(self) -> bool:
        return len(self.stack1) == 0
