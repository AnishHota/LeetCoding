class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}

        for i,x in enumerate(s):
            if x in hash and hash[x]!=t[i]:
                return False
            hash[x]=t[i]
        
        hash = {}
        for i,x in enumerate(t):
            if x in hash and hash[x]!=s[i]:
                return False
            hash[x]=s[i]
        
        return True
        