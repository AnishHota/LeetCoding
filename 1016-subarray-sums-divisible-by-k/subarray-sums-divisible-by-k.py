class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        hash = defaultdict(int)
        ans = 0
        for x in nums:
            prefix += x
            num = prefix%k    
            if num==0:
                ans+=1
            if num in hash:
                ans+=hash[num]
                hash[num]+=1             
            else:
                hash[num]+=1
        
        return ans