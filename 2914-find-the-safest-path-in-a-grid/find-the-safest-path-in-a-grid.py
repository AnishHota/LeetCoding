class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[0 for _ in range(n)] for _ in range(n)]
        q = collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]: q.append((i, j))
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            l = len(q)
            for _ in range(l):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and not distance[ni][nj] and not grid[ni][nj]:
                        q.append((ni, nj))
                        distance[ni][nj] = distance[i][j] - 1
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1: return 0

        pq = [(distance[0][0], 0, 0)]
        while pq:
            d, i, j = heapq.heappop(pq)
            if grid[i][j] == -1: continue
            grid[i][j] = -1
            if i == n - 1 and j == n - 1: return -d
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n: heapq.heappush(pq, (max(d, distance[ni][nj]), ni, nj))
        return -1