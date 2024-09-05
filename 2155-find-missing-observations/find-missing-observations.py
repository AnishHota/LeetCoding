class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean*(n+len(rolls)) - sum(rolls)

        if sum_n<n or sum_n>n*6:
            return []
        
        ans = [1]*n
        sum_n -= n
        i = 0
        while sum_n!=0:
            if sum_n>=5:
                ans[i]=6
                sum_n-=5
            else:
                ans[i]=sum_n+1
                sum_n=0
            i+=1
        
        return ans