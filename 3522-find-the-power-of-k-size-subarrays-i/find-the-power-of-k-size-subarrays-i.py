class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        
        ans = []
        l = 0
        n = len(nums)
        isConsec = True
        for r in range(n):
            if nums[r]-nums[r-1]!=1:
                isConsec = False
            else:
                isConsec = True
            if not isConsec:
                while l<r and l+k-1<n:
                    ans.append(-1)
                    l+=1
                l = r
            elif r-l==k-1:
                ans.append(nums[r])
                l+=1
        
        return ans

