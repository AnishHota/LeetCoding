class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = -1
        ans = 0
        prevMinInd = -1
        prevMaxInd = -1
        for r in range(len(nums)):
            if nums[r]<minK or nums[r]>maxK:
                l=r
            if nums[r]==minK:
                prevMinInd = r
            if nums[r]==maxK:
                prevMaxInd = r
            
            ans+=max(0,min(prevMinInd,prevMaxInd)-l)
            print(prevMinInd, prevMaxInd,l,ans )
        
        return ans

        