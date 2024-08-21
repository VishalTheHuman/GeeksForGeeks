from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(node,visited = [],parent=0):
            if node in visited:
                return True
            for n in adj[node]:
                if n==parent:
                    continue
                if dfs(n,visited+[node],node):
                    return True
            return False
        for i in range(V):
            if dfs(i,[],i):
                return True
        return False
