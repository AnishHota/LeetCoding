class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        l,r = 0,len(height)-1
        ans = 0
        while l<=r:
            if height[l]<=height[r]:
                ans+=max(maxL-height[l],0)
                maxL = max(maxL,height[l])
                l+=1
            else:
                ans+=max(maxR-height[r],0)
                maxR = max(maxR,height[r])
                r-=1
        return ans