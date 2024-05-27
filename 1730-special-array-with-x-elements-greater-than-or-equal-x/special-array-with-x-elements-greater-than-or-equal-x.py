class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)+1):
            cnt = 0
            for x in nums:
                if x>=i:
                    cnt+=1
                if cnt>i:
                    break
            if cnt==i:
                return i
        
        return -1