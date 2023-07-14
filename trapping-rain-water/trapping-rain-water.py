class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        l = 1
        r = n-2

        ans=0

        max_l = height[0]
        max_r = height[-1]

        while l<=r:

            if max_l<=max_r:
                if max_l<height[l]:
                    max_l = height[l]
                ans += max_l-height[l]
                l+=1
            else:
                if max_r<height[r]:
                    max_r = height[r]
                ans += max_r-height[r]
                r-=1
        
        return ans