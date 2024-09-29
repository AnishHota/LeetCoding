class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        ans = 0
        while j<len(nums):
            if nums[j]==0:
                k-=1
            if k<0:
                while i<len(nums) and k<0:
                    if nums[i]==0:
                        k+=1
                    i+=1
            ans = max(j-i+1,ans)
            j+=1
        
        return ans