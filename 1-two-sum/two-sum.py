class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i,num in enumerate(nums):
            if target-num in ind.keys():
                return [i,ind[target-num]]
            ind[num]=i
        