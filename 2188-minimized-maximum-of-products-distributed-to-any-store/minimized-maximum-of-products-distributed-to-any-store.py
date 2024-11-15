class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l,r = 1,max(quantities)
        ans = float("inf")
        while l<=r:
            mid = (l+r)//2
            tot = 0
            for q in quantities:
                tot+=q//mid
                if q%mid:
                    tot+=1
            if tot<=n:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        
        return ans
