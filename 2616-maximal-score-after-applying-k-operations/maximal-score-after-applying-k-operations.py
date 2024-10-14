class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapify(heap)
        score = 0
        while k!=0:
            n = heappop(heap)
            score += -1*n
            heappush(heap,math.floor(n/3))
            k-=1
        
        return score
            