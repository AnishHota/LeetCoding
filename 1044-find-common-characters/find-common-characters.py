class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        ans = Counter(words[0])
        for x in words:
            temp = Counter(x)
            ans = ans & temp
                  
        sol = []
        for k,v in ans.items():
            for _ in range(v):
                sol.append(k)
        
        return sol

        