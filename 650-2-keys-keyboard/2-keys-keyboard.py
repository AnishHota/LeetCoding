class Solution:
    def minSteps(self, n: int) -> int:

        factor = 2
        ans = 0
        while n>1:
            while n%factor==0:
                ans += factor
                n/=factor
            factor+=1
        
        return ans