class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] = 0
            else:
                nums[i]=1
        
        def sub(k):
            l = 0
            ans = 0
            s=0
            for r in range(len(nums)):
                s+=nums[r]
                while l<=r and s>k:
                    s-=nums[l]
                    l+=1
                ans+=r-l+1
            return ans

        return sub(k)-sub(k-1)