import collections
import heapq
class Solution:
    def solve(self, A):
        R, C = len(A), len(A[0])
        
        def neighbors(r, c):
            if r == R and c == C:
                for k in range(R):
                    yield k, 0
                    yield k, C-1
                for k in range(1, C-1):
                    yield 0, k
                    yield R-1, k
            else:
                for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                    if 0 <= nr < R and 0 <= nc < C:
                        yield nr, nc
        
        pq = [(0, R, C)]
        dist = collections.defaultdict(lambda: float('inf'))
        while pq:
            d, r, c = heapq.heappop(pq)
            if d > dist[r, c]: continue
            for nr, nc in neighbors(r, c):
                d2 = max(d, A[nr][nc])
                if d2 < dist[nr, nc]:
                    dist[nr, nc] = d2
                    heapq.heappush(pq, (d2, nr, nc))
        
        return sum(dist[r,c] - A[r][c] for r in range(R) for c in range(C))
                