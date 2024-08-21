from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        colorArray = [-1]*V
        
        def bfs(node):
            queue = deque([node])
            color = 0
            while queue: 
                l = len(queue)
                for _ in range(l):
                    node = queue.popleft()
                    colorArray[node] = color
                    for x in adj[node]:
                        if colorArray[x] == -1:
                            queue.append(x)
                        if colorArray[x] == colorArray[node]: 
                            return False
                color = (color + 1) % 2
            return True
        
        for i in range(V): 
            if colorArray[i]==-1:
                if not bfs(i):
                    return False
        
        return True
        
