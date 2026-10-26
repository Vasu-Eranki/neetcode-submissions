class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_stack.append(val)
        else:
            current_min_value = self.min_stack[-1]
            self.min_stack.append(min(current_min_value,val))
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
