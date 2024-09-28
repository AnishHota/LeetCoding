class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = [nums[0]]
        largest = [nums[-1]]
        n = len(nums)
        for i in range(1,len(nums)):
            smallest.append(min(nums[i],smallest[-1]))
            largest.append(max(nums[n-i-1],largest[-1]))
        
        largest = largest[::-1]
        for i in range(1,len(nums)-1):
            if smallest[i]<nums[i]<largest[i]:
                return True
        return False
