class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        ins = ""
        for x in s:
            ins += str(ord(x)-ord('a')+1)
        
        for _ in range(k):
            ans = 0
            for d in ins:
                ans += int(d)
            ins = str(ans)
        
        return ans
