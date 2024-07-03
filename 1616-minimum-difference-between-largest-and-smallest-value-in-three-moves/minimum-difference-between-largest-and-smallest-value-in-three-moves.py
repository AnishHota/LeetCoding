class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        
        minH = []
        maxH = []

        for x in nums:
            heapq.heappush(minH,x)
            heapq.heappush(maxH,-x)

        ans = float('inf')
        temp_max = []
        for i in range(4):
            temp_max.append(-1*heapq.heappop(maxH))
        temp_max.sort()

        for i in range(4):
            x = heapq.heappop(minH)
            y = temp_max[i]
            ans = min(ans,abs(x-y))

        return ans