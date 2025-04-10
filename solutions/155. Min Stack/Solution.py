class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        top = self.stack[-1] if self.stack else -1
        min_val = top[1] if isinstance(top, tuple) else float('inf')
        if val < min_val:
            min_val = val
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
