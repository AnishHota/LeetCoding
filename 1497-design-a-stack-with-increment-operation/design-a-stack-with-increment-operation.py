class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.ms = maxSize

    def push(self, x: int) -> None:
        if len(self.arr)<self.ms:
            self.arr.append(x)

    def pop(self) -> int:
        if self.arr:
            return self.arr.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        n = min(len(self.arr),k)
        for i in range(n):
            self.arr[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)