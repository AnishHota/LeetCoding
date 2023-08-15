class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for x in nums:
            if x in dic:
                return True
            else:
                dic[x]=1

        return False 