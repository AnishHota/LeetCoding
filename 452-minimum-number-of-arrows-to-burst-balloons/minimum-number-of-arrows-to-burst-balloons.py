class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x: x[1])
        curr = points[0][1]
        res = 0
        for p in points[1:]:
            if p[0]>curr:
                res+=1
                curr = p[1]
            else:
                curr = min(curr,p[1])
        
        return res+1