class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        ans = []
        for i,n in enumerate(nums):
            l, r = i+1, len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                threeS = n+nums[l]+nums[r]
                if threeS<0:
                    l+=1
                elif threeS>0:
                    r-=1
                else:
                    ans.append([n,nums[l],nums[r]])
                    print(i,l,r)
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans

        