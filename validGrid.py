from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0]
        }
    
        rows, cols = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])
        minCost = {(0, 0): 0}

        while q:
            r, c, cost = q.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return cost
            
            for d in direction:
                dr, dc = direction[d]
                nr, nc = r + dr, c + dc
                nCost = cost if d == grid[r][c] else cost + 1
                if(nr < 0 or nc < 0 or nr == rows or nc == cols or nCost >= minCost.get(nr, nc), float("inf")):
                    continue
                minCost[(nr, nc)] = nCost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, nCost))
                else:
                    q.append((nr, nc, nCost))
                    
                
        

if __name__ == '__main__':
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    obj = Solution()
    cost = obj.minCost(grid)
    print("The minimum cost to traverse the grid is",cost)