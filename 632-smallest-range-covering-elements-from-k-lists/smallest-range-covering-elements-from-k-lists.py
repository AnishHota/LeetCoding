class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        arridx = [0]*n
        heap = []
        minr = float("inf")
        maxr = -float('inf')
        for i in range(n):
            minr = min(minr,nums[i][0])
            maxr = max(maxr,nums[i][0])
            heappush(heap,(nums[i][0],i))

        ans = [minr,maxr]

        while heap:
            a,idx = heappop(heap)
            if ans[1]-ans[0] > maxr - a :
                ans = [a,maxr]
            if arridx[idx]+1<len(nums[idx]):
                arridx[idx]+=1
                new_a = nums[idx][arridx[idx]]
                maxr = max(maxr,new_a)  
                heappush(heap,(new_a,idx))
            else:
                break
        return ans
            
