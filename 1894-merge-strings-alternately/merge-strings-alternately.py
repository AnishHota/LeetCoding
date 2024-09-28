class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        n,m = len(word1),len(word2)
        ans = ""
        while i<n and j<m:
            ans+=word1[i]
            ans+=word2[j]
            i+=1
            j+=1
        
        if i<n:
            ans+=word1[i:]
        if j<m:
            ans+=word2[j:]
        return ans
        