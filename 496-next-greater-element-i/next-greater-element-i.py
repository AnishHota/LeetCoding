class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dic = {}
        stack = []
        stack.append(nums2[0])

        for i in range(1,len(nums2)):
            while stack and nums2[i]>stack[-1]:
                dic[stack[-1]]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
    
        
        return (dic.get(n,-1) for n in nums1)

        