class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        l,r = 0,1
        prof = 0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
            else:
                prof = max(prices[r]-prices[l],prof)
            r+=1
        return prof
            