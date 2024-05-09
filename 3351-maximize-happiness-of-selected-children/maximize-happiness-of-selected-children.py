class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        arr =[]
        for i in range(len(happiness)):
            heappush(arr,-happiness[i])
        
        ans = 0
        for i in range(k):
            l = -heappop(arr)
            ans += max(l-i,0)
        
        return ans