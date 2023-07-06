class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key in self.timemap.keys():
            for x in range(len(self.timemap[key])-1,-1,-1):
                if self.timemap[key][x][1]<=timestamp:
                    value=self.timemap[key][x][0]
                    return value

        return value 



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)