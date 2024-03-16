class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        dic = {0:0}
        ans = 0
        for i,x in enumerate(nums,1):
            if x==1:
                s+=1
            else:
                s-=1
            if s in dic:
                ans = max(ans,i-dic[s])
            else:
                dic[s]=i
        return ans

        