class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        asci = []

        for i in range(len(s)):
            asci.append(abs(ord(s[i])-ord(t[i])))
        

        l=0
        cost = 0
        ans = 0
        for r in range(len(asci)):
            cost+=asci[r]
            if cost<=maxCost:
                ans = max(ans, r-l+1)
            else:
                while cost>maxCost:
                    cost-=asci[l]
                    l+=1
        
        return ans
