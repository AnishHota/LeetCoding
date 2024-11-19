class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        curr = set()
        curr_sum = 0
        for r in range(len(nums)):
            # print(l,r,curr,ans,curr_sum)
            if nums[r] in curr:
                while l<r and nums[l]!=nums[r]:
                    curr.remove(nums[l])
                    curr_sum -= nums[l]
                    l+=1
                curr.remove(nums[l])
                curr_sum -= nums[l]
                l+=1
            if r-l+1>k:
                curr_sum-=nums[l]
                curr.remove(nums[l])
                l+=1

            curr_sum+=nums[r]
            curr.add(nums[r])

            if r-l+1==k:
                ans = max(ans,curr_sum)
            
        return ans       
            