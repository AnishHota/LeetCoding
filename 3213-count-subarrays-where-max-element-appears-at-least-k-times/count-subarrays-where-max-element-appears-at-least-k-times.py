class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = max(nums)
        l,ans = 0,0
        cnt=0
        for r in range(len(nums)):
            if nums[r]==n:
                cnt+=1
            while cnt>=k:
                cnt -= nums[l]==n
                l+=1
            ans+=l
        return ans     