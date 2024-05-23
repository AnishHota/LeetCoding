class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        self.ans = 0
        nums.sort()
        cnt = [0] * (nums[-1]+1)

        def sub(ind,curr):
            for i in range(ind,len(nums)):
                if (nums[i]-k)<=0 or cnt[nums[i]-k]==0:
                    self.ans+=1
                    curr.append(nums[i])
                    cnt[nums[i]]+=1
                    sub(i+1,curr)
                    cnt[nums[i]]-=1
                    curr.pop()
        
        sub(0,[])
        return self.ans