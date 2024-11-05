class Solution:
    def minChanges(self, s: str) -> int:
        s = [int(x) for x in s]

        if sum(s)==0 or sum(s)==len(s):
            return 0
        
        count = 0

        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                count+=1
        
        return count