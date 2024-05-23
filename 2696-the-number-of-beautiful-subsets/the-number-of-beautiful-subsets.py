class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        self.ans = []
        nums.sort()
        cnt = [0] * (nums[-1]+1)

        def sub(ind,curr):
            self.ans.append(curr.copy())
            
            for i in range(ind,len(nums)):
                if (nums[i]-k)<=0 or cnt[nums[i]-k]==0:
                    curr.append(nums[i])
                    cnt[nums[i]]+=1
                    sub(i+1,curr)
                    cnt[nums[i]]-=1
                    curr.pop()
        
        sub(0,[])
        return len(self.ans)-1