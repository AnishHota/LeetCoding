class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        i=0
        maxln=0
        for num in st:
            if num-1 not in st:
                temp = num
                while temp+1 in st:
                    temp = temp+1
                maxln = max(maxln,temp+1-num)
        
        return maxln


                
