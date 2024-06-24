class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queue = deque()
        ans = 0
        for i in range(len(nums)):
            while queue and i-queue[0]>=k:
                queue.popleft()
                ans+=1

            if (nums[i]+len(queue))%2==0:
                if i>len(nums)-k:
                    return -1
                queue.append(i)
        
        return ans+len(queue)