class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        l,r = 0, len(nums)-1
        ind = len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                ans[ind]=nums[l]**2
                l+=1
            else:
                ans[ind]=nums[r]**2
                r-=1
            ind-=1
        return ans
        
