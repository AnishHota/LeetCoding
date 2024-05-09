class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        # arr =[]
        # for i in range(len(happiness)):
        #     heappush(arr,-happiness[i])
        
        # ans = 0
        # for i in range(k):
        #     l = -heappop(arr)
        #     ans += max(l-i,0)
        
        # return ans

        happiness = sorted(happiness,reverse=True)
        
        ans = 0
        for i in range(k):
            if (happiness[i]-i)<0:
                break
            ans += happiness[i]-i
        
        return ans