#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visited = [False]*V
        pathNodeVisited = [False]*V
        
        def dfs(node):
            if pathNodeVisited[node]: 
                return True
            visited[node] = True
            pathNodeVisited[node] = True
            for x in adj[node]:
                if not visited[x]:
                    if dfs(x):
                        return True
                elif pathNodeVisited[x]:
                    return True
            pathNodeVisited[node] = False
            return False
            
        for i in range(V):
            if not visited[i]: 
                if dfs(i): 
                    return True
                
        return False




