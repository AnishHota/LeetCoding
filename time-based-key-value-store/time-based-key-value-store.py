class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap.keys():
            arr = self.timemap[key]
            l = 0
            r =  len(arr)-1

            while l<=r:
                mid = (l+r)//2
                if arr[mid][0]==timestamp:
                    return arr[mid][1]
                elif arr[mid][0]<timestamp:
                    l=mid+1
                else:
                    r=mid-1
            return "" if l==0 else arr[l-1][1]
        
        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)