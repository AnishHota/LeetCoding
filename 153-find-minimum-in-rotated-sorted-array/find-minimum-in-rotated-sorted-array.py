class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        if nums[0]<=nums[-1]:
            return nums[0]

        while l<r:
            mid = int(l+(r-l)/2)
            if nums[l]<nums[r]:
                return nums[l]
            elif nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
            
        return nums[l]