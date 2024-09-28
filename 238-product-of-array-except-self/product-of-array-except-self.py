class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        n = len(nums)
        arr= [1]*(n)

        for i in range(n):
            arr[i] *= pre
            arr[n-i-1] *= post
            pre *= nums[i]
            post *= nums[n-i-1]

        return arr