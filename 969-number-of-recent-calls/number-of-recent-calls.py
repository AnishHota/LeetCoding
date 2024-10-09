class RecentCounter:

    def __init__(self):
        self.cnt = deque()

    def ping(self, t: int) -> int:
        i = 0
        while self.cnt and self.cnt[i]<(t-3000):
            self.cnt.popleft()
        self.cnt.append(t)
        return len(self.cnt)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)