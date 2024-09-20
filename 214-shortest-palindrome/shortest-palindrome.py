class Solution:
    def shortestPalindrome(self, s: str) -> str:
        base = 31
        po = 1
        mod = 10**9+7
        lst_ind = 0
        prefix = 0
        suffix = 0
        for i in range(len(s)):
            c = ord(s[i])-ord('a')+1
            prefix = (prefix*base + c) % mod
            suffix = (suffix + c*po) % mod
            po = (po*base) % mod
            if prefix==suffix:
                lst_ind = i+1
        
        return s[lst_ind:][::-1] + s

        
            