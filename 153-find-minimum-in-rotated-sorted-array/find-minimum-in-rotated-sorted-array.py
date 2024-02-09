class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = int((l+r)/2)
            if mid>0 and mid<len(nums) and nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            if nums[mid]>nums[r]:
                l = mid+1
            elif nums[mid]<nums[r]:
                r=mid-1
        
        return nums[l]
            
            