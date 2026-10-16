# Min Stack
# status: solo | retry: -
# note: retry passed; switched from min indices to a value-based min stack with an inf sentinel (no empty check);
# push on >= so duplicate mins survive a pop

class MinStack:

    def __init__(self):
        inf = float('inf')
        self.st = []
        self.mins = [inf]

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.mins[-1] >= val:
            self.mins.append(val) 

    def pop(self) -> None:
        n = self.st.pop()
        if n == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mins[-1]
