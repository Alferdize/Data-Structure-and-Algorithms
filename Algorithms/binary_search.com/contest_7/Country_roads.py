from collections import defaultdict
class Solution:
    def solve(self, source, dest, population):
        # Write your code here
        graph = defaultdict(list)
        for u, v in zip(source, dest):
            graph[u].append(v)
            graph[v].append(u)
        ans = [0, 0]
        def dfs(node, par=-1, color=0):
            ans[color] += population[node]
            for nei in graph[node]:
                if nei != par:
                    dfs(nei, node, color ^ 1)
        
        dfs(0)
        return max(ans)