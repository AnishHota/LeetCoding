from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for _ in range(len(nums)+1)]
        freq = Counter(nums)
        result = []
        for x in freq:
            ans[freq[x]].append(x)
        
        for x in range(len(ans)-1,-1,-1):
            if ans[x]:
                result+=ans[x]
                k-=len(ans[x])
            if k<=0:
                return result[:len(result)+k]
        
        return result