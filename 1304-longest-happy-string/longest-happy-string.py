class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cnt = Counter({'a':a,'b':b,'c':c})
        ans='#'
        while cnt:
            (a,_),(b,_) = cnt.most_common(2)
            if a==ans[-1]==ans[-2]:
                a=b
            if cnt[a]<1:
                break
            ans+=a
            cnt[a]-=1

        return ans[1:]
        
