class Solution:
    def solve(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] & 1 == 0:
                    yield nr, nc

        def bfs(r, c):
            queue = [(r, c)]
            dist = {(r, c): 0}
            for r, c in queue:
                if dist[r, c] > 15:
                    break
                for nr, nc in neighbors(r, c):
                    if (nr, nc) not in dist:
                        dist[nr, nc] = dist[r, c] + 1
                        queue.append((nr, nc))
            return dist
        dist = None
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val == 2:
                    ndist = bfs(r, c)
                    if dist is None:
                        dist = ndist
                    else:
                        for key in list(dist.keys()):
                            if key in ndist:
                                dist[key] = max(dist[key], ndist[key])
                            else:
                                del dist[key]
        return min(dist.values()) if dist else 0


"""
Testcase
matrix = [[2, 0, 1, 0],
[1, 0, 1, 2],
[0, 0, 2, 2]]
3
"""
