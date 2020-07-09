"""
DFS
"""
class Solution:
    def numIslands(self, grid) -> int:
        def dfs(grid, r, c):
            grid[r][c] = 0
            nr, nc = len(grid), len(grid[0])
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                    dfs(grid, x, y)

        nr, nc = len(grid), len(grid[0])
        if nr == 0:
            return 0
        num_land = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    num_land += 1
                    dfs(grid, i, j)
        return num_land

"""
BFS
"""
import collections

class Solution:
    def numIslands(self, grid) -> int:

        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_land = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    num_land += 1
                    grid[i][j] = '0'
                    neighboors = collections.deque([(i, j)])
                    while neighboors:
                        r, c = neighboors.popleft()
                        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighboors.append((x, y))
                                grid[x][y] = '0'

        return num_land