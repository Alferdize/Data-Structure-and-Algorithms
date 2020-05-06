class Solution:
    def solve(self, friends):
        num_connected_components = 0
        visited = set()
        for i in range(len(friends)):
            if i not in visited:
                connect(friends, visited, i)
                num_connected_components += 1
        return num_connected_components
        
        
def connect(graph, visited, vtx):
    visited.add(vtx)
    for nei in graph[vtx]:
        if nei not in visited:
            connect(graph, visited, nei)