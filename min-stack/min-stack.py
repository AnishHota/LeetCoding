class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append((val,val))
        else:
            self.min = min(val,self.stack[-1][1])
            self.stack.append((val,self.min))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack)==0:
            self.min = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return  self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()