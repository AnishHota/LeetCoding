class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [-1]*k
        self.head = -1
        self.tail = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.insert(0,value)
        self.arr.pop()
        if self.head==-1:
            self.head = 0
        self.tail+=1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[0]=value
            self.head=self.tail=0
        else:
            self.arr[self.tail+1]=value
            self.tail+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        del self.arr[0]
        self.arr.append(-1)
        if self.arr[0]==-1:
            self.head=-1
        self.tail-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.tail]=-1
        if self.head==self.tail:
            self.head=self.tail=-1
        else:
            self.tail-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        if self.head==-1:
            return True
        return False

    def isFull(self) -> bool:
        if self.tail!=-1 and self.head!=-1 and self.tail-self.head+1==len(self.arr):
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()