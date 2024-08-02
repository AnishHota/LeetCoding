class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        nums += nums[:total]
        n = len(nums)
        i,j = 0,total
        ans = (j-i)-sum(nums[i:j])
        curr = ans
        while j<n:
            if nums[i]==0:
                curr -= 1
            if nums[j]==0:
                curr += 1
            ans = min(ans, curr)
            i+=1
            j+=1

        return ans
            
                


