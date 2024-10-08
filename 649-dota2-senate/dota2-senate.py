class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i,x in enumerate(senate):
            if x=="R":
                r.append(i)
            if x=="D":
                d.append(i)
        
        n = len(senate)
        while r and d:
            if r[0]<d[0]:
                d.popleft()
                r.popleft()
                r.append(n)
            else:
                r.popleft()
                d.popleft()
                d.append(n)
            n+=1
        
        if r:
            return "Radiant"
        return "Dire"