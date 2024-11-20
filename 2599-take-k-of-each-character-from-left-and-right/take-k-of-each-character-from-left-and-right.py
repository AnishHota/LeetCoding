class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = Counter(s)
        freq = {x:freq[x]-k for x in freq.keys()}
        if k==0:
            return 0
        if len(freq)!=3:
            return -1
        if freq['a']<0 or freq['b']<0 or freq['c']<0:
            return -1
        cnt = {c:0 for c in 'abc'}
        l = 0
        ans = -1
        for r,c in enumerate(s):
            cnt[c]+=1
            while l<=r and cnt[c]>freq[c]:
                cnt[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)

        if ans==-1:
            return ans
        return len(s)-ans
