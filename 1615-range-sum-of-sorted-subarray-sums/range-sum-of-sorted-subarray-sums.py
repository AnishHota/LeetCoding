class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumarr = []
        modulo = 1000000007
        for i in range(n):
            sumi = nums[i]
            sumarr.append(sumi)
            for j in range(i+1,n):
                sumi += nums[j]
                sumarr.append(sumi)
        sumarr.sort()
        return sum(sumarr[left-1:right])%modulo
