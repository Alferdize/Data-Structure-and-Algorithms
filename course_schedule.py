class Solution:
    def solve(self, matrix):
        visited=[False for _ in matrix]
        checked=[False for _ in matrix]
        def dfs(i):
            if visited[i]: return False
            if checked[i]: return True
            visited[i]=True
            for j in matrix[i]:
                if not dfs(j):
                    return False
            visited[i]=False
            checked[i]=True
            return True
        for i in range(len(matrix)):
            if not dfs(i):
                return False
        return True