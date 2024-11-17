class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        curr = 0
        ans = float('inf')
        l = 0
        q = deque()
        for i,x in enumerate(nums):
            curr += x
            if curr>=k:
                ans = min(ans, i+1)
            
            while q and curr-q[0][0]>=k:
                _,idx = q.popleft()
                ans = min(ans,i-idx)
            
            while q and curr<q[-1][0]:
                q.pop()
            
            q.append((curr,i))

        return ans if ans!=float('inf') else -1