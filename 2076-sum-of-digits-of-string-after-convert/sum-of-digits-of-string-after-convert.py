class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        ins = ""
        for x in s:
            ins += str(ord(x)-ord('a')+1)
        
        ins = int(ins)
        while k>0:
            k-=1
            ans = 0
            while ins>0:
                ans += ins%10
                ins = ins//10
            ins = ans
        
        return ans
