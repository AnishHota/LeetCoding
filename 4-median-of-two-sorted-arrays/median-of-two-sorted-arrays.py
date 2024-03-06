class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1

        m, n = len(nums1), len(nums2)

        half = (m+n)//2
        l,r = 0,m-1

        while True:
            mid = (r+l)//2
            remaining = half-mid-2
            Aleft = nums1[mid] if mid>=0 else float("-inf")
            Bleft = nums2[remaining] if remaining>=0 else float("-inf")
            Aright = nums1[mid+1] if (mid+1)<m else float("inf")
            Bright = nums2[remaining+1] if (remaining+1)<n else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                return min(Aright,Bright) if (n+m)%2!=0 else (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=mid-1
            else:
                l=mid+1