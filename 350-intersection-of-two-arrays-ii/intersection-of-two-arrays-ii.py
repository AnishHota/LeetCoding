class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1

        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for x in cnt1:
            if x in cnt2:
                ans += [x]*min(cnt1[x],cnt2[x])
        
        return ans


        