class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def getSteps(curr):
            a = curr
            b = curr+1
            steps = 0
            while a<=n:
                steps += min(n+1,b) - a
                a *= 10
                b *= 10
            return steps

        curr = 1
        k -= 1
        while k>0:
            steps = getSteps(curr)
            if steps<=k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr
                
            
