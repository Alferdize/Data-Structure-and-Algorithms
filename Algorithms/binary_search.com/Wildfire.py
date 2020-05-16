import collections
class Solution:
    def solve(self, matrix):
        # Write your code here
        if not matrix:
            return 0
        self.row = len(matrix)
        self.col = len(matrix[0])
        days = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = self.getQueue(matrix)
        tree_to_be_burned = self.getTreeCount(matrix)
        burned = 0
        if tree_to_be_burned == 0:
            return 0
        while q:
            days += 1
            size = len(q)
            
            for _ in range(size):
                i, j = q.popleft()
                
                for r, c in directions:
                    nr = i + r
                    nc = j + c
                    if 0 <= nr < self.row and 0 <= nc < self.col and matrix[nr][nc] == 1:
                        matrix[nr][nc] = 2
                        q.append((nr, nc))
                        burned += 1
            
            if tree_to_be_burned == burned:
                return days
        
        return -1 if tree_to_be_burned != burned else days
    
    def getQueue(self, matrix):
        q = collections.deque()
        
        for i in range(self.row):
            for j in range(self.col):
                if matrix[i][j] == 2:
                    q.append((i, j))
        return q
    
    def getTreeCount(self, matrix):
        count = 0
        
        for i in range(self.row):
            for j in range(self.col):
                if matrix[i][j] == 1:
                    count += 1
        
        return count