class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited = [False]*V
        stack = []
        
        def dfs(node):
            for n in adj[node]:
                if visited[n]:
                    continue
                dfs(n)
            visited[node] = True
            stack.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        return stack[::-1]
        

