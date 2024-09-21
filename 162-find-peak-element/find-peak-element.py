class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i,j = 1, len(nums)-2
        if len(nums)==1 or nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return j+1
        while i<=j:
            mid = i + (j-i)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid-1]:
                j=mid-1
            elif nums[mid]<nums[mid+1]:
                i=mid+1
