class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        cnt_a = 0
        ans = 0
        for i in range(n-1,-1,-1):
            if s[i]=='a':
                cnt_a+=1
            else:
                ans = min(ans+1,cnt_a)


        return ans