class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0,len(s)-1

        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                while l<=r and s[l]==s[l-1]:
                    l+=1
                while l<=r and s[r]==s[r+1]:
                    r-=1
            else:
                return (r-l+1)
        
        if r==l:
            return 1
        return 0

            
        