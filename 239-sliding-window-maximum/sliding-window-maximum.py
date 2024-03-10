class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        q = collections.deque()
        m = float("-inf")
        ans = []
        for r in range(len(nums)):
            if r>=k:
                ans.append(q[0])
                if q[0]==nums[l]:
                    q.popleft()
                l+=1
            if not q:
                q.append(nums[r])
            else:
                while q and q[-1]<nums[r]:
                    q.pop()
                q.append(nums[r])
        ans.append(q[0])
        return ans
                    
