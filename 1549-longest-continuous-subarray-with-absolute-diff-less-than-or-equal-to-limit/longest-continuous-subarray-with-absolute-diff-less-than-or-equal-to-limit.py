class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        j = 0
        ans = 0
        for i in range(len(nums)):
            while max_dq and nums[i]>max_dq[-1]:
                max_dq.pop()
            max_dq.append(nums[i])
            while min_dq and nums[i]<min_dq[-1]:
                min_dq.pop()
            min_dq.append(nums[i])
            while abs(max_dq[0]-min_dq[0])>limit:
                if nums[j]==max_dq[0]:
                    max_dq.popleft()
                if nums[j]==min_dq[0]:
                    min_dq.popleft()
                j+=1
            ans = max(ans, i-j+1)
        
        return ans
