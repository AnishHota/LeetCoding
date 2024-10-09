class RecentCounter:

    def __init__(self):
        self.cnt = []

    def ping(self, t: int) -> int:
        count = 1
        i = len(self.cnt)-1
        while i>=0 and self.cnt[i]>=(t-3000):
            count+=1
            i-=1
        self.cnt.append(t)
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)