class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.ms = maxSize
        self.inc =[0]*maxSize

    def push(self, x: int) -> None:
        if len(self.arr)<self.ms:
            self.arr.append(x)

    def pop(self) -> int:
        if not self.arr:
            return -1
        ind = len(self.arr)-1
        res = self.arr.pop()+self.inc[ind]
        if ind>0:
            self.inc[ind-1] += self.inc[ind]
        self.inc[ind] = 0
        return res

    def increment(self, k: int, val: int) -> None:
        n = min(len(self.arr)-1,k-1)
        if n>=0:
            self.inc[n] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)