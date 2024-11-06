class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax, cmax, cmin,pbit = 0,0,0,0
        for v in nums:
            cbit = v.bit_count()
            if cbit == pbit:
                cmin = min(cmin,v)
                cmax = max(cmax,v)
            elif cmin<pmax:
                return False
            else:
                pmax = cmax
                cmin = cmax = v
                pbit = cbit
        
        return cmin>=pmax