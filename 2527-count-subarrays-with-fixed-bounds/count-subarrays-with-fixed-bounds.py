class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l = -1
        ans = 0
        prevMinInd = -1
        prevMaxInd = -1
        for r,x in enumerate(nums):
            if x<minK or x>maxK:
                l=r
            if x==minK:
                prevMinInd = r
            if x==maxK:
                prevMaxInd = r
            ans+=max(0,min(prevMinInd,prevMaxInd)-l)
        
        return ans

        