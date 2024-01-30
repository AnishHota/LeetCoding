class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        n = len(nums)
        nums = sorted(nums)
        for i in range(n):
            l = i+1
            r = n-1
            target = -1*nums[i]
            while l<r:
                if l==i:
                    l+=1
                elif r==i:
                    r-=1
                else:
                    if nums[l]+nums[r]==target:
                        ans.add((nums[l],nums[r],nums[i]))
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif nums[l]+nums[r]>target:
                        r-=1
                    else:
                        l+=1
        return list(ans)

        