from heapq import heappop, heappush
from typing import List

class Solution:
    def trapRainWater(self, hm: List[List[int]]) -> int:
        rows, cols = len(hm), len(hm[0])
        visited = [[False] * cols for _ in range(rows)]

        min_heap = []

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (hm[i][j], i, j))
                    visited[i][j] = True

        res = 0

        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        while min_heap:
            height, r, c = heappop(min_heap)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    res += max(0, height - hm[nr][nc])
                    heappush(min_heap, (max(height, hm[nr][nc]), nr, nc))

        return res
    
if __name__ == '__main__':
    grid = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    obj = Solution()
    print("The total amount of water trapped is", obj.trapRainWater(grid))