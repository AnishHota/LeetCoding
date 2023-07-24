class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        d = [False]*(len(s)+1)
        d[0]=True
        for i in range(len(s)):
            if d[i]:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict:
                        d[j+1]=True
        
        return d[-1]