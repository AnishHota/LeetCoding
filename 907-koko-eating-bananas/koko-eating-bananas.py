class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        if len(piles)==h:
            return max(piles)
        while l<=r:
            k = int(l+(r-l)/2)
            temph = 0
            for x in piles:
                temph += math.ceil(x/k)
            if temph>h:
                l=k+1
            else:
                r=k-1
        return l



