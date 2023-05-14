class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [None] * len(nums)
        nex = [None] * len(nums)

        prev[0]=nums[0]
        for i in range(1,len(nums)):
            prev[i]=prev[i-1]*nums[i]

        nex[len(nums)-1]=nums[-1]
        for j in reversed(range(len(nums)-1)):
            nex[j]=nex[j+1]*nums[j]

        for x in range(len(nums)):
            if x==0:
                nums[x]=nex[1]
            elif x==len(nums)-1:
                nums[x]=prev[-2]
            else:
                nums[x]=prev[x-1]*nex[x+1]
        
        return nums
