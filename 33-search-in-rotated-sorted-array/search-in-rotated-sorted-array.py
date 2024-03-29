class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            mid = int(l+(r-l)/2)
            if target == nums[mid]:
                return mid
            else:
                if nums[mid]>nums[r]:
                    if target>=nums[l] and target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                else:
                    if target>nums[mid] and target<=nums[r]:
                        l=mid+1
                    else:
                        r=mid-1
        return -1