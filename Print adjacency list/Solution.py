
from typing import List
from collections import defaultdict

class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(V)]
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        return graph
            
