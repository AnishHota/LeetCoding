class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        inc_l = 0
        inc_r = 0
        dec_l, dec_r = 0,0
        ans = 0

        for i in range(1,n-1):
            inc_l,inc_r = 0,0
            dec_l, dec_r = 0,0
            for j in range(i):
                if rating[i]>rating[j]:
                    inc_l+=1
                elif rating[i]<rating[j]:
                    dec_l+=1
            for j in range(i+1,n):
                if rating[i]<rating[j]:
                    inc_r+=1
                elif rating[i]>rating[j]:
                    dec_r+=1
            ans+= inc_l*inc_r + dec_l*dec_r

        return ans