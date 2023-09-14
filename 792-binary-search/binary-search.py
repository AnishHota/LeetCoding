class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums)-1

        while i<=j:
            mid = (i+j)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                i=mid+1
            else:
                j=mid-1

        return -1
        