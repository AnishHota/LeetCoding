class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def backtrack(i):
            if i==len(s):
                ans.append(' '.join(cur))
                return

            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
            return
        
        cur = []
        ans = []
        backtrack(0)
        
        return ans

            