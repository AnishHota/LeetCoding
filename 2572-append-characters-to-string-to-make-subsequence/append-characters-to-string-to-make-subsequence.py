class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ind = 0

        for i in range(len(s)):
            if s[i]==t[t_ind]:
                t_ind+=1
            if t_ind==len(t):
                return 0
        
        return len(t)-t_ind

        