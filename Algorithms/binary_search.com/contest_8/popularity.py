class Solution:
    def solve(self, edges):
        from collections import defaultdict
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count = defaultdict(int)
        
        def dfs(x, parent):
            count[x] = 1
            for nb in adj[x]:
                if nb == parent:
                    continue
                count[x] += dfs(nb, x)
            return count[x]
        dfs(0, -1)
        ans = []
        for a, b in edges:
            x = min(count[a], count[b])
            ans.append(x * (count[0] - x))
        return ans