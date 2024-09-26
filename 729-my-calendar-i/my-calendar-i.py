class TreeNode:
    def __init__(self,s,e):
        self.s = s
        self.e = e
        self.l = None
        self.r = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start,end)
            return True
        return self.insert(self.root,start,end)
    
    def insert(self,node,start,end):
        if start>=node.e:
            if node.r:
                return self.insert(node.r,start,end)
            node.r = TreeNode(start,end)
            return True
        elif end<=node.s:
            if node.l:
                return self.insert(node.l,start,end)
            node.l = TreeNode(start,end)
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)