class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr, maxVal = 0,0
        for i in range(1,len(values)):
            curr = max(curr,values[i-1]+i-1)
            maxVal = max(maxVal,curr+values[i]-i)
        
        return maxVal