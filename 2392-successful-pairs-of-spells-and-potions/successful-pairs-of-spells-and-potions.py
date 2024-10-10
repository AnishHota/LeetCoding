class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for i,x in enumerate(spells):
            a,b = 0,len(potions)-1
            ans = 0
            while a<=b:
                mid = (a+b)//2
                if potions[mid]*x >= success:
                    ans = max(ans,len(potions)-mid)
                    b = mid-1
                else:
                    a = mid+1
            res.append(ans)
        
        return res