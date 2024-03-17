class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i,x in enumerate(intervals):
            if newInterval[0]>x[1]:
                ans.append(x)
            elif newInterval[1]<x[0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            else:
                newInterval = [min(newInterval[0],x[0]),max(newInterval[1],x[1])]
        ans.append(newInterval)
        return ans
