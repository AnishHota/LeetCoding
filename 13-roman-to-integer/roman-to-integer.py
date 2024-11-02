class Solution:
    def romanToInt(self, s: str) -> int:
        dic ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        i = 0
        ans = 0
        while i<len(s):
            if s[i]=='I' and i+1<len(s) and s[i+1] in 'VX':
                ans += dic[s[i+1]]-dic[s[i]]
                i+=1
            elif s[i]=='X' and i+1<len(s) and s[i+1] in 'LC':
                ans += dic[s[i+1]]-dic[s[i]]
                i+=1
            elif s[i]=='C' and i+1<len(s) and s[i+1] in 'DM':
                ans += dic[s[i+1]]-dic[s[i]]
                i+=1
            else:
                ans += dic[s[i]]
            i+=1
        return ans
