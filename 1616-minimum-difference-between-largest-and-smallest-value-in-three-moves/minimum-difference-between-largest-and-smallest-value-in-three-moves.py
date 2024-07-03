class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        
        minH = sorted(heapq.nsmallest(4,nums))
        maxH = sorted(heapq.nlargest(4,nums))
        ans = float('inf')
        for i in range(4):
            x = minH[i]
            y = maxH[i]
            ans = min(ans,abs(x-y))

        return ans