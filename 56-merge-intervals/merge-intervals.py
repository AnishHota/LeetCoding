class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals,key=lambda x:x[0])
        res = [(intervals[0])]
        for x,y in intervals[1:]:
            s,e = res[-1]
            if x<=e and y>=s:
                s,e = res.pop()
                res.append((min(s,x),max(y,e)))
            else:
                res.append((x,y))
        
        return res
        