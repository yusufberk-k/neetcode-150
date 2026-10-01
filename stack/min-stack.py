# Min Stack
# status: hint | retry: 2026-10-08
# note: single min var can't recover the previous min after pop; 
# keep a history of min indices (no sentinel, no duplicate state)

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minIns = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minIns) == 0:
            self.minIns.append(0)
        elif val <= self.stack[self.minIns[-1]]:               
            self.minIns.append(len(self.stack) - 1)

    def pop(self) -> None:
        if self.stack[self.minIns[-1]] == self.stack[-1]:
            self.minIns.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minIns[-1]]
