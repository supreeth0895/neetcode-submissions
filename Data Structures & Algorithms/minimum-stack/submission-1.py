class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_val[-1] if self.min_val else val)
        self.min_val.append(min_val)

    def pop(self) -> None:
        self.min_val.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]