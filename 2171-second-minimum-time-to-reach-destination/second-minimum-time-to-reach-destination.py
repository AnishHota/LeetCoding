class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adjmat = defaultdict(list)
        for s,d in edges:
            adjmat[s].append(d)
            adjmat[d].append(s)
        
        dist = [[float('inf'),float('inf')] for _ in range(n+1)]
        q = []
        heappush(q,(0,1))

        while q:
            t,node = heappop(q)
            if node==n and dist[node][1]!=float('inf'):
                return dist[node][1]
            t_time = time
            if (t//change)%2==1:
                t_time += (t//change+1)*change-t

            for neigh in adjmat[node]:
                if t+t_time < dist[neigh][0]:
                    dist[neigh][0], dist[neigh][1] = t + t_time, dist[neigh][0]
                    heappush(q,(t+t_time,neigh))
                if t+t_time> dist[neigh][0] and t+t_time<dist[neigh][1]:
                    dist[neigh][1] = t+t_time
                    heappush(q,(t+t_time,neigh))
        
        return -1
                
                
