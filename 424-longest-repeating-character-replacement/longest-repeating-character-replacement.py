class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0 for _ in range(26)]

        maxF = 0
        ans = 0
        l = 0
        for r in range(len(s)):
            freq[ord(s[r])-ord('A')]+=1
            maxF = max(maxF,freq[ord(s[r])-ord('A')])
            if (r-l+1)-maxF>k:
                freq[ord(s[l])-ord('A')]-=1
                l+=1
            ans = max(r-l+1,ans)
        return ans
            