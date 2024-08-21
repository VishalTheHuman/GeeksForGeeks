#User function Template for python3
from collections import defaultdict
class Solution:
    def possible_paths(self, edges, n, s, d):
        path_count = 0
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
        def dfs(node, visited=[]):
            if node in visited:
                return
            nonlocal d, path_count
            if node==d:
                path_count+=1
                return
            for n in graph[node]:
                dfs(n)
        dfs(s)
        return path_count

