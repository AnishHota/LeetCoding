from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap.keys():       
            self.timemap[key][0].append(timestamp)
            self.timemap[key][1].append(value)
        else:
            self.timemap[key]=[[timestamp],[value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap.keys():
            return ""
        l,r = 0, len(self.timemap[key][0])-1
        while l<=r:
            mid = int(l+(r-l)/2)
            if timestamp==self.timemap[key][0][mid]:
                return self.timemap[key][1][mid]
            elif timestamp>self.timemap[key][0][mid]:
                l=mid+1
            else:
                r=mid-1
        if r==-1:
            return ""
        return self.timemap[key][1][r]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)