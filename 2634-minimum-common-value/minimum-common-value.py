class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p,q = 0,0
        m = len(nums1)-1
        n = len(nums2)-1
        while p<=m and q<=n:
            if nums1[p]==nums2[q]:
                return nums1[p]
            elif nums1[p]<nums2[q]:
                p+=1
            else:
                q+=1
        
        return -1
        