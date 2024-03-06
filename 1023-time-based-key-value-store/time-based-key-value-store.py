from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:       
            self.timemap[key].append((timestamp,value))
        else:
            self.timemap[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        l,r = 0, len(self.timemap.get(key,[]))-1
        while l<=r:
            mid = int(l+(r-l)/2)
            if timestamp>=self.timemap[key][mid][0]:
                ans = self.timemap[key][mid][1]
                l=mid+1
            else:
                r=mid-1
        return ans




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)