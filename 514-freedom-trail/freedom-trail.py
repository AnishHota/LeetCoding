class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        chr_ind = defaultdict(list)
        for i,x in enumerate(ring):
            chr_ind[x].append(i)
        n = len(ring)
        dp = [0]*n

        
        for i in reversed(range(len(key))):
            new_dp = [float('inf')]*n
            for j in range(n):
                for x in chr_ind[key[i]]:
                    temp_min = min(n-abs(j-x), abs(j-x))
                    new_dp[j] = min(temp_min+dp[x]+1, new_dp[j])
            dp = new_dp
            
        
        return dp[0]


            
        