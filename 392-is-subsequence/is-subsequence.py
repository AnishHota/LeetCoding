class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not s:
            return True
        if s==t:
            return True
        if not t:
            return False
        for j in range(len(t)):
            if s[i]==t[j]:
                i+=1
            if i==len(s):
                return True
        
        return False