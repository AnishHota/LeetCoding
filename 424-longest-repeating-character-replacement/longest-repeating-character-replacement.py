class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r, l = 0,0
        has = [0]*26
        ans = 0
        maxF = 0
        while l<=r and r<len(s):
            has[ord(s[r])-65]+=1
            maxF = max(has[ord(s[r])-65],maxF)  
            while (r-l+1)-maxF>k:
                has[ord(s[l])-65]-=1
                l+=1
                # maxF = max(has)
            ans = max(ans,r-l+1)
            r+=1
        return ans



