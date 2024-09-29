class AllOne:

    def __init__(self):
        self.kv = defaultdict(int)
    
    def inc(self, key: str) -> None:
        self.kv[key]+=1
        

    def dec(self, key: str) -> None:
        self.kv[key]-=1
        if self.kv[key]==0:
            del self.kv[key]

    def getMaxKey(self) -> str:
        if not self.kv:
            return ""
        maxVal = max(self.kv.values())
        for k,v in self.kv.items():
            if v==maxVal:
                return k
        

    def getMinKey(self) -> str:
        if not self.kv:
            return ""
        minVal = min(self.kv.values())
        for k,v in self.kv.items():
            if v==minVal:
                return k


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()