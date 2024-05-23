class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        self.ans = 0

        def sub(ind, cnt):
            for i in range(ind,len(nums)):
                if cnt[nums[i]-k]==0 and cnt[nums[i]+k]==0:
                    self.ans+=1
                    cnt[nums[i]]+=1
                    sub(i+1,cnt)
                    cnt[nums[i]]-=1
        
        sub(0,defaultdict(int))
        return self.ans