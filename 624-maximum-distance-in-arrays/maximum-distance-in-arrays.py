class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNow, maxNow = arrays[0][0],arrays[0][-1]
        diff = 0
        for i,x in enumerate(arrays):
            if i!=0:
                diff = max(diff, max(abs(minNow-x[-1]),abs(maxNow-x[0])))
                minNow = min(minNow,x[0])
                maxNow = max(maxNow,x[-1])
        
        return diff


