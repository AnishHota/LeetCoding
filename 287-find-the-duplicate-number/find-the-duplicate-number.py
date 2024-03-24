class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        dummy = 0
        while dummy!=slow:
            slow = nums[slow]
            dummy = nums[dummy]
        
        return slow