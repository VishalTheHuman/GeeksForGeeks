class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        queue = deque([])
        count = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
         
        moves = [
            (0, 1), 
            (1, 0), 
            (0,-1), 
            (-1,0)
        ]
        while queue:
            currentLength = len(queue)
            newQueue = []
            for idx in range(currentLength):
               i, j = queue.popleft()
               for i_c, j_c in moves: 
                   if 0<=(i+i_c)<len(grid) and 0<=(j+j_c)<len(grid[0]) and grid[i+i_c][j+j_c]==1:
                       newQueue.append((i+i_c, j+j_c))
                       grid[i+i_c][j+j_c] = 2
            queue = deque(newQueue)
            count += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return count if count >-1 else 0

from collections import deque
