#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q = [0]
        visited = [0]
        while q:
            for node in adj[q.pop(0)]:
                if node not in visited:
                    q.append(node)
                    visited.append(node)
        return visited
