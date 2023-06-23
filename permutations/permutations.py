class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        stack = []
        path = []
        stack.append([nums,path])
        res = []

        while stack:
            nums,path = stack.pop()
            
            if not nums:
                res.append(path)
            
            for i in range(len(nums)):
                tempNums = nums[:i] + nums[i+1:]
                stack.append([tempNums,path+[nums[i]]])
        
        return res