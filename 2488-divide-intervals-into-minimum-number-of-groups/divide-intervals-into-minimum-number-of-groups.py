class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        times = [(x[0],1) for x in intervals]
        times += [(x[1],-1) for x in intervals]
        times = sorted(times,key=lambda x: x[0])
        cnt = 0
        res = 0
        for x,s in times:
            cnt += s
            res = max(cnt,res)
        
        return res