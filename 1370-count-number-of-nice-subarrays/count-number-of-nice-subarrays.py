class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def sub(k):
            ans = 0
            s = 0
            j = 0
            for i in range(len(nums)):
                s += nums[i]%2
                while s>k:
                    s -= nums[j]%2
                    j+=1
                ans += i-j+1
            return ans

        return sub(k)-sub(k-1)  
                    