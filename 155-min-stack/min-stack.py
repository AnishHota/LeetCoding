class MinStack:

    def __init__(self):
        self.stack = []
        self.minN = float('inf')

    def push(self, val: int) -> None:
        if val<self.minN or not self.stack:
            self.stack.append((val,val))
            self.minN = val
        else:
            self.stack.append((val,self.stack[-1][1]))
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minN = self.stack[-1][1]
        else:
            self.minN = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()