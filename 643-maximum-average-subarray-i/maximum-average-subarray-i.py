class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        res = curr
        j = 0
        for i in range(k,len(nums)):
            curr -= nums[j]
            curr += nums[i]
            if curr>res:
                res=curr
            j+=1
        
        return res/k
