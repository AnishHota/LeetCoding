class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0]=1

        preFixSum = 0
        result = 0
        for n in nums:
            preFixSum += n

            if preFixSum-k in dic:
                result = result + dic[preFixSum-k]
            
            if preFixSum in dic:
                dic[preFixSum] += 1
            else:
                dic[preFixSum] = 1
        
        return result