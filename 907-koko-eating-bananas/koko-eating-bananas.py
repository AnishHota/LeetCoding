class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        ans = float(inf)

        while l<=r:
            k = int((r+l)/2)
            hrs = 0
            for p in piles:
                hrs += int(p/k) + (1 if p%k!=0 else 0)
            if hrs<=h:
                ans = min(ans,k)
                r=k-1
            else:
                l=k+1

        return ans