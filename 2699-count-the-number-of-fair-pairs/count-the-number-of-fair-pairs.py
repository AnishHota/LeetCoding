class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def countpairs(val):
            cnt = 0
            j = len(nums)-1

            for i in range(len(nums)):
                while i<j and nums[i]+nums[j]>val:
                    j-=1
                if i==j:
                    break
                cnt += max(0,j-i)
            return cnt
        
        return countpairs(upper) - countpairs(lower-1)



