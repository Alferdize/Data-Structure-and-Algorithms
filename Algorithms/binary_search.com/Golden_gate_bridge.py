from itertools import product
from collections import deque
class Solution:
    def solve(self, A):
        R, C = len(A), len(A[0])
        
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        for r0, c0 in product(range(R), range(C)):
            if A[r0][c0] == 1:
                break
        
        # find first island
        stack = [(r0, c0)]
        seen = {(r0, c0)}
        while stack:
            node = stack.pop()
            for nei in neighbors(*node):
                if nei not in seen and A[nei[0]][nei[1]]:
                    seen.add(nei)
                    stack.append(nei)
        
        queue = deque([(r, c, 0) for r, c in seen])
        while queue:
            r, c, d = queue.popleft()
            if d and A[r][c] == 1:
                return d - 1
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei[0], nei[1], d+1))