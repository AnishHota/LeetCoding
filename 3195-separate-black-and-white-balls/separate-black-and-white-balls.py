class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        n = len(s)
        while i<n and s[i]=='0':
            i+=1
        
        ans = 0
        for j in range(i,n):
            if s[j]=='0':
                ans += j-i
                i+=1

        return ans