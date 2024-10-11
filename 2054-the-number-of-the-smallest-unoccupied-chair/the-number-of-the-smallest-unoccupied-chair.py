class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]

        times = sorted(times, key=lambda x: x[0])
        print(times)
        chairs = 0
        heap = []
        chheap = []
        for a,d in times:
            if (heap and a>=heap[0][0]) or chheap:
                while heap and a>=heap[0][0]:
                    chidx = heapq.heappop(heap)[1]
                    heapq.heappush(chheap,chidx)
                idx = heappop(chheap)
                heapq.heappush(heap,(d,idx))
                if a == target[0]:
                    return idx
            else:
                heapq.heappush(heap,(d,chairs))
                if a == target[0]:
                    return chairs
                chairs+=1
        return 0
            
