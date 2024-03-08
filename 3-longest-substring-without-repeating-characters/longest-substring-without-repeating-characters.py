class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = {}
        ans = 0

        l,r = 0,0
        while r<len(s):
            if s[r] in ind and ind[s[r]]!=-1:
                ans = max(ans,r-l)
                while l<=ind[s[r]]+1:
                    ind[s[l]]=-1
                    l+=1
            ind[s[r]]=r
            r+=1
        
        return max(ans,r-l)