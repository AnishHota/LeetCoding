class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def common(cnt1, cnt2):
            ans = {}
            for x in cnt1:
                if x in cnt2:
                    ans[x] = min(cnt1[x],cnt2[x])
            return ans
        
        ans = Counter(words[0])
        for x in words:
            temp = Counter(x)
            ans = common(ans,temp)
                  
        sol = []
        for k,v in ans.items():
            for _ in range(v):
                sol.append(k)
        
        return sol

        