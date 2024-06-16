class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        max_i = 0
        ans = 0
        i=0
        while max_i<target:
            if i<len(coins) and max_i+1>=coins[i]:
                max_i += coins[i]
                i+=1
            else:
                ans+=1
                max_i += max_i+1
        
        return ans

