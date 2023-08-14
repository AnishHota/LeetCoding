class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-i for i in stones]
        heapq.heapify(self.heap)

        while len(self.heap)>=2:
            x = -self.heap[0]
            heapq.heappop(self.heap)
            y = -self.heap[0]
            heapq.heappop(self.heap)
            if x!=y:
                heapq.heappush(self.heap,-abs(x-y))
        
        if self.heap:
            return -self.heap[0]
        
        return 0