class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq= Counter(nums)
        for x,f in freq.items():
            heapq.heappush(heap,(f,x))
            if len(heap)==k+1:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res