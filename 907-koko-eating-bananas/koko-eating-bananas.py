class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l<=r:
            k = int((r+l)/2)
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k)
            if hrs<=h:
                r=k-1
            else:
                l=k+1

        return l