class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def sub(s):
            if s<0: return 0
            dic = defaultdict(int)
            l= 0
            ans = 0
            for r in range(len(nums)):
                dic[nums[r]]+=1
                while len(dic)>s:
                    dic[nums[l]]-=1
                    if dic[nums[l]]==0:
                        dic.pop(nums[l])
                    l+=1
                ans+=r-l+1
            return ans

        return sub(k)-sub(k-1)
        