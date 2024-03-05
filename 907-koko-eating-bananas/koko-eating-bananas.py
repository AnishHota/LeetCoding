class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ans = float('inf')
        if len(piles)==h:
            return max(piles)
        while l<=r:
            k = int(l+(r-l)/2)
            temph = 0
            for x in piles:
                temph += max(x//k if x%k==0 else (x//k)+1,1)
            if temph>h:
                l=k+1
            else:
                ans = min(ans,k)
                r=k-1
        return ans



