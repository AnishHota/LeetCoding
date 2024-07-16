class LinkedList():

    def __init__(self,key,val,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedList(-1,-1)
        self.tail = LinkedList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.has = {}

    def deleteNode(self,node):
        prevn = node.prev
        nextn = node.next
        prevn.next = nextn
        nextn.prev = prevn
        del self.has[node.key]
    
    def addNode(self,node):
        prevn = self.tail.prev
        prevn.next = node
        node.prev = prevn
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.has:
            value = self.has[key].val
            curr = LinkedList(key,value)
            self.deleteNode(self.has[key])
            self.has[key]=curr
            self.addNode(curr)
            return value
            
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.has:
            self.deleteNode(self.has[key])
            self.has[key] = LinkedList(key,value)
            self.addNode(self.has[key])
        else:
            if len(self.has)==self.capacity:
                self.deleteNode(self.head.next)
            
            self.has[key] = LinkedList(key,value)
            self.addNode(self.has[key])
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)