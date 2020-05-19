from collections import deque
class Solution:
    def solve(self, grid):
        r = len(grid)
        c = len(grid[0])
        dp = [[-1 for _ in range(c)] for _ in range(r)]
        
        def nei(i, j):
            if i-1 >= 0: yield (i-1, j)
            if i+1 < r: yield (i+1, j)
            if j-1 >= 0: yield (i, j-1)
            if j+1 < c: yield (i, j+1)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0: continue
                d = deque([(i, j, 0)])
                seen = {(i, j)}
                while d:
                    x, y, l = d.popleft()
                    if grid[x][y] == 0:
                        dp[x][y] = max(dp[x][y], l)
                        break
                
                    for x1, y1 in nei(x, y):
                        if (x1, y1) not in seen:
                            d.append((x1, y1, l+1))
                            seen.add((x1, y1))
                            
        max_val = -1
        for row in dp:
            for val in row:
                max_val = max(max_val, val)
                
        return max_val