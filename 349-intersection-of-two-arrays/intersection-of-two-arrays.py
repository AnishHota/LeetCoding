class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        arr = [0 for _ in range(1001)]
        for x in nums1:
            arr[x]=1
        ans = []
        for x in nums2:
            if arr[x]!=0:
                ans.append(x)
                arr[x]=0
        return ans
        

        