class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        pre_max = [0] * n 
        post_max = [0] * n

        max_curr = height[0]
        for i in range(n):
            if height[i]>max_curr:
                max_curr = height[i]
            pre_max[i]=max_curr
        
        max_curr = height[-1]
        for i in range(n-1,-1,-1):
            if height[i]>max_curr:
                max_curr = height[i]
            post_max[i]=max_curr

        ans = [0] * n
        for i in range(n):
            ans[i] = min(pre_max[i],post_max[i])-height[i]
        
        return sum(ans)