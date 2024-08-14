class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1]-nums[0]
        while low<=high:
            mid = low + (high-low)//2
            i,j = 0,1
            count=0
            while j<len(nums):
                while nums[j]-nums[i]>mid:
                    i+=1
                count += j-i
                j+=1
            if count<k:
                low = mid+1
            else:
                high = mid-1
                
        return low