import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        store = set()
        M, N = len(grid), len(grid[0])
        moves = [
            (0, 1), 
            (1, 0), 
            (0,-1), 
            (-1,0)
        ]
        
        def dfs(i, j):
            nonlocal base
            result.append((i-base[0], j-base[1]))
            for i_c, j_c in moves: 
                n_i, n_j = i+i_c, j+j_c
                if 0<=n_i<M and 0<=n_j<N and grid[n_i][n_j]: 
                    grid[n_i][n_j] = 0
                    dfs(n_i,n_j)
            
        result = []    
        for i in range(M): 
            for j in range(N): 
                if grid[i][j]:
                    base = (i,j)
                    grid[i][j] = 0
                    dfs(i,j)
                    store.add(tuple(result))
                    result.clear()
                
        return len(store)

