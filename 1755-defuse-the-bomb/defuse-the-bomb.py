class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*(len(code))
        
        prefix = [0]
        n = len(code)
        code += code
        for x in code:
            prefix.append(x+prefix[-1])
        ans = []
        if k>0:
            for i in range(n):
                ans.append(prefix[i+1+k]-prefix[i+1])
            
        if k<0:
            for i in range(n):
                ans.append(prefix[n+i]-prefix[n+i+k])
        
        return ans

        