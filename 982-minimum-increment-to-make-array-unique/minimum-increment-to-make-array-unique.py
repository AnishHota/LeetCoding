class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # seen = set()
        # ans = 0
        # for i,x in enumerate(nums):
        #     if x in seen:
        #         temp = x
        #         while temp in seen:
        #             temp+=1
        #         ans += temp-x
        #         seen.add(temp)
        #     else:
        #         seen.add(x)
        
        # return ans

        # nums.sort()
        # ans = 0
        # for i,x in enumerate(nums):
        #     if i==0:
        #         continue
        #     if x<=nums[i-1]:
        #         ans += nums[i-1]+1-x
        #         nums[i]=nums[i-1]+1
        # return ans

        freq = Counter(nums)
        ans = 0

        for i in range(min(nums),max(nums)+len(nums)):
            if i in freq and freq[i]>1:
                ans+=freq[i]-1
                freq[i+1] += freq[i]-1
                freq[i]=1
        
        return ans